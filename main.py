from .xyz_trajectory import XYZ_Trajectory
from .hydrogen_bond import Hydrogen_Bond, Hydrogen_Bonds
from .inp_file_generator import Calc_Data_Inp
from .science_plot import Science_Plot
import os
import matplotlib.pyplot as plt
import numpy as np

file_path = '/home/mark/Desktop/VladimirR/Amidines/MLP/amidines.xyz'
file_dir = os.path.dirname(file_path)

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)

steps = Trajectory.steps

h_bonds1_list = []
h_bonds2_list = []

for step in steps:
    h_bonds1_list.append(Hydrogen_Bond([step.atoms[1], step.atoms[8], step.atoms[10]]))
    h_bonds2_list.append(Hydrogen_Bond([step.atoms[7], step.atoms[13], step.atoms[12]]))

clvs1 = []
clvs2 = []

clvs2_1 = []
clvs2_2 = []

for i in range(20000, 70000):
    clvs1.append(h_bonds1_list[i].colvar)
    clvs2.append(h_bonds2_list[i].colvar)
    clvs2_1.append(h_bonds1_list[i].colvar2)
    clvs2_2.append(h_bonds2_list[i].colvar2)

#q1_1 = np.array(clvs1)
#q1_2 = np.array(clvs2)
#q2_1 = np.array(clvs2_1)
#q2_2 = np.array(clvs2_2)
        
#plt.xlabel('q1_2, Å', fontsize=int(14))
#plt.ylabel('q2_2, Å', fontsize=int(14))
#plt.scatter(q1_2, q2_2, s = 1)

#a, b = np.polyfit(q1_1, q2_1, 1)
#y_trend = a*x + b
#equation = f'y = {round(a, 2)}x + {round(b, 2)}'
#plt.text(0.5, 0.9, equation, fontsize=14, transform=plt.gca().transAxes)
#plt.plot(x, y_trend, color = 'red')

#plt.show()

clvneg = [x for x in clvs1 if x < -0.3]
clvpos = [x for x in clvs1 if x > 0.3]
clvmean = [x for x in clvs1 if x < 0.3 and x > -0.3]

print(len(clvneg))
print(len(clvpos))
print(len(clvmean))

#plt.xlabel('t, фс')
#plt.ylabel('q1, Å')
#plt.plot(range(1000000, 3500000, 50), clvs1, lw = 0.8)
#plt.show()