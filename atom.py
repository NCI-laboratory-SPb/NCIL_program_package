import math

class Atom:
    """Class Atom.
    
    Parameters:
    coords : list
    """

    def __init__(self, **params):
        self.__atom_name = params.get('tupe', False)
        self.__coords = params['coords']

    @property
    def atom_name(self):
        return self.__atom_name

    @property
    def cords(self):
        """Retroun list of coords"""
        return self.__coords
    
    def distance(self, other):
        """Return evklid distance between two Atoms"""
        other_coords = other.coords
        sum = 0
        for i, axis_val in enumerate(other_coords):
            sum += (float(axis_val) - float(self.coords[i]))**2
        dist = math.sqrt(sum)
        return dist