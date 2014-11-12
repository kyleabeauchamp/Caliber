import mdtraj as md

# Use VMD to save 2F4K-0-protein.mae as protein.pdb 
filename = "/home/kyleb/dat/ShawScience/TarBalls/DESRES-Trajectory_2F4K-0-protein/2F4K-0-protein/2F4K-0-protein-%.3d.dcd"
traj = md.load([filename % i for i in range(62)], top="protein.pdb", stride=5)

traj.save("./Trajectories/trj0.dcd")
