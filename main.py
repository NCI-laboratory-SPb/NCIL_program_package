from xyz_trajectory import XYZ_Trajectory
from inp_file_generator import Calc_Data_Inp
import os

file_path = '/home/mark/Desktop/VladimirR/Hal_bond/Lev/ULTRANasilie-pos-1.xyz'
file_dir = os.path.dirname(file_path)

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)

Trajectory_random_steps = Trajectory.random_steps(35)
random_steps = Trajectory_random_steps.steps
paths = []

for i in range(0, 35):
    params = {'molecule' : random_steps[i], 'method' : 'b3lyp', 'basis' : 'def2-TZVPD', 'name' : f'NMR_{i}', 'nmr' : 'giao', 'cores' : 9, 'memory' : 12}
    Calc_Data = Calc_Data_Inp(**params)
    path, _ = Calc_Data.generate_gaussian_inp(path=file_dir, filename=f'NMR_{i}.gjf')
    paths.append(path)

with open(os.path.join(file_dir, 'scrip.sh'), 'w') as file:
    for i in paths:
        file.write()