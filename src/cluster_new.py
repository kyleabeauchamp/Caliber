import msmbuilder.cluster, msmbuilder.msm, msmbuilder.example_datasets, msmbuilder.lumping, msmbuilder.utils
from sklearn.pipeline import make_pipeline
import mdtraj as md

n_micro = 750

#trajectories = [md.load("./trajectory%d.xtc" % i, top="./protein.pdb") for i in [1, 2]]
#trajectories = msmbuilder.example_datasets.fetch_2f4k()["trajectories"]
trajectories = msmbuilder.example_datasets.fetch_bpti()["trajectories"]

clusterer = msmbuilder.cluster.MiniBatchKMedoids(n_clusters=n_micro, metric="rmsd", batch_size=1000)
clusterer.fit(trajectories)
assignments = clusterer.predict(trajectories)

n_macro = 4

micromsm = msmbuilder.msm.MarkovStateModel(n_timescales=n_macro + 1)
lumper = msmbuilder.lumping.PCCAPlus(n_macro)
macromsm = msmbuilder.msm.MarkovStateModel(n_timescales=n_macro)

pipeline = make_pipeline(micromsm, lumper, macromsm)
macro_assignments = pipeline.fit_transform(assignments)

macromsm.transmat_
