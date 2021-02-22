#here we gonna call all madlibs

from madlib import madlibs,lap,hungergame,subject
import random

if __name__=="__main__":
    m=random.choice([madlibs,lap,hungergame,subject])
    m.madlib()




