#this file is like a unit test file we will be using to test rest of the files in this project
import numpy as np
import custompred

org_arr0 = [[0,0,0,0], [1, 1 , 2, 1], [-2,-2,-2,-2], [-2,1,-2,-2]]

comp_box = []
a = custompred.equ_help((2,0), (1,1))
#a.ind.append((1,0))
#a.ind.append((2,0))
a.par.append((1,0))
a.par.append((3,1))
comp_box.append(a)
b = custompred.equ_help((2,1), (1,1))
#b.ind.append((1,0))
#b.ind.append((2,1))
#b.ind.append((2,2))
b.par.append((1,0))
b.par.append((1,2))
b.par.append((3,1))
comp_box.append(b)
c = custompred.equ_help((2,2), (1,2))
#c.ind.append((1,3))
#c.ind.append((2,3))
c.par.append((1,1))
c.par.append((1,3))
c.par.append((3,1))
comp_box.append(c)
d = custompred.equ_help((2,3), (1,2))
d.par.append((1,3))
comp_box.append(d)
e = custompred.equ_help((3,0), (3,1))
e.ind.append((3,2))
comp_box.append(e)
custompred.setmin_max(comp_box,org_arr0)
com_set=[]
custompred.prob_generator(comp_box, org_arr0 , com_set)
print("<-----possible sets found-------->")
print(len(com_set))
print("<-----sets are--------->")
for box in comp_box:
    print(box.ind)
    print("<---next--->")
print(com_set)
