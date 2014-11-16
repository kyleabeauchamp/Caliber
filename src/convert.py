import mdtraj as md

# First use VMD to save 2F4K-0-protein.mae as protein.pdb 
filename = "/home/kyleb/dat/ShawScience/TarBalls/DESRES-Trajectory_2F4K-0-protein/2F4K-0-protein/2F4K-0-protein-%.3d.dcd"
traj = md.load([filename % i for i in range(62)], top="protein.pdb", stride=5)

traj.save("./Trajectories/trj0.h5")


import mdtraj as md
import numpy as np

# First use VMD to save 2F4K-0-protein.mae as protein.pdb 
filename = "/home/kyleb/dat/ShawScience/TarBalls/DESRES-Trajectory-bpti-100/bpti-100/bpti-100-%.3d.dcd"
trj0 = md.load("system.pdb")
atom_indices = np.arange(892)  # Just protein

traj = md.load([filename % i for i in range(42)], top=trj0, stride=1, atom_indices=atom_indices)
trj0.atom_slice(atom_indices, inplace=True)

traj.center_coordinates()
traj.superpose(trj0)

traj.save("./Trajectories/trj0.h5")


trj0.save("./native.pdb")

traj.save("./out.dcd")
