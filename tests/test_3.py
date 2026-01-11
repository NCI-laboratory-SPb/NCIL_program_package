import os

import matplotlib.pyplot as plt
import numpy as np

from xyz_trajectory import XYZ_Trajectory

file_path = "E:/SPBU/FQW/Program_review/formimidamide_340000_360000.xyz"
file_dir = os.path.dirname(file_path)

Trajectory = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_path=file_path)

fig, axes = plt.subplots(8, 1, figsize=(10, 20))

data1 = Trajectory.angle_list(10, 4, 13)
axes[0].scatter(range(len(data1)), data1, s=1, alpha=0.6, color='blue')
axes[0].axhline(np.mean(data1), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data1):.2f}°')
axes[0].set_ylabel('∠(NHN)₁, °')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

data2 = Trajectory.angle_list(11, 7, 12)
axes[1].scatter(range(len(data2)), data2, s=1, alpha=0.6, color='green')
axes[1].axhline(np.mean(data2), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data2):.2f}°')
axes[1].set_ylabel('∠(NHN)₂, °')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

data3 = Trajectory.dist_list(10, 4)
axes[2].scatter(range(len(data3)), data3, s=1, alpha=0.6, color='purple')
axes[2].axhline(np.mean(data3), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data3):.3f}Å')
axes[2].set_ylabel('r(NH)₁, Å')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

data4 = Trajectory.dist_list(11, 7)
axes[3].scatter(range(len(data4)), data4, s=1, alpha=0.6, color='orange')
axes[3].axhline(np.mean(data4), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data4):.3f}Å')
axes[3].set_ylabel('r(NH)₂, Å')
axes[3].legend()
axes[3].grid(True, alpha=0.3)

data5 = Trajectory.dist_list(13, 4)
axes[4].scatter(range(len(data5)), data5, s=1, alpha=0.6, color='brown')
axes[4].axhline(np.mean(data5), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data5):.3f}Å')
axes[4].set_ylabel('r(N...H)₁, Å')
axes[4].legend()
axes[4].grid(True, alpha=0.3)

data6 = Trajectory.dist_list(12, 7)
axes[5].scatter(range(len(data6)), data6, s=1, alpha=0.6, color='pink')
axes[5].axhline(np.mean(data6), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data6):.3f}Å')
axes[5].set_ylabel('r(N...H)₂, Å')
axes[5].legend()
axes[5].grid(True, alpha=0.3)

data7 = Trajectory.torsion_angle_list(12, 0, 10, 4)
axes[6].scatter(range(len(data7)), data7, s=1, alpha=0.6, color='teal')
axes[6].axhline(np.mean(data7), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data7):.2f}°')
axes[6].set_ylabel('∠(NCNH)₁, °')
axes[6].legend()
axes[6].grid(True, alpha=0.3)

data8 = Trajectory.torsion_angle_list(13, 1, 11, 7)
axes[7].scatter(range(len(data8)), data8, s=1, alpha=0.6, color='gray')
axes[7].axhline(np.mean(data8), color='red', linestyle='--', alpha=0.7, label=f'Mean: {np.mean(data8):.2f}°')
axes[7].set_ylabel('∠(NCNH)₂, °')
axes[7].set_xlabel('Step number')
axes[7].legend()
axes[7].grid(True, alpha=0.3)

plt.suptitle('Hydrogen Bond Dynamics Analysis', fontsize=14, y=0.99)

plt.tight_layout()

output_file = os.path.join(file_dir, "hydrogen_bond_analysis.png")
plt.savefig(output_file, dpi=600, bbox_inches='tight')
print(f"Graph saved to: {output_file}")

plt.close(fig)

print("\nStatistics:")
print(f"∠(NHN)₁: {np.mean(data1):.2f} ± {np.std(data1):.2f}° (min: {np.min(data1):.2f}, max: {np.max(data1):.2f})")
print(f"∠(NHN)₂: {np.mean(data2):.2f} ± {np.std(data2):.2f}° (min: {np.min(data2):.2f}, max: {np.max(data2):.2f})")
print(f"r(NH)₁: {np.mean(data3):.3f} ± {np.std(data3):.3f}Å (min: {np.min(data3):.3f}, max: {np.max(data3):.3f})")
print(f"r(NH)₂: {np.mean(data4):.3f} ± {np.std(data4):.3f}Å (min: {np.min(data4):.3f}, max: {np.max(data4):.3f})")