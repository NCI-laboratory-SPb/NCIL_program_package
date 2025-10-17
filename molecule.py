class Molecule:
    """Class Molecule.
    
    Parameters:
    atoms : list
    """

    def __init__(self, atoms):
        self.__atoms = atoms
    
    @property
    def atoms(self):
        return self.__atoms