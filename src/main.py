#!/usr/bin/env python3
########################################################################
#%% import block     ###################################################
########################################################################
from init import init
from MFunctions import print_menu, get_userinput, enter_new_match \
                     , show_players, show_rankings, draw_random_matches \
                     , add_new_player
########################################################################
#%% main program     ####################################################
########################################################################
init()
print_menu()
while (True):
  userinput = get_userinput()
  if (userinput == "1"):
    enter_new_match()
  elif (userinput == "2"):
    show_players()
  elif (userinput == "3"):
    show_rankings()
  elif (userinput == "4"):
    draw_random_matches()
  elif (userinput == "5"):
    add_new_player()
  elif (userinput == "q"):
    break
  else:
    raise ValueError("Unexpected value for userinput: '{:s}'".format(userinput))
