import random

import matplotlib.pyplot as plt

from .atom import Atom
from .molecule import Molecule

class XYZ_Trajectory:
    """Class XYZ_Trajectory
    
    Parameters:
    steps : list
    List of objects Molecul. One step - one molecule.
    
    """

    def __init__(self, steps, cell=None):
        self.__steps = steps
        self.__steps_number = len(steps)
        self.__cell = cell

    def __add__(self, other):
        if type(other)==XYZ_Trajectory:
            new_steps = []
            new_steps.extend(self.steps)
            for step in other.steps:
                new_steps.append(step)
            return XYZ_Trajectory(steps=new_steps, cell=self.cell)
        else:
            raise ArithmeticError("The type of the object being added must be \"XYZ_Trajectory\".")
        
    def __check_step_indx(self, indx):
        if type(indx)!=int:
            raise IndexError("The step index must be an integer.")
        steps_num = self.steps_number
        if indx<-steps_num or indx>=steps_num:
            raise IndexError("The step index is out of range.")

    def __getitem__(self, indx):
        self.__check_step_indx(indx)
        return self.steps[indx]
    
    def __setitem__(self, indx, step):
        self.__check_step_indx(indx)
        if type(step)!=Molecule:
            raise TypeError("The new step must be of type Molecule.")
        self.__steps[indx] = step

    @property
    def steps(self):
        """Return list of objs Molecule"""
        return self.__steps

    @property
    def steps_number(self):
        """Return int"""
        return self.__steps_number
    
    @property
    def cell(self):
        """Return list of floats"""
        return self.__cell
    
    @cell.setter
    def cell(self, cell):
        if type(cell) == list and len(cell) == 3 and all(type(x) in [int, float] for x in cell):
            for step in self.steps:
                step.cell = cell
            self.__cell = cell

    def copy(self):
        return XYZ_Trajectory(steps=self.steps, cell=self.cell)

    def static_center_of_mass(self):
        """Return obj XYZTrajectory with steps, which center of mass is zero."""
        steps = self.steps
        new_steps = []
        for step in steps:
            atoms = step.atoms
            center_of_mass = step.center_of_mass
            new_atoms = []
            for atom in atoms:
                new_coords = [atom.coords[0] - center_of_mass[0], atom.coords[1] - center_of_mass[1], atom.coords[2] - center_of_mass[2]]
                new_atoms.append(Atom(atom_name=atom.atom_name, coords=new_coords, atom_mass=atom.mass))
            new_steps.append(Molecule(atoms=new_atoms))
        return XYZ_Trajectory(steps=new_steps, cell=self.cell)
    
    def cut_traj(self, start_step_num, final_step_num):
        """Return XYZ_Trajectory obj with steps from start_step_num to final_step_num from old XYZ_Trajectory obj."""
        steps = self.steps
        new_steps = []
        for i in range(start_step_num, final_step_num+1):
            new_steps.append(steps[i])
        return XYZ_Trajectory(steps=new_steps, cell=self.cell)

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
        return XYZ_Trajectory(steps=new_steps, cell=self.cell)
    
    def sum_traj(self, trajs):
        """Return XYZ_Trajectory obj with steps from old XYZ_Trajectory obj and trajs list."""
        new_traj = self.copy()
        for traj in trajs:
            new_traj+=traj
        return new_traj
    
    def subsystem_traj(self, atom_num_list):
        """Return XYZ_Trajectory obj with steps with atoms from atom_num_list."""
        steps = self.steps
        new_steps = []
        for step in steps:
            new_atoms = []
            for atom_num in atom_num_list:
                new_atoms.append(step.atoms[atom_num])
            new_steps.append(Molecule(atoms=new_atoms))
        return XYZ_Trajectory(steps=new_steps, cell=self.cell)

    @staticmethod
    def extr_from_xyz(file_name):
        """Reading .xyz file with MD trajectory and return obj Trajectory"""
        with open(file_name, "r", encoding="utf-8") as file:
            data = file.readlines()
        steps = []

        if len(data[0].split()) == 1 and 'time' in data[1].lower() or 'generated' in data[1].lower():
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

        elif len(data[1].split()) == 2 and 'converged=true' in data[1].lower():
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

        elif "Coordinates from ORCA" in data[1]:
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
        
        else:
            raise ValueError(f"Unrecognized XYZ comment-line format in {file_name}")

        return XYZ_Trajectory(steps=steps)

    def dist_list(self, atom1_num, atom2_num, start_step_num = None, final_step_num = None):
        """Create list of floats distances between atom1 and atom2 and return list of foat distances."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number
        steps = self.steps[start_step_num:final_step_num+1]

        dist_list = []

        if self.cell == None:
            for step in steps:
                step_atoms = step.atoms
                dist_list.append(step_atoms[atom1_num].dist(step_atoms[atom2_num]))
        else:
            for step in steps:
                step_atoms = step.atoms
                dist_list.append(step_atoms[atom1_num].dist(step_atoms[atom2_num], cell=self.cell))
        return dist_list
    
    def dist_plot(self, atom1_num, atom2_num, start_step_num=None, final_step_num=None, title=None, x_label="Steps", y_label=None, 
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
    
    def center_of_mass_list(self, start_step_num = None, final_step_num = None):
        """Create list of tuples with center of mass coords and return list of tuples with center of mass coords."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number
        steps = self.steps[start_step_num:final_step_num+1]

        center_of_mass_list = []
        for step in steps:
            center_of_mass_list.append(step.center_of_mass)
        return center_of_mass_list
    
    @staticmethod
    def periodic_boundary_conditions_traj(traj, cell):
        """Return XYZ_Trajectory obj with steps with atoms coords in cell."""
        steps = traj.steps
        new_steps = []
        for step in steps:
            new_atoms = []
            for atom in step.atoms:
                coords = atom.coords
                new_coords = [coords[0] % cell[0], coords[1] % cell[1], coords[2] % cell[2]]
                new_atoms.append(Atom(atom_name=atom.atom_name, coords=new_coords, atom_mass=atom.mass))
            atom1_coords = new_atoms[0].coords
            for atom in new_atoms [1:]:
                atom_coords = atom.coords
                for i in range(3):
                    if abs(atom_coords[i] - atom1_coords[i]) > cell[i]/2:
                        if atom_coords[i] > atom1_coords[i]:
                            atom_coords[i] -= cell[i]
                        else:
                            atom_coords[i] += cell[i]
            new_steps.append(Molecule(atoms=new_atoms))
        return XYZ_Trajectory(steps=new_steps, cell=cell)
    
    def save(self, start_step_num = None, final_step_num = None, file_name = None):
        """Save steps [start_step_num, final_step_num] (inclusive) to an .xyz file.
        Return the number of steps written."""
        if start_step_num == None:
            start_step_num = 0
        if final_step_num == None:
            final_step_num = self.steps_number - 1
        if not (0 <= start_step_num <= final_step_num < self.steps_number):
            raise ValueError(
                f"Invalid step range [{start_step_num}, {final_step_num}]"
                f"for a trajectory of {self.steps_number} steps."
            )

        steps = self.steps
        n_atoms_in_mol = len(steps[0].atoms)
        new_lines = []
        for step in steps[start_step_num: final_step_num+1]:
            new_lines.append(f"{n_atoms_in_mol}\n")
            new_lines.append("Generated by NCIL_program_package\n")
            for atom in step.atoms:
                coords = "    ".join(str(x) for x in atom.coords)
                new_lines.append(f"{atom.atom_name}    {coords}\n")

        if file_name is None:
            file_name = f"trajectory_{start_step_num}_{final_step_num}.xyz"

        with open(file_name, "w", encoding="utf-8") as xyz_traj_file:
            xyz_traj_file.writelines(new_lines)
        
        return final_step_num - start_step_num + 1