from molecule import Molecule
from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import Hydrogen_Bond
from science_plot import Science_Plot

file_path = '/home/mark/Desktop/VladimirR/Amidines_Mark/Amidines_mtd-pos-1.xyz'
q1 = []
q2 = []

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)
steps = Trajectory.steps
for step in steps:
    step_atoms = step.atoms
    q1.append(Hydrogen_Bond.colvar(step_atoms[9], step_atoms[8], step_atoms[10]))
    q2.append(Hydrogen_Bond.colvar(step_atoms[4], step_atoms[3], step_atoms[12]))

Science_Plot.plt_clv_clv(q1, q2)