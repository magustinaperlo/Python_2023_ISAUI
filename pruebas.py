import os


def fun():
    print ("hello")


def rep(fin,max):
    con = 0
    while(con < max):
        os.system(fin)
        con += 1

rep("fun()",3)