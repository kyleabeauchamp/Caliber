# Commands for MSMBuilder2-based pipeline for ward clustering

ln -s protein.pdb native.pdb
RebuildProject -c native.pdb
CreateAtomIndices -a minimal -s native.pdb
cd ..

mkdir hp3510ns
cd hp3510ns
ln -s ../hp35/* ./
rm Trajectories
rm ProjectInfo.yaml

ipython
"""
import mdtraj as md
t = md.load("../hp35/Trajectories/trj0.h5", stride=10)
t.save("./Trajectories/trj0.h5")
"""


RebuildProject -c native.pdb

# Work on 10ns subsampled dataset for now, uses less memory.
# For BPTI, will do full dataset, but note this uses LOTS of memory.
Cluster rmsd hierarchical
AssignHierarchical -s 1 -n 10

# Build transition matrix, do ergodic trimming etc.
BuildMSM -l 1

#Output some structures for visualization.
SaveStructures -c 3 -S sep -f pdb

pymol PDBs/*.pdb
# Should see state8 with 25% population as native state
