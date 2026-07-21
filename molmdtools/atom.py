import math

import numpy as np

from .molecule import Molecule
from .elements import ATOM_MASSES

class Atom:
    """Class Atom.
    
    Parameters:
    coords : list
    """

    def __init__(self, atom_name='X', coords=None, atom_mass=None):
        if coords is None:
            coords = [0.0, 0.0, 0.0]
        else:
            coords = [float(coord) for coord in coords]

        if len(coords) != 3:
            raise ValueError("Coords must be a list of length 3.")

        self.__atom_name = atom_name
        self.__atom_mass = atom_mass
        self.__coords = coords

    def __add__(self, other):
        if type(other)==Atom:
            return Molecule(atoms=[self, other])
        elif type(other)==Molecule:
            mol1_atoms = other.atoms
            atoms = mol1_atoms+[self, ]
            return Molecule(atoms=atoms)
        else:
            raise ArithmeticError("The type of the object being added must be \"Atom\" or \"Molecule.\"")
        
    def __radd__(self, other):
        return self+other
                               
    @property
    def atom_name(self):
        return self.__atom_name
    
    @property
    def mass(self):
        if self.__atom_mass is not None:
            return self.__atom_mass
        elif self.__atom_name in ATOM_MASSES:
            atom_mass = ATOM_MASSES[self.__atom_name]["mass"]
            self.__atom_mass = atom_mass
            return atom_mass
        else:
            raise ValueError("Mass of atom {} is not defined".format(self.__atom_name))

    @mass.setter
    def mass(self, mass):
        if mass > 0 and type(mass) in [int, float]:
            self.__atom_mass = mass

    @property
    def coords(self):
        """Return list of coords"""
        return self.__coords
    
    def dist(self, other, cell=None):
        """Cell - list of float. Return evklid distance between two Atoms"""
        if cell == None:
            other_coords = other.coords
            sum = 0
            for i, axis_val in enumerate(other_coords):
                sum += (axis_val - self.coords[i])**2
            dist = math.sqrt(sum)
            return dist
        else:
            other_coords = other.coords
            sum = 0
            for i, axis_val in enumerate(other_coords):
                dist_axis = abs(axis_val - self.coords[i])
                dist_axis %= cell[i]
                if dist_axis > cell[i]/2:
                    dist_axis = cell[i] - dist_axis
                sum += dist_axis**2
            dist = math.sqrt(sum)
            return dist
    
    @staticmethod
    def angle(atom1, atom2, atom3, cell=None):
        """Return float angle in degrees between atoms atom1-atom2-atom3"""
        a1_coords = np.array(atom1.coords)
        a2_coords = np.array(atom2.coords)
        a3_coords = np.array(atom3.coords)
        if cell == None:
            dist_vect_a2_a1 = a1_coords - a2_coords
            dist_vect_a2_a3 = a3_coords - a2_coords
            angle_cos = np.dot(dist_vect_a2_a1, dist_vect_a2_a3)/(np.linalg.norm(dist_vect_a2_a3)*np.linalg.norm(dist_vect_a2_a1))
            angle_rad = np.arccos(angle_cos)
        else:
            cell = np.array(cell)
            dist_vect_a2_a1 = a1_coords - a2_coords
            dist_vect_a2_a3 = a3_coords - a2_coords
            for i in range(3):
                dist_vect_a2_a1[i] %= cell[i]
                if dist_vect_a2_a1[i] > cell[i]/2:
                    dist_vect_a2_a1[i] -= cell[i]
                dist_vect_a2_a3[i] %= cell[i]
                if dist_vect_a2_a3[i] > cell[i]/2:
                    dist_vect_a2_a3[i] -= cell[i]
            angle_cos = np.dot(dist_vect_a2_a1, dist_vect_a2_a3)/(np.linalg.norm(dist_vect_a2_a3)*np.linalg.norm(dist_vect_a2_a1))
            angle_rad = np.arccos(angle_cos)
        return angle_rad/math.pi*180
    
    @staticmethod
    def torsion_angle(atom1, atom2, atom3, atom4, cell=None):
        """Return float torsion angle atom1-atom2-atom3-atom4"""
        a1_coords = np.array(atom1.coords)
        a2_coords = np.array(atom2.coords)
        a3_coords = np.array(atom3.coords)
        a4_coords = np.array(atom4.coords)
        if cell == None:
            r1 = a2_coords - a1_coords
            r2 = a3_coords - a2_coords
            r3 = a4_coords - a3_coords
        else:
            cell = np.array(cell)
            r1 = a2_coords - a1_coords
            r2 = a3_coords - a2_coords
            r3 = a4_coords - a3_coords
            for i in range(3):
                r1[i] %= cell[i]
                if r1[i] > cell[i]/2:
                    r1[i] -= cell[i]
                r2[i] %= cell[i]
                if r2[i] > cell[i]/2:
                    r2[i] -= cell[i]
                r3[i] %= cell[i]
                if r3[i] > cell[i]/2:
                    r3[i] -= cell[i]
        n1 = np.cross(r1, r2)
        n2 = np.cross(r2, r3)
        x = np.dot(n1, n2)
        y = np.dot(r2/np.linalg.norm(r2), np.cross(n1, n2))
        tors_angle = np.arctan2(y, x)
        return tors_angle/math.pi*180
