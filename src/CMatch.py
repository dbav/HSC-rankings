########################################################################
#%% import block     ###################################################
########################################################################
from datetime import date, MINYEAR, timedelta
from CPlayerlist import Playerlist
from CPlayer import Player
########################################################################
#%% match class     ####################################################
########################################################################
class Match:
  """
  The Match class
  Attributes:
    date
    sideA
    sideB
    type
    baxA
    baxB
    pbrA
    pbrB
    games
    winner
    score_difference
  Methods:
    __init__
  """
  def __init__(self, sideA, sideB, type, games, date=date.today()-timedelta(days=2)): # use if matches from yesterday (or even earlier) are to be entered
  #def __init__(self, sideA, sideB, type, games, date=date.today()): # use if matches from today are to be entered
      self.date             = "{0:4d}-{1:2d}-{2:2d}".format(date.year, date.month, date.day)
      self.sideA            = sideA
      self.sideB            = sideB
      playersA              = [Player.load(i) for i in self.sideA]
      playersB              = [Player.load(i) for i in self.sideB]
      self.type             = type
      if ("mixed" in self.type.lower()):        
        self.baxA             = float(sum([i.bax_m for i in playersA]))/float(len(playersA))
        self.baxB             = float(sum([i.bax_m for i in playersB]))/float(len(playersB))
        self.pbrA             = float(sum([i.pbr_m for i in playersA]))/float(len(playersA))
        self.pbrB             = float(sum([i.pbr_m for i in playersB]))/float(len(playersB))
      elif ("doubles" in self.type.lower()):
        self.baxA             = float(sum([i.bax_d for i in playersA]))/float(len(playersA))
        self.baxB             = float(sum([i.bax_d for i in playersB]))/float(len(playersB))
        self.pbrA             = float(sum([i.pbr_d for i in playersA]))/float(len(playersA))
        self.pbrB             = float(sum([i.pbr_d for i in playersB]))/float(len(playersB))      
      elif ("singles" in self.type.lower()):
        self.baxA             = float(sum([i.bax_s for i in playersA]))/float(len(playersA))
        self.baxB             = float(sum([i.bax_s for i in playersB]))/float(len(playersB))
        self.pbrA             = float(sum([i.pbr_s for i in playersA]))/float(len(playersA))
        self.pbrB             = float(sum([i.pbr_s for i in playersB]))/float(len(playersB))
      elif ("undefined" in self.type.lower()):
        self.baxA             = float(sum([i.bax_u for i in playersA]))/float(len(playersA))
        self.baxB             = float(sum([i.bax_u for i in playersB]))/float(len(playersB))
        self.pbrA             = float(sum([i.pbr_u for i in playersA]))/float(len(playersA))
        self.pbrB             = float(sum([i.pbr_u for i in playersB]))/float(len(playersB))
      else:
        raise ValueError("ERROR: Unknown match type '{0:s}' enountered in match initialization")
      self.games            = games
      winstr                = ""
      for i in games:
        if i[0] > i[1]:
          winstr += "A"
        else:
          winstr += "B"
      self.winner           = self.sideA if (winstr.count("A") > winstr.count("B")) else self.sideB
      self.score_difference = float(sum([i[0]-i[1] for i in games]))/float(len(games))
