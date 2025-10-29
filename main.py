import math

import numpy as np

from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import Hydrogen_Bond, Colvars_Lists
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

culv_list = Colvars_Lists(np.array([q1, q2]))
dispersion = culv_list.dispersion
new_culv = culv_list.colvar_transform(np.array([[1, 1], [1, -1]]))
new_dispersion = new_culv.dispersion

#Science_Plot.plt_clv_clv(culv_list, title='Amidines', x_label='y', y_label='x')
#Science_Plot.plt_clv_clv(new_culv, title='Amidines', x_label='x+y', y_label='x-y')

print(dispersion)

print(new_dispersion)
print(math.log10(new_dispersion[0]/new_dispersion[1]))