from xyz_trajectory import XYZ_Trajectory

file_path = "E:/SPBU/FQW/Program_review/formimidamide_340000_360000.xyz"

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)

Trajectory.angle_plot(10, 4, 13, y_label="∠(NHN)₁")
Trajectory.angle_plot(11, 7, 12, y_label="∠(NHN)₂")
Trajectory.dist_plot(10, 4, y_label="r(NH)₁")
Trajectory.dist_plot(11, 7, y_label="r(NH)₂")
Trajectory.dist_plot(13, 4, y_label="r(N...H)₁")
Trajectory.dist_plot(12, 7, y_label="r(N...H)₂")
Trajectory.torsion_angle_plot(12, 0, 10, 4, y_label="∠(NCNH)₁")
Trajectory.torsion_angle_plot(13, 1, 11, 7, y_label="∠(NCNH)₂")