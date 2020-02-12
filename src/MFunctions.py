########################################################################
#%% import block     ###################################################
########################################################################
from CPlayerlist import Playerlist
from CPlayer import Player
from CMatch import Match
from MPaths import readmemdpath, readmepath
from random import random, choice
########################################################################
#%% printing constants     #############################################
########################################################################
borderstr      = "{0:#^72s}".format("")
messagefmt     = "{0:#^18s}     {{0: ^26s}}     {0:#^18s}".format("")
tablerowfmt    = "| {rank: <8s} | {baxname: <29s} {baxnmatches: >4s} | {bax: <7s} | {empty: <15s} | {rank: <8s} | {pbrname: <29s} {pbrnmatches: >4s} | {pbr: <7s} |\n"
tableheaderfmt = "|{0:-<10s}|{0:-<36s}|{0:-<9s}|{0:-<17s}|{0:-<10s}|{0:-<36s}|{0:-<9s}|\n".format("")
########################################################################
#%% prints the menu     ################################################
########################################################################
def print_menu():
  print(borderstr)
  print(borderstr)
  print(messagefmt.format("Welcome to the"))
  print(messagefmt.format("Harburger SC"))
  print(messagefmt.format("Badminton"))
  print(messagefmt.format("internal ranking"))
  print(messagefmt.format("manager"))
  print(borderstr)
  print(borderstr)
  print("")
########################################################################
#%% get userinput     ##################################################
########################################################################
def get_userinput():
  userinput        = ""
  possible_options = ["1","2","3","4","5","q"]
  while (True):
    if (type(userinput) == type("")) and (len(userinput) == 1):
      if (userinput in possible_options):
        break
      else:
        print("Please input either of: {0:s}".format(", ".join(possible_options)))
        userinput = input("    --> ")
    elif (len(userinput) > 0):
      print("Please input either of: {0:s}".format(", ".join(possible_options)))
      userinput = input("    --> ")
    else:
      print("Choose an action to perform:")
      print("    (1) {0:s}".format("Enter new match"))
      print("    (2) {0:s}".format("Show players"))
      print("    (3) {0:s}".format("Show rankings"))
      print("    (4) {0:s}".format("Draw random matches"))
      print("    (5) {0:s}".format("Add new player"))
      print("    (q) {0:s}".format("Exit"))
      userinput = input("    --> ")
  return(userinput)
########################################################################
#%% enter new match     ################################################
########################################################################
def get_side(otherside=None):
  playerlist = Playerlist()
  side = None
  mode = "B" if otherside else "A"
  while (True):
    print("Enter name(s) of player(s) of side {0:s}, i.e. 'Tobi, Hark' (q to quit):".format(mode))
    side = input("    --> ").strip().split(',')
    side = [i.strip() for i in side]
    if (side[0] == "q"):
      return(side)
    if (len(side) > 2):
      print("ERROR: Please enter only one or two names.")
      print("")
      continue
    if (otherside and not (len(side) == len(otherside))):
      print("ERROR: Please enter exactly {0:d} name{1:s} to match side A.".format(len(otherside),"" if len(otherside) == 1 else "s"))
      print("")
      continue
    elif not (False in [True in [j.lower() in i for i in [l.lower() for l in playerlist.names]] for j in side]):
      for j, jtem in enumerate(side):
        for i in playerlist.names:
          if (jtem.lower() in i.lower()):
            side[j] = i
            break
      if (len(side) == 2 and side[0] == side[1]):
        print("ERROR: Please enter two different names for side {0:s}".format(mode))
        print("")
        continue
      if (otherside and (True in [i in otherside for i in side])):
        print("ERROR: Please choose only players that are not already in side A")
        print("")
        continue        
      break
    else:
      print("ERROR: Player(s) '{0:s}' not found.".format(", ".join(side)))
      print("")
  print("Side {0:s} is '{1:s}'".format(mode, ", ".join(side)))
  return(side)
