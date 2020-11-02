import numpy as np
from graphics import *
import random
import opennegb
import grid

"""
class box:
    def __init__(self,state,neg_mine):
        self.state = state
        self.neg_mine = neg_mine
        self.neg_Notmine = 8 - neg_mine
        self.disc_mine = []
        self.disc_safe = []
    def discbox_mine(self, i , j):
        if(len(self.disc_mine) != 8):
            self.disc_mine.append((i,j))
    def discbox_safe(self, i , j):
        if(len( self.disc_safe) !=):
            self.disc_safe.append((i,j))
"""
colors = { -1:[0,0,0], 0:[215,255,215] , 1:[135, 206, 235], 2:[0, 128, 0] , 3:[255, 0, 0], 4:[128, 0, 128],
           5:[128, 0, 0], 6 :[64, 224, 208], 7:[255, 192, 203] , 8:[128, 128, 128], 9:[255,255,255]}

def up(ival, jval,n):
    if(ival ==0):
        return None
    return [ival-1, jval]
def down(ival, jval,n):
    if(ival <n-1):
        return [iva+1, jval]
    return None
def left(ival,jval,n):
        if(jval >0):
            return [ival , jval -1]
        return
        None
def right(ival, jval, n ):
    if(jval<n-1):
        return[ival, jval+1]
    return None
def upleft(ival, jval , n):
    if( up(ival,jval,n) != None and left(ival,jval,n) != None):
        return[ival-1, jval-1]
    return None
def upright(ival, jval , n):
    if( up(ival,jval,n) != None and right(ival,jval,n) != None):
        return[ival-1, jval+1]
    return None
def downleft(ival, jval, n):
    if( down(ival,jval,n) != None and left(ival,jval,n) != None):
        return[ival+1, jval-1]
    return None
def downright(ival, jval, n):
    if( down(ival,jval,n) != None and right(ival,jval,n) != None):
        return[ival+1, jval+1]
    return None
def mark_allsafe(ival,jval,agent_mtx, n,pairs):
    x = opennegb.getneg(ival, jval,n)
    for index in x:
        i = index[0]
        j = index[1]
        if( check_inpairs(index, pairs) == False):
            continue
        pairs.remove(index)
        #agent_mtx[i][j] = 1
        agent_mtx[i][j] = 9
    return x
def sm_idf(ival, jval , agent_mtx ,n):
    x = opennegb.getneg(ival, jval,n)
    safe = []
    mine = []
    unidf = []
    for index in x:
        if( agent_mtx[index[0], index[1]] == 9):
            safe.append(index)
        if( agent_mtx[index[0], index[1]] == -1):
            mine.append(index)
        if( agent_mtx[index[0], index[1]] == 0):
            unidf.append(index)
    return safe , mine , unidf

def set_allmines(unidf, agent_mtx , pairs):
    for index in unidf:
        if (check_inpairs(index, pairs) == False):
            continue
        agent_mtx[index[0]][index[1]] = -1
        pairs.remove(index)  #removing the identified box
def check_inpairs(index, pairs):
    if( len(pairs) ==0):
        return False
    for p in pairs:
        if( index[0] == p[0] and index[1] == p[1]):
            return True

    return False
def mark_safe(unidf, agent_mtx , pairs ):
    for index in unidf:
        if ( check_inpairs(index, pairs) == False ):
            continue
        pairs.remove(index)
        #agent_mtx[index[0]][index[1]] = 1
        agent_mtx[index[0]][index[1]] = 9
def agent_moves(ij_pairs, pairs, agent_mtx, arr,n):
    #print(ij_pairs)
    ival = ij_pairs[0]
    jval = ij_pairs[1]
    if( arr[ival][jval] == -1): #the box is a mine
        agent_mtx[ival][jval] = -1
        return
    if(arr[ival][jval] == 0): #the box has no neightbors that are mines
        #agent_mtx[ival][jval] = 1
        agent_mtx[ival][jval] = 9
        x = mark_allsafe(ival,jval,agent_mtx,n , pairs)
        for index in x: #keep exploring
            if( check_inpairs(index, pairs) == False):
                continue
            else:
                agent_moves(index, pairs, agent_mtx, arr,n)
        return


    safe ,mines , unidf = sm_idf(ival , jval, agent_mtx, n)  # if you are here then it means you are not in a mine or a box with all safe neighbors but now you have to make a decision
    #now we have number of identidied safe and mines round the box
    if( arr[ival][jval] - len(mines) == len(unidf)):  # in this we are saying that if the total number of mines - the known mines = hidden then all hidden are mines
        #agent_mtx[ival][jval] = 1
        agent_mtx[ival][jval] = 9
        set_allmines(unidf, agent_mtx , pairs)
        return  # return because no where to go now
    totalsafe = 8-arr[ival][jval]
    if( totalsafe - len(safe) == len(unidf)):
        #agent_mtx[ival][jval]=1
        agent_mtx[ival][jval]=9
        mark_safe(unidf, agent_mtx , pairs )
        random.shuffle(unidf)  # shuffles it to meake it more random
        for index in unidf:
            if( check_inpairs(index, pairs) == False):
                continue
            else:
                pairs.remove(index)
                agent_moves(index, pairs, agent_mtx, arr,n)  # recorsive meathods that explores the once that are safe
    #agent_mtx[ival][jval] = 1
    agent_mtx[ival][jval] = 9


def start_agent(n, arr):
    pairs = []
    for i in range(0,n):
        for j in range(0,n):
            pairs.append((i,j))
    #return_box =[]
    agent_mtx = np.zeros((n,n))
    while(len(pairs) >0):
        ival = random.randint(0,len(pairs))-1
        ij_pairs = pairs[ival]
        pairs.remove(ij_pairs)
        agent_moves(ij_pairs, pairs, agent_mtx, arr,n)
        newmatrix = agent_mtx



        w, gui = grid.buildmaze(n) #now that we have the base w and gui which is each boxes we can start coloring them
        gui = np.array(gui)
        gui = gui.reshape((n,n))
        w.setBackground('white')
        newmatrix = np.array(newmatrix)


        #print(val)
        #print(val[0][0])
        for i in range(0,n):
            for j in range( 0 , n):
                #print(arr[i][j])
                #if(val[i][j] == -1):
                #    gui[i][j].setFill(color_rgb(0,0,0))
                #    continue
                c = colors[newmatrix[i][j]]
                gridnum = newmatrix[i][j]
                #print("this is the value of n: " + str(gridnum))
                #print(val[i][j])
                #print(c[0])
                #print(type(gui[i][j]))
                gui[i][j].setFill(color_rgb(c[0],c[1],c[2]))

                gui[i][j].draw(w)
        w.getMouse()
        w.close()





        #newmatrix = agent_mtx
        #matrixgui.matrix_gui(n,newmatrix)
        #if(pairs == None): #you don't need this
            #break

    return agent_mtx
