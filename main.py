import math

import numpy as np

from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import Hydrogen_Bond, Colvars_Lists
from science_plot import Science_Plot

#file_path = '/home/mark/Desktop/VladimirR/Amidines_Mark/Amidines_mtd-pos-1.xyz'
file_path = '/home/mark/Desktop/VladimirR/Amidines_Mark/ADAD-DADA_mtd-pos-1.xyz'
#file_path = '/home/mark/Desktop/VladimirR/Amidines_Mark/ADDA-DAAD_mtd-pos-1.xyz'

q1 = []
q2 = []
q3 = []
q4 = []

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)
steps = Trajectory.steps
for step in steps:
    step_atoms = step.atoms
#    q1.append(Hydrogen_Bond.colvar(step_atoms[9], step_atoms[8], step_atoms[10]))
#    q2.append(Hydrogen_Bond.colvar(step_atoms[4], step_atoms[3], step_atoms[12]))
    q1.append(Hydrogen_Bond.colvar(step_atoms[15], step_atoms[11], step_atoms[28]))
    q2.append(Hydrogen_Bond.colvar(step_atoms[35], step_atoms[35], step_atoms[14]))
    q3.append(Hydrogen_Bond.colvar(step_atoms[34], step_atoms[33], step_atoms[29]))
    q4.append(Hydrogen_Bond.colvar(step_atoms[30], step_atoms[26], step_atoms[13]))
#   q1.append(Hydrogen_Bond.colvar(step_atoms[36], step_atoms[34], step_atoms[15]))
#   q2.append(Hydrogen_Bond.colvar(step_atoms[14], step_atoms[10], step_atoms[24]))
#   q3.append(Hydrogen_Bond.colvar(step_atoms[33], step_atoms[32], step_atoms[28]))
#   q4.append(Hydrogen_Bond.colvar(step_atoms[29], step_atoms[26], step_atoms[13]))

culv_list = Colvars_Lists(np.array([q1, q2, q3, q4]))
dispersion = culv_list.dispersion
#new_culv = culv_list.colvar_transform(np.array([[1, 1], [1, -1]]))
#new_dispersion = new_culv.dispersion

Science_Plot.plt_clv_clv(culv_list, title='ADAD-DADA_MetaD', colvar1_num=0, colvar2_num=1)
Science_Plot.plt_clv_clv(culv_list, title='ADAD-DADA_MetaD', colvar1_num=0, colvar2_num=2)
Science_Plot.plt_clv_clv(culv_list, title='ADAD-DADA_MetaD', colvar1_num=0, colvar2_num=3)
Science_Plot.plt_clv_clv(culv_list, title='ADAD-DADA_MetaD', colvar1_num=1, colvar2_num=2)
Science_Plot.plt_clv_clv(culv_list, title='ADAD-DADA_MetaD', colvar1_num=1, colvar2_num=3)
Science_Plot.plt_clv_clv(culv_list, title='ADAD-DADA_MetaD', colvar1_num=2, colvar2_num=3)
#Science_Plot.plt_clv_clv(new_culv, title='Amidines', x_label='x+y', y_label='x-y')

#print(dispersion)

#print(new_dispersion)
#print(math.log10(new_dispersion[0]/new_dispersion[1]))