import math

import numpy as np

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

    @staticmethod
    def angle(atom1, atom2, atom3):
        """Return float angle in degrees between atoms atom1-atom2-atom3"""
        a1_coords = np.array(atom1.coords)
        a2_coords = np.array(atom2.coords)
        a3_coords = np.array(atom3.coords)
        dist_vect_a2_a1 = a1_coords - a2_coords
        dist_vect_a2_a3 = a3_coords - a2_coords
        angle_cos = np.dot(dist_vect_a2_a1, dist_vect_a2_a3)/(np.linalg.norm(dist_vect_a2_a3)*np.linalg.norm(dist_vect_a2_a1))
        angle_rad = np.arccos(angle_cos)
        return angle_rad/math.pi*180
    
    @staticmethod
    def torsion_angle(atom1, atom2, atom3, atom4):
        """Return float torsion angle atom1-atom2-atom3-atom4"""
        a1_coords = np.array(atom1.coords)
        a2_coords = np.array(atom2.coords)
        a3_coords = np.array(atom3.coords)
        a4_coords = np.array(atom4.coords)
        r1 = a2_coords - a1_coords
        r2 = a3_coords - a2_coords
        r3 = a4_coords - a3_coords
        n1 = np.cross(r1, r2)
        n2 = np.cross(r2, r3)
        x = np.dot(n1, n2)
        y = np.dot(r2/np.linalg.norm(r2), np.cross(n1, n2))
        tors_angle = np.arctan2(y, x)
        return tors_angle/math.pi*180