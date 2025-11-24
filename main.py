from xyz_trajectory import XYZ_Trajectory

file_path = '/home/mark/Desktop/VladimirR/Hal_bond/Lev/ULTRANasilie-pos-1.xyz'

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)

Trajectory_random_steps = Trajectory.random_steps(35)

