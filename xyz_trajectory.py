import random

import matplotlib.pyplot as plt

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

        if len(data[0].split()) == 1 and 'time' in data[1] or 'generated' in data[1]:
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
    
    def dist_list(self, atom1_num, atom2_num, start_step_num = None, final_step_num = None):
        """Create list of floats distances between atom1 and atom2 and return list of foat distances."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number
        steps = self.steps[start_step_num:final_step_num+1]

        dist_list = []
        for step in steps:
            step_atoms = step.atoms
            dist_list.append(step_atoms[atom1_num].distance(step_atoms[atom2_num]))
        return dist_list
    
    def dist_plot(self, atom1_num, atom2_num, start_step_num=None, final_step_num=None, title=None, x_label="Steps", y_label="Corner, °", 
                    font_size=14):
        """Creates plot of distances betweem two atoms and return None."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number

        if title == None:
            title = f"Distance_{atom1_num}_{atom2_num}"
        if y_label == None:
            y_label = f"Distance_{atom1_num}_{atom2_num}, Å"
        
        x = range(start_step_num, final_step_num)
        dist_list = self.dist_list(atom1_num, atom2_num, start_step_num=start_step_num, final_step_num=final_step_num)
        
        plt.title(title, fontsize=int(font_size))
        plt.xlabel(xlabel=x_label, fontsize=int(font_size))
        plt.ylabel(ylabel=y_label, fontsize=int(font_size))
        plt.scatter(x, dist_list, s = 1)
        plt.show()

        return None
    
    def angle_list(self, atom1_num, atom2_num, atom3_num, start_step_num = None, final_step_num = None):
        """Create list of floats corners and return list of foat corners."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number
        steps = self.steps[start_step_num:final_step_num+1]

        angle_list = []
        for step in steps:
            step_atoms = step.atoms
            angle_list.append(Atom.angle(step_atoms[atom1_num], step_atoms[atom2_num], step_atoms[atom3_num]))
        return angle_list
    
    def angle_plot(self, atom1_num, atom2_num, atom3_num, start_step_num=None, final_step_num=None, title=None, x_label="Steps", y_label=None, 
                    font_size=14):
        """Creates plot of angle and return None."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number

        if title == None:
            title = f"Angle{atom1_num}_{atom2_num}_{atom3_num}"
        if y_label == None:
            y_label = f"Angle{atom1_num}_{atom2_num}_{atom3_num}, °"
        
        x = range(start_step_num, final_step_num)
        angle_list = self.angle_list(atom1_num, atom2_num, atom3_num, start_step_num=start_step_num, final_step_num=final_step_num)
        
        plt.title(title, fontsize=int(font_size))
        plt.xlabel(xlabel=x_label, fontsize=int(font_size))
        plt.ylabel(ylabel=y_label, fontsize=int(font_size))
        plt.scatter(x, angle_list, s = 1)
        plt.show()

        return None
    
    def torsion_angle_list(self, atom1_num, atom2_num, atom3_num, atom4_num, start_step_num = None, final_step_num = None):
        """Create list of floats torsion angles and return list of foat torsion angles."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number
        steps = self.steps[start_step_num:final_step_num+1]

        torsion_angle_list = []
        for step in steps:
            step_atoms = step.atoms
            torsion_angle_list.append(Atom.torsion_angle(step_atoms[atom1_num], step_atoms[atom2_num], step_atoms[atom3_num], step_atoms[atom4_num]))
        return torsion_angle_list
    
    def torsion_angle_plot(self, atom1_num, atom2_num, atom3_num, atom4_num, start_step_num=None, final_step_num=None, title=None, x_label="Steps", 
                            y_label=None, font_size=14):
        """Creates plot of torsion angle and return None."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number

        if title == None:
            title = f"Torsion angle {atom1_num}_{atom2_num}_{atom3_num}_{atom4_num}"
        if y_label == None:
            y_label = f"Torsion angle {atom1_num}_{atom2_num}_{atom3_num}_{atom4_num}, °"
        
        x = range(start_step_num, final_step_num)
        torsion_corner_list = self.torsion_angle_list(atom1_num, atom2_num, atom3_num, atom4_num, start_step_num=start_step_num, final_step_num=final_step_num)
        
        plt.title(title, fontsize=int(font_size))
        plt.xlabel(xlabel=x_label, fontsize=int(font_size))
        plt.ylabel(ylabel=y_label, fontsize=int(font_size))
        plt.scatter(x, torsion_corner_list, s = 1)
        plt.show()

        return None
    
    def save(self, start_step_num = None, final_step_num = None, file_name = None):
        """Saving XYZ_Trajectory in .xyz file. Return Integer number of steps in saved trajectory."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number
        else:
            final_step_num+=1
        steps = self.steps
        n_atoms_in_mol = len(steps[0])
        new_lines = []
        for step in steps[start_step_num: final_step_num]:
            new_lines.append(f"{str(n_atoms_in_mol)}\n")
            new_lines.append("Generated by NCIL_program_package\n")
            for atom in step.atoms:
                new_lines.append(f"{atom.atom_name}    {"    ".join(atom.coords)}\n")

        if file_name == None:
            with open(f"trajectory_{start_step_num}_{final_step_num}", "w") as xyz_traj_file:
                xyz_traj_file.writelines(new_lines)

        else:
            with open(file_name, "w") as xyz_traj_file:
                xyz_traj_file.writelines(new_lines)
        
        return int(final_step_num - start_step_num)