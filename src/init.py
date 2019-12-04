########################################################################
#%% import block     ###################################################
########################################################################
from os.path import exists, join
from MPaths import playerlistpath, playerdir
from CPlayerlist import Playerlist
########################################################################
#%% check if data files exist     ######################################
########################################################################
def init():
  if exists(playerlistpath):
    playerlist = Playerlist()
    for i in playerlist.ids:
      playerpath = join(playerdir,i)
      if not exists(playerpath):
        raise NameError("File '{0:s}' not found.".format(playerpath))
  else:
    raise NameError("File '{0:s}' not found.".format(playerlistpath))
