########################################################################
#%% import block     ###################################################
########################################################################
from CPlayerlist import Playerlist
from CPlayer import Player
from CMatch import Match
from MPaths import readmemdpath, readmepath
from random import random, randrange#, choice
########################################################################
#%% printing constants     #############################################
########################################################################
borderstr      = "{0:#^72s}".format("")
messagefmt     = "{0:#^18s}     {{0: ^26s}}     {0:#^18s}".format("")
tablerowfmt    = "| {0: <8s} | {1: <34s} | {2: <7s} | {3: <15s} | {0: <8s} | {4: <34s} | {5: <7s} |\n"
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
      baxlist.append((player.bax_s, player.name))
      pbrlist.append((player.pbr_s, player.name))
    elif (type == "md" and player.gender == "m"):
      baxlist.append((player.bax_d, player.name))
      pbrlist.append((player.pbr_d, player.name))
    elif (type == "ws" and player.gender == "f"):
      baxlist.append((player.bax_s, player.name))
      pbrlist.append((player.pbr_s, player.name))
    elif (type == "wd" and player.gender == "f"):
      baxlist.append((player.bax_d, player.name))
      pbrlist.append((player.pbr_d, player.name))
    elif (type == "mx"):
      baxlist.append((player.bax_m, player.name))
      pbrlist.append((player.pbr_m, player.name))
    elif (type == "ud"):
      baxlist.append((player.bax_u, player.name))
      pbrlist.append((player.pbr_u, player.name))
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
    print("{4: >2d} {0: <25s} {1: <6.2f} | {4: >2d} {2: <25s} {3: <6.2f}".format(baxlist[i][1], baxlist[i][0], pbrlist[i][1], pbrlist[i][0], i+1))
  print("")
  print(borderstr)
  print(borderstr)
  print("")    
def update_rankings():
  with open(readmemdpath,"w") as outfile:
    outfile.write(tablerowfmt.format("", "", "", "", "", ""))
    outfile.write(tableheaderfmt)
    for type in ["ud", "ms", "md", "ws", "wd", "mx"]:
      baxlist, pbrlist = create_ranking(type)
      outfile.write(tablerowfmt.format("", "", "", "**Rankings {0:s}**".format(type.upper()), "", ""))
      outfile.write(tablerowfmt.format("**Rank**", "**Name**", "**BAX**", "", "**Name**", "**PBR**"))
      for i in range(len(baxlist)):
        outfile.write(tablerowfmt.format("{0: <8d}".format(i+1), baxlist[i][1], "{0: <7.2f}".format(baxlist[i][0]), "", pbrlist[i][1], "{0: <7.2f}".format(pbrlist[i][0]) ))
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
    print("")
    print("{0:3d}: {1:^70s}".format(i, item))
    print("")
  print("")
  print(borderstr)
  print(borderstr)
  print("")
