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