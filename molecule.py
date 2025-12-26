import numpy as np

class Molecule:
    """Class Molecule.
    
    Parameters:
    atoms : list
    """

    def __init__(self, atoms):
        self.__atoms = atoms
    
    @property
    def atoms_num(self):
        return len(self.__atoms)

    @property
    def atoms(self):
        return self.__atoms
    

class Dist_Matrix:
    """Class Dist_Matrix

    Parameters:
    dist_matrix : np_array(dists(obj Atom[i] of obj Molecule, obj Atom[j] of obj Molecule))
    """

    def __init__(self, molecule):

        dists = []
        atoms = molecule.atoms
        atoms_num = molecule.atoms_num
        for i, atom in enumerate(atoms):
            dists_from_i_atom = []
            for j in range(0, i+1):
                dists_from_i_atom.append(dists[j][i])
            for j in range(i+1, atoms_num):
                dists_from_i_atom.append(atom.distance(atoms[j]))

        self.__dist_matrix = np.array(dists)
        
    @property
    def dist_matrix(self):
        return self.__dist_matrix