def draw_random_matches():
  maxretries = 4
  playerlist = Playerlist()
  players    = [Player.load(i) for i in playerlist.ids]
  males      = [i for i in players if i.gender == "m"]
  females    = [i for i in players if i.gender == "f"]
  matches    = []
  retries    = 0
  while (len(players) >= 2):
    if (retries > maxretries):
      print_random_matches(matches)
    rng        = random()
    if (rng <= 0.7):
      # any match
      tmpplayers = players.copy()
      rng = random()
      if (rng <= 0.5):
        # any doubles
        if (len(tmpplayers) < 4):
          retries += 1
          continue
        sideAA = tmpplayers.pop(randrange(len(tmpplayers)))
        sideAB = tmpplayers.pop(randrange(len(tmpplayers)))
        sideA  = "{0:s},{1:s}".format(sideAA.name, sideAB.name)
        sideBA = tmpplayers.pop(randrange(len(tmpplayers)))
        sideBB = tmpplayers.pop(randrange(len(tmpplayers)))
        sideB  = "{0:s},{1:s}".format(sideBA.name, sideBB.name)
        match  = sideA+" vs. "+sideB
        pbrs   = [sideAA.pbr_d, sideAB.pbr_d, sideBA.pbr_d, sideBB.pbr_d]
        if (max(pbrs) - min(pbrs) > 12.0):
          match += " !!! FORBIDDEN !!!"
        if (retries < maxretries and "FORBIDDEN" in match):
          retries += 1
          continue
        else:
          matches.append(match)
          players = tmpplayers.copy()
          retries = 0
      else:
        # any singles
        if (len(tmpplayers) < 2):
          retries += 1
          continue
        sideA  = tmpplayers.pop(randrange(len(tmpplayers)))
        sideB  = tmpplayers.pop(randrange(len(tmpplayers)))
        match  = "{0:s} vs. {1:s}".format(sideA.name, sideB.name)
        pbrs   = [sideA.pbr_s, sideB.pbr_s]
        if (max(pbrs) - min(pbrs) > 12.0):
          match += " !!! FORBIDDEN !!!"
        if (retries < maxretries and "FORBIDDEN" in match):
          retries += 1
          continue
        else:
          matches.append(match)
          players = tmpplayers.copy()
          retries = 0
    elif (rng <= 0.8):
      # mixed
      males   = [i for i in players if i.gender == "m"]
      females = [i for i in players if i.gender == "f"]
      if (len(males) < 2 or len(females) < 2):
        retries += 1
        continue
      sideAA  = males.pop(randrange(len(males)))
      sideAB  = females.pop(randrange(len(females)))
      sideA   = "{0:s},{1:s}".format(sideAA.name, sideAB.name)
      sideBA  = males.pop(randrange(len(males)))
      sideBB  = females.pop(randrange(len(females)))
      sideB   = "{0:s},{1:s}".format(sideBA.name, sideBB.name)
      match   = sideA+" vs. "+sideB
      pbrs    = [sideAA.pbr_m, sideAB.pbr_m, sideBA.pbr_m, sideBB.pbr_m]
      if (max(pbrs) - min(pbrs) > 12.0):
        match += " !!! FORBIDDEN !!!"
      if (retries < maxretries and "FORBIDDEN" in match):
        retries += 1
        continue
      else:
        matches.append(match)
        players = males.copy()+females.copy()
        retries = 0
    elif (rng <= 0.9):
      # doubles
      males      = [i for i in players if i.gender == "m"]
      females    = [i for i in players if i.gender == "f"]
      rng = random()
      tmpplayers = males if rng <= 0.5 else females
      if (len(tmpplayers) < 4):
        retries += 1
        continue
      sideAA = tmpplayers.pop(randrange(len(tmpplayers)))
      sideAB = tmpplayers.pop(randrange(len(tmpplayers)))
      sideA  = "{0:s},{1:s}".format(sideAA.name, sideAB.name)
      sideBA = tmpplayers.pop(randrange(len(tmpplayers)))
      sideBB = tmpplayers.pop(randrange(len(tmpplayers)))
      sideB  = "{0:s},{1:s}".format(sideBA.name, sideBB.name)
      match  = sideA+" vs. "+sideB
      pbrs   = [sideAA.pbr_d, sideAB.pbr_d, sideBA.pbr_d, sideBB.pbr_d]
      if (max(pbrs) - min(pbrs) > 12.0):
        match += " !!! FORBIDDEN !!!"
      if (retries < maxretries and "FORBIDDEN" in match):
        retries += 1
        continue
      else:
        matches.append(match)
        players = males.copy()+females.copy()
        retries = 0
    elif (rng <= 1.0):
      # singles
      males      = [i for i in players if i.gender == "m"]
      females    = [i for i in players if i.gender == "f"]
      rng = random()
      tmpplayers = males if rng <= 0.5 else females
      if (len(tmpplayers) < 2):
        retries += 1
        continue
      sideA = tmpplayers.pop(randrange(len(tmpplayers)))
      sideB = tmpplayers.pop(randrange(len(tmpplayers)))
      match  = "{0:s} vs. {1:s}".format(sideA.name, sideB.name)
      pbrs   = [sideA.pbr_s, sideB.pbr_s]
      if (max(pbrs) - min(pbrs) > 12.0):
        match += " !!! FORBIDDEN !!!"
      if (retries < maxretries and "FORBIDDEN" in match):
        retries += 1
        continue
      else:
        matches.append(match)
        players = males.copy()+females.copy()
        retries = 0
  print_random_matches(matches)
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