def get_type(sideA, sideB):
  playersA = [Player.load(i) for i in sideA]
  playersB = [Player.load(i) for i in sideB]
  if (len(sideA) == 1):
    if (playersA[0].gender == "m" and playersB[0].gender == "m"):
      type = "Men's singles"
    elif (playersA[0].gender == "f" and playersB[0].gender == "f"):
      type = "Women's singles"
    else:
      type = "Undefined discipline"
      #print("ERROR: This match type is not supported: {0:s} vs. {1:s}".format(playersA[0].gender, playersB[0].gender))
      #print("")
      #return("q")
  elif (len(sideA) == 2):
    if (playersA[0].gender == "m" and playersA[1].gender == "m" and playersB[0].gender == "m" and playersB[1].gender == "m"):
      type = "Men's doubles"
    elif (playersA[0].gender == "f" and playersA[1].gender == "f" and playersB[0].gender == "f" and playersB[1].gender == "f"):
      type = "Women's doubles"
    elif ( not playersA[0].gender == playersA[1].gender and not playersB[0].gender == playersB[1].gender):
      type = "Mixed doubles"
    else:
      type = "Undefined discipline"
      #print("ERROR: This match type is not supported: {0:s}/{1:s} vs. {2:s}/{2:s}".format(playersA[0].gender, playersA[1].gender, playersB[0].gender, playersB[1].gender))
      #print("")
      #return("q")
  else:
      print("ERROR: There are {:d} players assigned on sideA. This is not allowed.".format(len(sideA)))
      print("")
      return("q")
  return(type)
def get_game(games):
  number = "first" if (len(games) == 0) else "second" if (len(games) == 1) else "third"
  while (True):
    print("Enter the result of the {0:s} game, i.e. '21:7' if side A scored 21 points and side B scored 7 points (q to quit).".format(number))
    game = input("    --> ").split(":")
    if ("q" in game):
      return("q")
    invalid_score = False
    for i in game:
      for j in i.strip():
        if not (j in "0123456789"):
          invalid_score = True
    # check if game result is valid
    if (invalid_score):
      print("ERROR: Please type in games result as i.e. '17:21' if side B won.")
      print("")
      continue
    w = int(game[0]) if (int(game[0]) > int(game[1])) else int(game[1])
    l = int(game[0]) if (int(game[0]) < int(game[1])) else int(game[1])
    if (w == l):
      print("ERROR: Games result ({0:s}:{1:s}) is not possible. There has to be a winner.".format(*game))
      print("")
      continue
    elif (w < 21):
      print("ERROR: Games winners score ({0:d}) must be at least 21 points.".format(w))
      continue
    elif (w > 30):
      print("ERROR: Games winners score ({0:d}) must not exceed 30 points".format(w))
      continue
    elif (w == 30 and l < 28):
      print("ERROR: Impossible game result: {0:s}:{1:s}".format(*game))
      continue
    elif (w > 21 and w < 30 and not w-l == 2 ):
      print("ERROR: Impossible game result: {0:s}:{1:s}".format(*game))
      continue
    break
  return((int(game[0]),int(game[1])))
def enter_new_match():
  sideA = get_side()
  if (sideA[0] == "q"):
    return()
  sideB = get_side(sideA)
  if (sideB[0] == "q"):
    return()
  type  = get_type(sideA, sideB)
  if (type == "q"):
    return()
  games = []
  outcome = ""
  games.append(get_game(games))
  if ("q" in games):
    return()
  outcome += "A" if (games[-1][0] > games[-1][1]) else "B"
  games.append(get_game(games))
  if ("q" in games):
    return()
  outcome += "A" if (games[-1][0] > games[-1][1]) else "B"
  if not (outcome == "AA" or outcome == "BB"):
    games.append(get_game(games))
  if ("q" in games):
    return()
  match = Match(sideA, sideB, type, games)
  players = [Player.load(i) for i in sideA] + [Player.load(j) for j in sideB]
  if ("mixed" in type.lower()):
    for i in players:
      i.add_match_m(match.__dict__)
  elif ("doubles" in type.lower()):
    for i in players:
      i.add_match_d(match.__dict__)
  elif ("singles" in type.lower()):
    for i in players:
      i.add_match_s(match.__dict__)
  elif ("undefined" in type.lower()):
    for i in players:
      i.add_match_u(match.__dict__)
  else:
    raise ValueError("ERROR: Unknown match type '{0:s}' enountered in 'enter_new_match'".format(type))
  update_rankings()
