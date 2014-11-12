import mixtape.cluster, mixtape.markovstatemodel
import mdtraj as md

trajectories = [md.load("./Trajectories/trj0.dcd", top="./protein.pdb")]

clusterer = mixtape.cluster.RegularSpatial(d_min=1.0, metric=md.rmsd)
clusterer.fit(trajectories)

assignments = clusterer.predict(trajectories)

msm = mixtape.markovstatemodel.MarkovStateModel()
msm.fit(assignments)

