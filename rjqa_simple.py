# rjqa console

import os
import pandas as pd
import random

QA_FILE = 'jq_clean.csv'


os.system('clear')
print('reticulating splines...')
df = pd.read_csv(QA_FILE)
print('done')

while True:
    
     # get random index
    rq_index = int(random.random() * len(df))
    
    # get row
    rq = df.iloc[rq_index]
    
    # print
    print("%s for $%s:" % (rq['category'], rq['value']))
    print("\n%s" % rq['question'])
    input('\nenter for answer...')
    print("\n%s" % rq['answer'])
    input('\nenter for next question...')
    os.system('clear')
    continue