########################################################################
#%% show players     ###################################################
########################################################################
def show_players():
  playerlist = Playerlist()
  print(borderstr)
  print(borderstr)
  print(messagefmt.format("List of players"))
  print(borderstr)
  print(borderstr)
  print("")
  print("{0:_^34}____{1:_^34}".format("ID","Name"))
  for i in sorted(playerlist.names):
    print("{0: <34} |  {1: <34}".format(playerlist.invplayerdict[i], i))
  print("")
  print(borderstr)
  print(borderstr)
  print("")
########################################################################
#%% show rankings     ##################################################
########################################################################
def show_rankings():
  for type in ["ud", "ms", "md", "ws", "wd", "mx"]:
    show_ranking(type)
def create_ranking(type):
  playerlist  = Playerlist()
  baxlist     = []
  pbrlist     = []
  for i in playerlist.ids:
    player = Player.load(i)
    if (type == "ms" and player.gender == "m"):
      baxlist.append((player.bax_s, player.name, len(player.bax_s_history)-1))
      pbrlist.append((player.pbr_s, player.name, len(player.pbr_s_history)-1))
    elif (type == "md" and player.gender == "m"):
      baxlist.append((player.bax_d, player.name, len(player.bax_d_history)-1))
      pbrlist.append((player.pbr_d, player.name, len(player.pbr_d_history)-1))
    elif (type == "ws" and player.gender == "f"):
      baxlist.append((player.bax_s, player.name, len(player.bax_s_history)-1))
      pbrlist.append((player.pbr_s, player.name, len(player.pbr_s_history)-1))
    elif (type == "wd" and player.gender == "f"):
      baxlist.append((player.bax_d, player.name, len(player.bax_d_history)-1))
      pbrlist.append((player.pbr_d, player.name, len(player.pbr_d_history)-1))
    elif (type == "mx"):
      baxlist.append((player.bax_m, player.name, len(player.bax_m_history)-1))
      pbrlist.append((player.pbr_m, player.name, len(player.pbr_m_history)-1))
    elif (type == "ud"):
      baxlist.append((player.bax_u, player.name, len(player.bax_u_history)-1))
      pbrlist.append((player.pbr_u, player.name, len(player.pbr_u_history)-1))
  baxlist.sort(reverse=True)
  pbrlist.sort(reverse=True)
  assert(len(baxlist) == len(pbrlist))
  return((baxlist, pbrlist))
def show_ranking(type):
  baxlist, pbrlist = create_ranking(type)
  print(borderstr)
  print(borderstr)
  print(messagefmt.format("Ranking {0:s}".format(type.upper())))
  print(borderstr)
  print(borderstr)
  print("")
  print("{0:_^34}____{1:_^34}".format("BAX","PBR"))
  for i in range(len(baxlist)):
    print("{rank: >2d} {baxname: <20s} ({baxnmatches: >2d}) {bax: <6.2f} | {rank: >2d} {pbrname: <20s} ({pbrnmatches: >2d}) {pbr: <6.2f}".format(baxname=baxlist[i][1], bax=baxlist[i][0], baxnmatches=baxlist[i][2], pbrname=pbrlist[i][1], pbr=pbrlist[i][0], pbrnmatches=pbrlist[i][2], rank=i+1))
  print("")
  print(borderstr)
  print(borderstr)
  print("")    
