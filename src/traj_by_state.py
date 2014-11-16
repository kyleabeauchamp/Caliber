import mdtraj as md
import mdtraj.io

ass = md.io.loadh("./Data/Assignments.Fixed.h5")["arr_0"]

# Get assignment data for first trajectory:
a = ass[0]
n_states = a.max() + 1

traj = md.load("./Trajectories/trj0.h5")

traj_chunks = [traj[a == i] for i in range(n_states)]

for i, t in enumerate(traj_chunks):
    t.save("./state%d.dcd" % i)
