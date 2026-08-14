import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from .atom import Atom

class Hydrogen_Bond:
    """Class Hydrogen_Bond.
    
    Parameters:
    atoms : list
    List of objects Atom: [Atom-donor, Atom-Hydrogen, Atom-Axceptor]. Sequence is important for calculation coolvar.
    Warning!!! Numeration starts from 0: if number of atom in chemcraft = 20, you should input 19.
    """

    def __init__(self, atoms):
        self.__atoms = atoms
    
    @property
    def atoms(self):
        """Return list of atoms"""
        return self.__atoms

    @property
    def colvar1(self):
        """Return float colvar (dist2-dist1)/2"""
        atoms = self.atoms
        hydrogen = atoms[1]
        donor = atoms[0]
        axceptor = atoms[2]
        colvar1 = (hydrogen.dist(donor)-hydrogen.dist(axceptor))/2
        return colvar1
    
    @property
    def colvar2(self):
        """Return float colvar (dist2+dist1)/2"""
        atoms = self.atoms
        hydrogen = atoms[1]
        donor = atoms[0]
        axceptor = atoms[2]
        colvar2 = (hydrogen.dist(donor)+hydrogen.dist(axceptor))/2
        return colvar2
    

class Hydrogen_Bonds:
    """Class Hydrogen_Bonds.
    
    Parameters:
    h_bonds : list
    List of objects Hydrogen_Bond.
    """

    def __init__(self, h_bonds):
        self.__h_bonds = h_bonds

    @property
    def h_bonds(self):
        """Return list of objs Hydrogen_Bond"""
        return self.__h_bonds

    @property
    def colvars1_list(self):
        """Return obj Colvars_Lists of list of colvar one"""
        colvars1_list = []
        h_bonds = self.h_bonds
        for h_bond in h_bonds:
            colvars1_list.append(h_bond.colvar1)
        return Colvars_Lists(colvars1_list)


class Colvars_Lists:
    """Class Colvars.
    
    Parameters:
    colvars_lsts : np.array
    Array, when row - list of colvar.
    """

    def __init__(self, colvars_lsts):
        self.__colvars_lsts  = colvars_lsts
    
    @property
    def colvars_lsts(self):
        return self.__colvars_lsts
    
    @property
    def dispersion(self):
        """Make list of collective variables disperdions. Return list of floats"""
        dispersions = []
        colvars_lsts = self.colvars_lsts
        for i in range(len(colvars_lsts)):
            disp_val_i = float(np.var(colvars_lsts[i]))
            dispersions.append(disp_val_i)
        return dispersions

    def colvar_transform(self, translation_matrix):
        """Translation_matrix - np.arrey. Translate colvars and retrun new np.arrey of colvars"""
        new_lst = ((self.colvars_lsts.T)@translation_matrix).T
        return Colvars_Lists(new_lst)
    
    def colvars_plot(self):
        """Draw graphs of density of distribution of colvars"""
        colors = ["black", "red", "blue", "green"]
        plt.figure(figsize=(10, 6))

        clvs = self.colvars_lsts
        
        if type(clvs[0]) != list:
            sns.kdeplot(clvs, color='black')
        
        else:
            for ind, clv in enumerate(clvs):
                sns.kdeplot(clv, color=colors[ind%4])
        
        plt.show()


class HB_Analyzer:
    """Class HB_Analyzer.
    
    """

    @staticmethod
    def hb_in_structure(structure, atoms_nums):
        """Only for NHN H-bonds! structure - obj Molecule, atoms_nums = [atom-donor, H, axceptor HB]. Return True if HB in structure."""
        max_hb_dist = 2.75
        min_hb_angle = 150
        coords = structure.atoms
        donor = coords[atoms_nums[0]]
        hydrogen = coords[atoms_nums[1]]
        acceptor = coords[atoms_nums[2]]
        return donor.dist(hydrogen, cell=structure.cell) <= max_hb_dist and acceptor.dist(hydrogen, cell=structure.cell) <= max_hb_dist and Atom.angle(donor, hydrogen, acceptor, cell=structure.cell) >= min_hb_angle

    @staticmethod        
    def hb_in_traj(traj, atoms_nums):
        """Only for NHN H-bonds! traj - obj XYZTrajectory, atoms_nums = [atom-donor, H, axceptor HB]. Return list nums of structures in XYZTrajectory with HB."""
        steps = traj.steps
        steps_with_HB = []
        for ind, step in enumerate(steps):
            if HB_Analyzer.hb_in_structure(step, atoms_nums=atoms_nums):
                steps_with_HB.append(ind)
            
        return steps_with_HB