def update_rankings():
  with open(readmemdpath,"w") as outfile:
    outfile.write(tablerowfmt.format(rank="", baxname="", bax="", baxnmatches="", empty="", pbrname="", pbr="", pbrnmatches=""))
    outfile.write(tableheaderfmt)
    for type in ["ud", "ms", "md", "ws", "wd", "mx"]:
      baxlist, pbrlist = create_ranking(type)
      outfile.write(tablerowfmt.format(rank="", baxname="", bax="", baxnmatches="", empty="**Rankings {0:s}**".format(type.upper()), pbrname="", pbr="", pbrnmatches=""))
      outfile.write(tablerowfmt.format(rank="**Rank**", baxname="**Name (# of matches)**", bax="**BAX**", baxnmatches="", empty="", pbrname="**Name (# of matches)**", pbr="**PBR**", pbrnmatches=""))
      for i in range(len(baxlist)):
        outfile.write(tablerowfmt.format(rank="{0: <8d}".format(i+1), baxname=baxlist[i][1], bax="{0: <7.2f}".format(baxlist[i][0]), baxnmatches="({0: >2d})".format(baxlist[i][2]), empty="", pbrname=pbrlist[i][1], pbr="{0: <7.2f}".format(pbrlist[i][0]), pbrnmatches="({0: >2d})".format(pbrlist[i][2]) ))
    with open(readmepath, "r") as appendfile:
      outfile.write(appendfile.read())
########################################################################
#%% draw random (within constraints) matches of the week     ###########
########################################################################
def print_random_matches(matches):
  print(borderstr)
  print(borderstr)
  print(messagefmt.format("Random matches"))
  print(borderstr)
  print(borderstr)
  print("")
  for i, item in enumerate(matches):
    print("{0:2d}: {1:s}".format(i+1, item))
    print("")
  print("")
  print(borderstr)
  print(borderstr)
  print("")
def match2str(matches):
  matchstrs = []
  for i in matches:
    if (len(i) == 4):
      # UDD, MX or *D match
      matchstrA = ", ".join([j.name for j in i[0:2]])
      matchstrB = ", ".join([j.name for j in i[2:4]])
      matchstr  = " *vs.* ".join([matchstrA, matchstrB])
      if (i[0].gender != i[1].gender and i[2].gender != i[3].gender):
        # MX match
        baxA = 0.5*(i[0].bax_m + i[1].bax_m)
        baxB = 0.5*(i[2].bax_m + i[3].bax_m)
        pbrA = 0.5*(i[0].pbr_m + i[1].pbr_m)
        pbrB = 0.5*(i[2].pbr_m + i[3].pbr_m)
        if (abs(baxA - baxB) > 30.0 or abs(pbrA - pbrB) > 12.0):
          matchstr += " *(FORBIDDEN)*"
      elif (i[0].gender == i[1].gender and i[1].gender == i[2].gender and i[2].gender == i[3].gender):
        # *D match
        baxA = 0.5*(i[0].bax_d + i[1].bax_d)
        baxB = 0.5*(i[2].bax_d + i[3].bax_d)
        pbrA = 0.5*(i[0].pbr_d + i[1].pbr_d)
        pbrB = 0.5*(i[2].pbr_d + i[3].pbr_d)
        if (abs(baxA - baxB) > 30.0 or abs(pbrA - pbrB) > 12.0):
          matchstr += " *(FORBIDDEN)*"
      else:
        # UDD match
        baxA = 0.5*(i[0].bax_u + i[1].bax_u)
        baxB = 0.5*(i[2].bax_u + i[3].bax_u)
        pbrA = 0.5*(i[0].pbr_u + i[1].pbr_u)
        pbrB = 0.5*(i[2].pbr_u + i[3].pbr_u)
        if (abs(baxA - baxB) > 30.0 or abs(pbrA - pbrB) > 12.0):
          matchstr += " *(FORBIDDEN)*"
    elif (len(i) == 2):
      matchstr  = " *vs.* ".join([j.name for j in i])
      # UDS or *S match
      if (i[0].gender == i[1].gender):
        # *S match
        if (abs(i[0].bax_s - i[1].bax_s) > 30.0 or abs(i[0].pbr_s - i[1].pbr_s) > 12.0):
          matchstr += " *(FORBIDDEN)*"
      else:
        # UDS match
        if (abs(i[0].bax_u - i[1].bax_u) > 30.0 or abs(i[0].pbr_u - i[1].pbr_u) > 12.0):
          matchstr += " *(FORBIDDEN)*"
    matchstrs.append(matchstr)
  return(matchstrs)
