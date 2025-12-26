import math

class Atom:
    """Class Atom.
    
    Parameters:
    coords : list
    """

    def __init__(self, atom_name='X', coords=[0.0, 0.0, 0.0]):
        self.__atom_name = atom_name
        self.__coords = coords
                               
    @property
    def atom_name(self):
        return self.__atom_name

    @property
    def coords(self):
        """Return list of coords"""
        return self.__coords
    
    def distance(self, other):
        """Return evklid distance between two Atoms"""
        other_coords = other.coords
        sum = 0
        for i, axis_val in enumerate(other_coords):
            sum += (float(axis_val) - float(self.coords[i]))**2
        dist = math.sqrt(sum)
        return dist