########################################################################
#%% import block     ###################################################
########################################################################
from os.path import dirname, abspath, join
########################################################################
#%% set paths to files     #############################################
########################################################################
repodir = dirname(dirname(abspath(__file__)))
datadir = join(repodir, "data")
playerlistpath = join(datadir, "players.json")
playerdir      = join(datadir, "players")
readmemdpath   = join(repodir, "README.md")
readmepath     = join(repodir, "readme")
