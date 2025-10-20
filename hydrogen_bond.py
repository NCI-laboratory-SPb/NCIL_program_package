import numpy as np

from atom import Atom

class Hydrogen_Bond:
    """Class Hydrogen_Bond.
    
    Parameters:
    atoms : list
    List of objects Atom: [Atom-donor, Atom-Hydrogen, Atom-Axceptor]. Sequence is important for calculation coolvar. 
    """

    def __init__(self, atoms):
        self.__atoms = atoms
    
    @property
    def atoms(self):
        """Return list of atoms"""
        return self.__atoms

    @property
    def colvar(self):
        """Return float colvar (dist2-dist1)/2"""
        atoms = self.atoms
        hydrogen = atoms[1]
        donor = atoms[0]
        axceptor = atoms[2]
        colvar = (hydrogen.distance(axceptor)-hydrogen.distance(donor))/2
        return colvar
    
    @staticmethod
    def colvar(donor, hydrogen, axceptor):
        """Input 3 Atom objects and return colvar"""
        colvar = (hydrogen.distance(axceptor)-hydrogen.distance(donor))/2
        return colvar
    

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
    def colvars_lists(self):
        colvars_lists = []
        h_bonds = self.h_bonds
        for i in h_bonds:
            colvars_lists.append(i.colvar)
        return Colvars_Lists(colvars_lists)


class Colvars_Lists:
    """Class Colvars.
    
    Parameters:
    colvars_lsts : np.array
    Arrey, when row - list of colvar.
    """

    def __init__(self, colvars_lsts):
        self.__colvars_lsts  = colvars_lsts
    
    @property
    def colvars_lsts(self):
        return self.__colvars_lsts

    def colvar_transform(self, translation_matrix):
        """Translation_matrix - np.arrey. Translate colvars and retrun new np.arrey of colvars"""
        new_lst = ((self.colvars_lsts.T)@translation_matrix).T
        return Colvars_Lists(new_lst)