# rjqa console

from fuzzywuzzy import fuzz
import os
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
    
    
    def __init__(self, name, buzzer_key):
        
        self.name = name
        self.buzzer_key = buzzer_key
        self.score = 0
        
        

class Game(object):
    
    
    def __init__(self):
        
        # players
        self.players = {}
        self.buzzers = {}
        
        # ste dataframe with all questions
        print('reticulating splines...')
        self.qdf = pd.read_csv(QA_FILE)
        
    
    def add_player(self, p):
        
        # add player
        self.players[p.name] = p
        
        # add buzzer
        self.buzzers[p.buzzer_key] = p.name
        
    
    def do_question(self):
    
        # get random index
        rq_index = int(random.random() * len(self.qdf))
        
        # get row
        rq = self.qdf.iloc[rq_index]
        
        # init Q
        q = Question(rq)
        
        # print
        print("%s for $%s:" % (q.category, q.value))
        print("\n%s" % q.question)
        
        # check buzzers
        while True:
            
            buzzer = input("\n\nbuzz in anytime...")
            
            if buzzer in self.buzzers.keys():
                
                # get player
                p = self.players[self.buzzers[buzzer]]
                
                # get answer
                a = input("Your answer, %s (enter after given)? " % p.name)
                
                # show answer
                print("The answer is: %s" % q.answer)
                
                # get verdict
                v = input("How'd you do ('y' for correct): ")
                
                if v == 'y':
                    
                    print("Well done!")
                    
                    # bump score
                    p.score += q.value
                
                else:
                    
                    print('Too bad')
                    
                    p.score -= q.value
                
                # continue
                input('enter to continue...')
                break
                    
            
            else:
                print("Don't recognize that buzzer, still waiting...")
                continue
            
        
        
class Question(object):
    
    def __init__(self, row):
        
        # save row
        self.row = row
        
        # parse
        self.category = row['category']
        self.question = row['question']
        self.answer = row['answer']
        self.value = row['value']
        
    
    def guess_a(self):
        pass
        
        
        
        
########################################################################
# Flow
########################################################################
if __name__ == "__main__":
    
    os.system('clear')
    
    print("Welcome to console rjqa (Random Jeopardy Question & Answer!\n")
    
    # init game
    g = Game()

    # get players
    pnum = int(input("\nHow many are playing? "))
    
    # loop through pnum and init players
    for x in range(0, pnum):
        
        # get name
        name = input("Player #%s name: " % (x + 1))
        
        # get buzzer key
        buzzer_key = input("Buzzer key for %s (except 'y' and 'n'): " % name)
        
        # init player
        p = Player(name, buzzer_key)
        
        # create player and add to game
        g.add_player(p)
        
    # get number of questions
    qnum = int(input("How many questions would you like to play?"))
    
    # loop through
    print("Let's play rjqa!")
    for x in range(0,qnum):
        
        # clear and init
        os.system('clear')
        print("Current scores:")
        for name,p in g.players.items():
            print('%s, $%s' % (p.name, p.score))
        print("Question %s / %s...\n\n" % ((x+1),qnum))
        
        # do question
        g.do_question()
        
    # wrap-up
    print("After a thrilling game, here are the results:")
    for name,p in g.players.items():
        print('%s, $%s' % (p.name, p.score))
    print("Finis.")