########################################################################
#%% import block     ###################################################
########################################################################
# uuid for creating unique user ids
from uuid import uuid5, NAMESPACE_DNS
from os.path import join
from json import load, dump
from MPaths import playerdir
from CPlayerlist import Playerlist
########################################################################
#%% player class     ###################################################
########################################################################
class Player:
  """
  The Player class
  Attributes:
    name
    id
    gender
    status                                        # active or inactive
    bax_s                                         # for singles
    bax_d                                         # for doubles
    bax_m                                         # for mixed
    bax_u                                         # for undefined discipline
    bax_s_history
    bax_d_history
    bax_m_history
    bax_u_history
    pbr_s
    pbr_d
    pbr_m
    pbr_u
    pbr_s_history
    pbr_d_history
    pbr_m_history
    pbr_u_history
    matches_s
    matches_d
    matches_m
    matches_u
    matches_s_history
    matches_d_history
    matches_m_history
    matches_u_history
    update_at_s
    update_at_d
    update_at_m
    update_at_u
  Methods:
    __init__
    set_name
    set_id
    set_gender
    set_status
    set_bax_s
    set_bax_d
    set_bax_m
    set_bax_u
    set_bax_s_history
    set_bax_d_history
    set_bax_m_history
    set_bax_u_history
    add_bax_s
    add_bax_d
    add_bax_m
    add_bax_u
    set_pbr_s
    set_pbr_d
    set_pbr_m
    set_pbr_u
    set_pbr_s_history
    set_pbr_d_history
    set_pbr_m_history
    set_pbr_u_history
    add_pbr_s
    add_pbr_d
    add_pbr_m
    add_pbr_u
    set_matches_s
    set_matches_d
    set_matches_m
    set_matches_u
    set_matches_s_history
    set_matches_d_history
    set_matches_m_history
    set_matches_u_history
    reset_matches_s
    reset_matches_d
    reset_matches_m
    reset_matches_u
    add_match_s
    add_match_d
    add_match_m
    add_match_u
    create
    load
    save
    update_pbr
    update_bax
  """
  update_at_s = 1
  update_at_d = 1
  update_at_m = 1
  update_at_u = 1
  def __init__(self):
    self.name              = ""
    self.id                = ""
    self.gender            = ""
    self.status            = "active"
    self.bax_s             = 500.00
    self.bax_d             = 500.00
    self.bax_m             = 500.00
    self.bax_u             = 500.00
    self.bax_s_history     = [500.00]
    self.bax_d_history     = [500.00]
    self.bax_m_history     = [500.00]
    self.bax_u_history     = [500.00]
    self.pbr_s             = 50.00
    self.pbr_d             = 50.00
    self.pbr_m             = 50.00
    self.pbr_u             = 50.00
    self.pbr_s_history     = [50.00]
    self.pbr_d_history     = [50.00]
    self.pbr_m_history     = [50.00]
    self.pbr_u_history     = [50.00]
    self.matches_s         = []
    self.matches_d         = []
    self.matches_m         = []
    self.matches_u         = []
    self.matches_s_history = []
    self.matches_d_history = []
    self.matches_m_history = []
    self.matches_u_history = []
  def set_name(self, name):
    self.name = name
  def set_id(self, id):
    self.id = id
  def set_gender(self, gender):
    self.gender = gender
  def set_status(self, status):
    self.status = status
  def set_bax_s(self, bax):
    self.bax_s = bax
  def set_bax_d(self, bax):
    self.bax_d = bax
  def set_bax_m(self, bax):
    self.bax_m = bax
  def set_bax_u(self, bax):
    self.bax_u = bax
  def set_bax_s_history(self, bax_history):
    self.bax_s_history = bax_history
  def set_bax_d_history(self, bax_history):
    self.bax_d_history = bax_history
  def set_bax_m_history(self, bax_history):
    self.bax_m_history = bax_history
  def set_bax_u_history(self, bax_history):
    self.bax_u_history = bax_history
  def add_bax_s(self, bax):
    self.bax_s_history.append(bax)
  def add_bax_d(self, bax):
    self.bax_d_history.append(bax)
  def add_bax_m(self, bax):
    self.bax_m_history.append(bax)
  def add_bax_u(self, bax):
    self.bax_u_history.append(bax)
  def set_pbr_s(self, pbr):
    self.pbr_s = pbr
  def set_pbr_d(self, pbr):
    self.pbr_d = pbr
  def set_pbr_m(self, pbr):
    self.pbr_m = pbr
  def set_pbr_u(self, pbr):
    self.pbr_u = pbr
  def set_pbr_s_history(self, pbr_history):
    self.pbr_s_history = pbr_history
  def set_pbr_d_history(self, pbr_history):
    self.pbr_d_history = pbr_history
  def set_pbr_m_history(self, pbr_history):
    self.pbr_m_history = pbr_history
  def set_pbr_u_history(self, pbr_history):
    self.pbr_u_history = pbr_history
  def add_pbr_s(self, pbr):
    self.pbr_s_history.append(pbr)
  def add_pbr_d(self, pbr):
    self.pbr_d_history.append(pbr)
  def add_pbr_m(self, pbr):
    self.pbr_m_history.append(pbr)
  def add_pbr_u(self, pbr):
    self.pbr_u_history.append(pbr)
  def set_matches_s(self, matches):
    self.matches_s = matches
  def set_matches_d(self, matches):
    self.matches_d = matches
  def set_matches_m(self, matches):
    self.matches_m = matches
  def set_matches_u(self, matches):
    self.matches_u = matches
  def set_matches_s_history(self, matches_history):
    self.matches_s_history = matches_history
  def set_matches_d_history(self, matches_history):
    self.matches_d_history = matches_history
  def set_matches_m_history(self, matches_history):
    self.matches_m_history = matches_history
  def set_matches_u_history(self, matches_history):
    self.matches_u_history = matches_history
  def reset_matches_s(self):
    self.matches_s = []
  def reset_matches_d(self):
    self.matches_d = []
  def reset_matches_m(self):
    self.matches_m = []
  def reset_matches_u(self):
    self.matches_u = []
  def add_match_s(self, match):
    self.matches_s.append(match)
    self.matches_s_history.append(match)
    if (len(self.matches_s) >= self.update_at_s):
      self.update_bax_s()
      self.update_pbr_s()
      self.reset_matches_s()
    self.save()
  def add_match_d(self, match):
    self.matches_d.append(match)
    self.matches_d_history.append(match)
    if (len(self.matches_d) >= self.update_at_d):
      self.update_bax_d()
      self.update_pbr_d()
      self.reset_matches_d()
    self.save()
  def add_match_m(self, match):
    self.matches_m.append(match)
    self.matches_m_history.append(match)
    if (len(self.matches_m) >= self.update_at_m):
      self.update_bax_m()
      self.update_pbr_m()
      self.reset_matches_m()
    self.save()
  def add_match_u(self, match):
    self.matches_u.append(match)
    self.matches_u_history.append(match)
    if (len(self.matches_u) >= self.update_at_u):
      self.update_bax_u()
      self.update_pbr_u()
      self.reset_matches_u()
    self.save()
  def create(name, gender):
    assert( type(name) == type("") )
    assert( type(gender) == type(""))
    player = Player()
    player.set_name(name)
    player.set_id(uuid5(NAMESPACE_DNS, name).hex)
    player.set_gender(gender)
    playerlist = Playerlist()
    playerlist.add_player(player.id, player.name)
    player.save()
  def load(nameid):
    playerlist = Playerlist()
    player     = Player()
    if (nameid in playerlist.names):
      id = playerlist.invplayerdict[nameid]
    elif (nameid in playerlist.ids):
      id = nameid
    else:
      raise ValueError("{0:s} is not a known player".format(nameid))
    playerpath = join(playerdir, id)
    with open(playerpath, "r") as i:
      playerdict = load(i)
    player.set_name(playerdict["name"])
    player.set_id(playerdict["id"])
    player.set_gender(playerdict["gender"])
    player.set_status(playerdict["status"])
    player.set_bax_s(playerdict["bax_s"])
    player.set_bax_d(playerdict["bax_d"])
    player.set_bax_m(playerdict["bax_m"])
    player.set_bax_u(playerdict["bax_u"])
    player.set_bax_s_history(playerdict["bax_s_history"])
    player.set_bax_d_history(playerdict["bax_d_history"])
    player.set_bax_m_history(playerdict["bax_m_history"])
    player.set_bax_u_history(playerdict["bax_u_history"])
    player.set_pbr_s(playerdict["pbr_s"])
    player.set_pbr_d(playerdict["pbr_d"])
    player.set_pbr_m(playerdict["pbr_m"])
    player.set_pbr_u(playerdict["pbr_u"])
    player.set_pbr_s_history(playerdict["pbr_s_history"])
    player.set_pbr_d_history(playerdict["pbr_d_history"])
    player.set_pbr_m_history(playerdict["pbr_m_history"])
    player.set_pbr_u_history(playerdict["pbr_u_history"])
    player.set_matches_s(playerdict["matches_s"])
    player.set_matches_d(playerdict["matches_d"])
    player.set_matches_m(playerdict["matches_m"])
    player.set_matches_u(playerdict["matches_u"])
    player.set_matches_s_history(playerdict["matches_s_history"])
    player.set_matches_d_history(playerdict["matches_d_history"])
    player.set_matches_m_history(playerdict["matches_m_history"])
    player.set_matches_u_history(playerdict["matches_u_history"])
    return(player)
  def save(self):
    if not (self.id == ""):
      playerpath = join(playerdir, self.id)
      with open(playerpath, "w") as i:
        dump(self.__dict__, i, sort_keys=True, indent=4)
  def update_pbr_s(self):
    new_pbr = self.update_pbr(self.matches_s, self.pbr_s)
    self.set_pbr_s(new_pbr)
    self.add_pbr_s(new_pbr)
  def update_pbr_d(self):
    new_pbr = self.update_pbr(self.matches_d, self.pbr_d)
    self.set_pbr_d(new_pbr)
    self.add_pbr_d(new_pbr)
  def update_pbr_m(self):
    new_pbr = self.update_pbr(self.matches_m, self.pbr_m)
    self.set_pbr_m(new_pbr)
    self.add_pbr_m(new_pbr)
  def update_pbr_u(self):
    new_pbr = self.update_pbr(self.matches_u, self.pbr_u)
    self.set_pbr_u(new_pbr)
    self.add_pbr_u(new_pbr)
  def update_pbr(self, matches, pbr):
    performance = 0.0
    for i in matches:
      if (self.name in i["sideA"]):
        performance += i["pbrB"] + i["score_difference"]
      elif (self.name in i["sideB"]):
        performance += i["pbrA"] - i["score_difference"]
      else:
        raise ValueError("{0:s} here ... unable to update pbr ... somehow I seem to think to have played in a match that I did not play in ...".format(self.name))
    performance = float(performance)/float(len(matches))
    new_pbr = 0.5 * (pbr + performance)
    return(new_pbr)
  def update_bax_s(self):
    Bneu = self.update_bax(self.matches_s, self.bax_s)
    self.set_bax_s(Bneu)
    self.add_bax_s(Bneu)
  def update_bax_d(self):
    Bneu = self.update_bax(self.matches_d, self.bax_d)
    self.set_bax_d(Bneu)
    self.add_bax_d(Bneu)
  def update_bax_m(self):
    Bneu = self.update_bax(self.matches_m, self.bax_m)
    self.set_bax_m(Bneu)
    self.add_bax_m(Bneu)
  def update_bax_u(self):
    Bneu = self.update_bax(self.matches_u, self.bax_u)
    self.set_bax_u(Bneu)
    self.add_bax_u(Bneu)
  def update_bax(self, matches, bax):
    Balt  = bax
    n     = len(matches)
    Bopp  = []
    Sist  = 0.0
    Nvic  = 0.0
    for i in matches:
      if (self.name in i["sideA"]):
        Bopp.append(i["baxB"])
      elif (self.name in i["sideB"]):
        Bopp.append(i["baxA"])
      else:
        raise ValueError("{0:s} here ... unable to update bax ... somehow I seem to think to have played in a match that I did not play in ...".format(self.name))
      if (self.name in i["winner"]):
        if (len(i["games"]) == 2):
          Sist += 1.0
        elif (len(i["games"]) == 3):
          Sist += 0.8
        else:
          raise ValueError("{0:s} here ... unable to update bax ... somehow I seem to have played a match consisting of not 2 or 3 games ...".format(self.name))
        Nvic += 1.0
      else:
        if (len(i["games"]) == 2):
          Sist += 0.0
        elif (len(i["games"]) == 3):
          Sist += 0.2
        else:
          raise ValueError("{0:s} here ... unable to update bax ... somehow I seem to have played a match consisting of not 2 or 3 games ...".format(self.name))
        Nvic += 0.0
    Bniv  = float(sum(Bopp))/float(n)
    Wd    = [1.0/(1.0 + pow(10.0, -float(Balt-Bi)/50.0)) for Bi in Bopp]
    Ssoll = sum(Wd)
    Berst = Bniv + 7.0 * (Sist - float(n)/2.0)
    Bneu0 = Balt + 7.0 * (Sist - Ssoll)
    return(Bneu0)
    if (Balt <= Bniv):
      Bneu = min((5.0 * Bneu0 + 2.0 * Nvic/float(n) * Berst) / (5.0 + 2.0 * Nvic/float(n)), Berst)
    elif (Balt > Bniv):
      Bneu = max(((4.0 * Nvic/float(n) + 5.0) * Bneu0 + Berst) / (4.0 * Nvic/float(n) + 6.0), Berst)
    else:
      raise ValueError("{0:s} here ... unable to update bax ... Balt is neither lower than, nor equal to, nor greater than Bniv ...".format(self.name))
    return(Bneu)
