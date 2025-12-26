"""
# NCIL Program Package

Package for molecular structure analysis, hydrogen bond calculations,
and molecular dynamics trajectory processing.

## Main features:
- **Loading and processing structures** from PDB/XYZ files
- **Hydrogen bond analysis** in molecular complexes
- **Result visualization** using scientific plots
- **Input file generation** for quantum-chemical calculations

## Quick start:

from NCIL_program_package import Atom, Molecule
from NCIL_program_package import analyze_hydrogen_bonds, plot_analysis

# Create an atom
atom = Atom("H", [0.0, 0.0, 0.0])

# Create a molecule
molecule = Molecule([atom1, atom2, atom3])

# Analyze hydrogen bonds

# Visualize results

#Instalation

#Complete workflow example:
import NCIL_program_package as ncil

# 1. Load structure

# 2. Analyze bonds

# 3. Generate report

# 4. Visualize
"""

version = "0.1.0"
author = "Vladimir"
email = "vladimir.rogachevskij@gmail.com"
licence = ""
url = ""

from .atom import Atom
from .molecule import Molecule
from .xyz_trajectory import XYZ_Trajectory
from .hydrogen_bond import Hydrogen_Bond, Hydrogen_Bonds
from .inp_file_generator import Calc_Data_Inp
from .science_plot import Science_Plot