def draw_players(players, allplayers, allmales, allfemales, *args):
  match = []
  match.append(choice(players))
  sexA  = match[0].gender
  for i in args[1:]:
    if (i == "any"):
      while(True):
        tmp = choice(allplayers)
        if not (tmp.name in [j.name for j in match]):
          break
    elif (i == "same"):
      if (sexA == "m"):
        while(True):
          tmp = choice(allmales)
          if not (tmp.name in [j.name for j in match]):
            break
      elif (sexA == "f"):
        while(True):
          tmp = choice(allfemales)
          if not (tmp.name in [j.name for j in match]):
            break
      else:
        raise ValueError("gender error in same draw in draw_players()")
    elif (i == "other"):
      if (sexA == "m"):
        while(True):
          tmp = choice(allfemales)
          if not (tmp.name in [j.name for j in match]):
            break
      elif (sexA == "f"):
        while(True):
          tmp = choice(allmales)
          if not (tmp.name in [j.name for j in match]):
            break
      else:
        raise ValueError("gender error in other draw in draw_players()")
    else:
      raise ValueError("error in draw_players()")
    match.append(tmp)
  return(match)
def draw_random_matches():
  playerlist = Playerlist()
  players    = [Player.load(i) for i in playerlist.ids]
  allplayers = players[:]
  males      = [i for i in players if i.gender == "m"]
  allmales   = males[:]
  females    = [i for i in players if i.gender == "f"]
  allfemales = females[:]
  matches    = []
  while (len(players) >= 1):
    match_type = ""
    rng = random()
    if (rng <= 0.19):
      # UD match
      rng = random()
      if (rng <= 0.5):
        # UD doubles
        match = draw_players(players, allplayers, allmales, allfemales, "any", "any", "any", "any")
      elif (rng <= 1.0):
        # UD singles
        match = draw_players(players, allplayers, allmales, allfemales, "any", "any")
      else:
        raise ValueError("Invalid random number in UD match draw")
    elif (rng <= 0.46):
      # MX match
        match = draw_players(players, allplayers, allmales, allfemales, "any", "other", "same", "other")
    elif (rng <= 0.73):
      # *D match
        match = draw_players(players, allplayers, allmales, allfemales, "any", "same", "same", "same")
    elif (rng <= 1.00):
      # *S match
        match = draw_players(players, allplayers, allmales, allfemales, "any", "same")
    else:
      raise ValueError("Invalid random number in draw_random_matches")
    for i in match:
      for j, jtem in enumerate(players):
        if (i.name == jtem.name):
          del players[j]
    matches.append(match)
  print_random_matches(match2str(matches))
########################################################################
#%% create new player     ##############################################
########################################################################
def add_new_player():
  playerlist = Playerlist()
  print(borderstr)
  print(borderstr)
  print(messagefmt.format("Adding new player"))
  print(borderstr)
  print(borderstr)
  print("")
  while (True):
    print("Enter the name of the new Player, i.e. Max Mustermann (enter q to quit):")
    name = input("    --> ").strip()
    if (name == "q"):
        return()
    elif (name in playerlist.names):
      print("ERROR: Player '{0:s}' already exists.".format(name))
      print("")
    else:
      break
  while (True):
    print("Enter the gender (m or f) of {0:s} (enter q to quit):".format(name))
    gender = input("    --> ").strip()
    if (gender == "q"):
        return()
    elif (gender not in ["m", "f"]):
      print("ERROR: Player '{0:s}' must be male (m) or female (f).".format(name))
      print("")
    else:
      break
  Player.create(name, gender)
