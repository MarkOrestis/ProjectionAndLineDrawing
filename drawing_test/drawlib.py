# Drawing Routines, like OpenGL
# Orestis Markozanes
from matlib import *

mylist = []
gtleft = 0
gtright = 0
gtbottom = 0
gttop = 0
gtorthographic = 0
gtperspective = 0
gtnear = 0
gtfar = 0
gtfov = 0





def gtOrtho(left, right, bottom, top, near, far):
    global gtleft
    global gtright
    global gtbottom
    global gttop
    global gtorthographic
    global gtperspective
    
    gtleft = left
    gtright = right
    gtbottom = bottom
    gttop = top
    gtorthographic = 1
    gtperspective = 0
    

def gtPerspective(fov, near, far):
    global gtfov
    global gtnear
    global gtfar
    global gtorthographic
    global gtperspective
    
    gtfov = fov
    gtnear = near
    gtfar = far
    gtorthographic = 0
    gtperspective = 1

def gtBeginShape():
    
    pass
    
def gtEndShape():
    if (gtorthographic == 1):
        for i in range(0,len(mylist) - 1, 2):
            startx = (mylist[i][0] - gtleft) * width/(gtright - gtleft)
            starty = (mylist[i][1] - gtbottom) * height/(gttop - gtbottom)
            
            endx = (mylist[i + 1][0] - gtleft) * width/(gtright-gtleft)
            endy = (mylist[i + 1][1] - gtbottom) * height/(gttop - gtbottom)
        
            line(startx, height - starty, endx, height - endy)
    
    if (gtperspective == 1):
        # gtfov = gtfov * PI/180
        
        k = tan(radians(gtfov/2))
        for i in range(0, len(mylist) - 1, 2):
            startx = mylist[i][0]/abs(mylist[i][2])
            starty = mylist[i][1]/abs(mylist[i][2])
            
            endx = mylist[i+1][0]/abs(mylist[i+1][2])
            endy = mylist[i+1][1]/abs(mylist[i+1][2])
            
            finalstartx = (startx + k) * width/(2*k)
            finalstarty = (starty + k) * height/(2*k)
            
            finalendx = (endx + k) * width/(2*k)
            finalendy = (endy + k) * height/(2*k)
            
            line(finalstartx, height - finalstarty, finalendx, height - finalendy)
    
    del mylist[:]
    

def gtVertex(x, y, z):
    
    gtvertex = [x,y,z,1]
    ctm = gtGetMatrix()
    
    result = matrixMult(ctm, gtvertex)
    mylist.append(result)


def matrixMult(a,b):
    result = [0,0,0,0]
    for i in range(len(a)):
        for j in range(len(b)):
            result[i] += a[i][j]*b[j]
    return result
    
    