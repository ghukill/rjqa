# rjqa console

import pandas as pd
import random

########################################################################
# Settings
########################################################################
QA_FILE = 'jq_clean.csv'



########################################################################
# Models
########################################################################
class Player(object):
    
    
    def __init__(self, name):
        
        self.name = name
        self.score = 0
        
        

class Game(object):
    
    
    def __init__(self):
        
        # players
        self.players = {}
        
        # ste dataframe with all questions
        self.qdf = pd.read_csv(QA_FILE)
        
    
    def add_player(self, p):
        
        self.players[p.name] = p
        
    
    def do_question(self):
        
        
        
########################################################################
# Flow
########################################################################
if __name__ == "__main__":
    
    # init game
    g = Game()

    # get players
    pnum = int(input("How many are playing?"))
    
    # loop through pnum and init players
    for x in range(0, pnum):
        
        # get name
        name = input("Player #%s name: " % (x + 1))
        p = Player(name)
        
        # create player and add to game
        g.add_player(p)