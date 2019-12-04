########################################################################
#%% import block     ###################################################
########################################################################
from json import load, dump
from MPaths import playerlistpath
########################################################################
#%% playerlist class     ###############################################
########################################################################
class Playerlist:
  """
  The Playerlist class
  Attributes:
    playerdict    (dictionary id   -> name)
    invplayerdict (dictionary name -> id  )
    names
    ids
  Methods:
    __init__
    update
    get_name
    get_id
    add_player
    save
  """
  def __init__(self):
    with open(playerlistpath,"r") as i:
        self.playerdict = load(i)
    self.invplayerdict  = { v : k for k, v in self.playerdict.items() }
    self.names = list(self.playerdict.values())
    self.ids   = list(self.playerdict.keys())
  def update(self):
    self.invplayerdict  = { v : k for k, v in self.playerdict.items() }
    self.names = self.playerdict.values()
    self.ids   = self.playerdict.keys()    
  def get_name(self,id):
    if ( id in self.ids ):
      return(self.playerdict[id])
    else:
      return(None)
  def get_id(self,name):
    if ( name in self.names ):
      return(self.invplayerdict[name])
    else:
      return(None)
  def add_player(self, id, name):
    if not (id in self.ids) and not (name in self.names):
      self.playerdict[id] = name
      self.update()
      self.save()
    else:
      raise ValueError("Player {:s} (id = {:s}) already exists.".format(name, id))
  def save(self):
    with open(playerlistpath, "w") as i:
      dump(self.playerdict, i, sort_keys=True, indent=4)
