########################################################################
#%% import block     ###################################################
########################################################################
from os.path import exists, join
from MPaths import repodir, datadir, playerlistpath, playerdir, readmemdpath, readmepath
from CPlayerlist import Playerlist
########################################################################
#%% check if directories and files exist     ###########################
########################################################################
def init():
  if ( not exists(repodir) ):
    raise NameError("Directory '{0:s}' not found.".format(repodir))
  if ( not exists(datadir) ):
    raise NameError("Directory '{0:s}' not found.".format(datadir))
  if ( exists(playerlistpath) ):
    playerlist = Playerlist()
    for i in playerlist.ids:
      playerpath = join(playerdir,i)
      if ( not exists(playerpath) ):
        raise NameError("File '{0:s}' not found.".format(playerpath))
  else:
    raise NameError("File '{0:s}' not found.".format(playerlistpath))
  if ( not exists(readmemdpath) ):
    raise NameError("File '{0:s}' not found.".format(repodir))
  if ( not exists(readmepath) ):
    raise NameError("File '{0:s}' not found.".format(repodir))
