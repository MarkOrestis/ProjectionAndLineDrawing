# In the routine below, you should draw your initials in perspective
# Orestis Markozanes

from matlib import *
from drawlib import *

def persp_initials():
    global mylist
    
    gtInitialize()
    gtPerspective(100,-100,100)
    
    
    gtPushMatrix()
    gtTranslate(0,-10,-30)
    gtRotateX(-40)
    gtScale(2.5,2.5,2.5)
    letter_M()    
    gtPopMatrix()
    
    gtPushMatrix()
    gtTranslate (-0.37, 0.97, 0)
    gtRotateX(20)
    gtScale (0.17, 0.17, 1)
    letter_O()   
    gtPopMatrix()

    del mylist[:]
             
             
def letter_O():
    steps = 64
    xold = 1
    yold = 0
    gtBeginShape()
    for i in range(steps+1):
        theta = 2 * 3.1415926535 * i / float(steps)
        x = cos(theta)
        y = sin(theta)
        gtVertex (xold, yold, 1)
        gtVertex (x, y, 1)
        xold = x
        yold = y
    gtEndShape()
    
def letter_M():
    
    gtVertex(-1, 0, 10)
    gtVertex(-1, 3, 10)
    
    gtVertex(-1, 3, 10)
    gtVertex( 0, 2, 10)
    
    gtVertex( 0, 2, 10)
    gtVertex( 1, 3, 10)
    
    gtVertex(1, 3, 10)
    gtVertex(1, 0, 10)
    
    gtEndShape()