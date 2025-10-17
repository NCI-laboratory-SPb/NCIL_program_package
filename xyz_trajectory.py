import os

from atom import Atom
from molecule import Molecule

class XYZ_Trajectory:
    """Class XYZ_Trajectory
    
    Parameters:
    steps : list
    List of objects Molecul. One step - one molecule.
    """

    def __init__(self, steps):
        self.__steps = steps

    @property
    def steps(self):
        return self.__steps

    @staticmethod
    def xyz_traj_extr_from_xyz(file_path):
        file = open(file_path)
        data = file.readlines()
        steps = []

        if len(data[0].split()) == 1 and 'time' in data[1]:
            num_atoms = int(data[0])
            steps_num = int(len(data)/(num_atoms+2))
            
            for i in range(steps_num):
                atoms = []
                for j in range(num_atoms):
                    coords = [float(data[i*(2+num_atoms)+2+j].replace(',', '.').split()[1]),
                            float(data[i*(2+num_atoms)+2+j].split()[2]),
                            float(data[i*(2+num_atoms)+2+j].split()[3])
                            ]
                    atoms.append(Atom(coords))
                steps.append(Molecule(atoms=atoms))

        return XYZ_Trajectory(steps=steps)