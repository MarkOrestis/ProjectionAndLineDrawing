# Matrix Stack Library -- Use your code from Project 1A


# Matrix Stack Library
# Orestis Markozanes
# you should modify the routines below to complete the assignment
stack = []
count = 0

def gtInitialize():
    global count
    count = 0
    del stack[:]
    identityMatrix = [[1,0,0,0],
             [0,1,0,0],
             [0,0,1,0],
             [0,0,0,1]]
    stack.append(identityMatrix)

def gtPushMatrix():
    global count
    temp = gtGetMatrix()
    count += 1
    stack.append(temp)

def gtPopMatrix():
    global count
    if (count == 0):
        print "cannot pop the matrix stack"
    else:
        del stack[-1]
        count -= 1

def gtTranslate(x, y, z):
    global count
    translateMatrix = [[1,0,0,x], 
                       [0,1,0,y], 
                       [0,0,1,z], 
                       [0,0,0,1]]
    result = multiplication4x4(gtGetMatrix(), translateMatrix)
    stack[count] = result

def gtScale(x, y, z):
    global count
    scaledMatrix = [[x,0,0,0],
                    [0,y,0,0],
                    [0,0,z,0],
                    [0,0,0,1]]
    result = multiplication4x4(gtGetMatrix(), scaledMatrix)
    stack[count] = result

def gtRotateX(theta):
    theta = theta*PI/180
    rotateXMatrix = [[1,0,0,0],
                     [0,cos(theta),-sin(theta),0],
                     [0,sin(theta),cos(theta),0],
                     [0,0,0,1]]
    result = multiplication4x4(gtGetMatrix(), rotateXMatrix)
    stack[count] = result

def gtRotateY(theta):
    theta = theta*PI/180
    rotateYMatrix = [[cos(theta),0, sin(theta),0],
                     [0,1,0,0],
                     [-sin(theta),0,cos(theta), 0],
                     [0,0,0,1]]
    result = multiplication4x4(gtGetMatrix(), rotateYMatrix)
    stack[count] = result

def gtRotateZ(theta):
    theta = theta*PI/180
    rotateZMatrix = [[cos(theta),-sin(theta),0,0],
                     [sin(theta),cos(theta),0,0],
                     [0,0,1,0],
                     [0,0,0,1]]
    result = multiplication4x4(gtGetMatrix(), rotateZMatrix)
    stack[count] = result

def gtGetMatrix():
    return stack[count]

def print_ctm():
    temp = gtGetMatrix()
    for i in temp:
        print (i)
    print "\n"

def multiplication4x4(ctm, matrix):
    result = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += ctm[i][k]*matrix[k][j]
    return result
    