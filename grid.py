from graphics import *
import numpy as np
import math
n = 20
def probmatrix(dimension, number_of_mines):   #meathod for calculating the initial matrix
    total = n*n
    arr = []
    #print(z)
    for i in range(0,number_of_mines):
        arr.append(1)
    for i in range(number_of_mines,total):
        arr.append(0)

    np.random.shuffle(arr)
    return arr

def buildmaze(n):
    win = GraphWin("My maze" , n*40 ,n*40)
    arr = []
    l = 0
    k = 40
    for i in range(0,n):
        for j in range(0,n):
            shape = Rectangle(Point(l, i*40), Point(k,40*(i+1)))
            #print(l)
            shape.setOutline("blue")
            shape.setFill("red")
            arr.append(shape)
            l = l+40
            k = k+40
        l=0
        k =40
    #print(type(arr[0][0]))
    return win, arr
"""
val = np.array(probmatrix(n,20)).reshape((n,n))
w , arr = buildmaze(n)
w.setBackground('black')
arr = np.array(arr)
arr = arr.reshape((n,n))
print( arr.shape)
for i in range(0,n):
    for j in range( 0 , n):
        #print(arr[i][j])
        if( val[i][j] == 0):
            arr[i][j].setFill(color_rgb(40,255,40))
            arr[i][j].draw(w)
        else:
            arr[i][j].draw(w)
#m = np.array((10,10))

w.getMouse()
w.close()
"""
