import random

from .atom import Atom
from .molecule import Molecule

class XYZ_Trajectory:
    """Class XYZ_Trajectory
    
    Parameters:
    steps : list
    List of objects Molecul. One step - one molecule.
    """

    def __init__(self, steps):
        self.__steps = steps
        self.__steps_number = len(steps)

    @property
    def steps(self):
        """Return list of objs Molecule"""
        return self.__steps

    @property
    def steps_number(self):
        """Return int"""
        return self.__steps_number
    
    def random_steps(self, final_steps_number):
        """Return XYZ_Trajectory obj with random n steps from old XYZ_Trajectory obj"""
        steps = self.steps
        steps_number = self.steps_number
        random_ind_list = []
        new_steps = []
        for i in range(final_steps_number):
            selected_step = random.randint(0, steps_number)
            while selected_step in random_ind_list:
                selected_step = random.randint(0, steps_number)
            random_ind_list.append(selected_step)
            new_steps.append(steps[selected_step])
        return XYZ_Trajectory(steps=new_steps)

    @staticmethod
    def xyz_traj_extr_from_xyz(file_path):
        """Reading .xyz file with MD trajectory and return obj Trajectory"""
        file = open(file_path)
        data = file.readlines()
        steps = []

        if len(data[0].split()) == 1 and 'time' in data[1]:
            num_atoms = int(data[0])
            steps_num = int(len(data)/(num_atoms+2))
            
            for i in range(steps_num):
                atoms = []
                for j in range(num_atoms):
                    atom_name = str(data[i*(2+num_atoms)+2+j].replace(',', '.').split()[0])
                    coords = [float(data[i*(2+num_atoms)+2+j].replace(',', '.').split()[1]),
                            float(data[i*(2+num_atoms)+2+j].split()[2]),
                            float(data[i*(2+num_atoms)+2+j].split()[3])
                            ]
                    atoms.append(Atom(atom_name=atom_name, coords=coords))
                steps.append(Molecule(atoms=atoms))

        return XYZ_Trajectory(steps=steps)