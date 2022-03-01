import rubik.cube as rubik

# dev strategy
#    validate prarms
#    load parms['cube'] into cube model
#    rotate cube in desire direction
#    serialize cube model in string
#    return string + status of 'ok'

def _solve(parms):
    #load keys from input parms using getElement form cube.py
    #status already checked from cube.py
    status = rubik.getElement(parms, 'status')
    rotate = rubik.getElement(parms, 'rotate')
    cube = rubik.getElement(parms, 'cube')
    result = {}
    result['status'] = status   
        
    #if status is error only return error
    if (status != 'ok'):
        return result
    
    #if no input rotate value or value is empty, set rotate to default 'F'
    if (rotate == None or rotate == ''):
        rotate = 'F'
    
    #if rotate is invalid, return error
    result['status'] = checkRotate(rotate)
    if (result['status'] != 'ok'):
        return result
    
    cube = rotateCube(rotate, cube)
    #update the cube in first index of result
    finalResult = {'cube': cube}
    finalResult.update(result)          
    return finalResult


#check invalid rotate input
def checkRotate(rotate):
    result = {}
    #not string return error
    if (isinstance(rotate, str) == False):
        result = 'error: Invalid rotation, rotate is not string'
        return result
    #check for rotate error if rotate is not qualified 
    validRotate = ['f','r', 'b', 'l', 'u', 'd']
    for i in range(len(rotate)):
        if rotate[i].lower() not in validRotate:
            result = 'error: Invalid rotation, rotate input contains invalid letters'
            return result
    result = 'ok'
    return result
    
def rotateCube(rotate, cube):
        #loop through list of rotation
    rotateList = list(rotate)
    for step in rotateList:
        #create list to store the rotating color elements
        faceColor = []
        sideColor = []
        direction = 1
        cubeList = list(cube)
        #negative is clockwise, positive is counterclockwise
        if step.isupper():
            direction = -1
            
        #load the specific index decided by the rotate letter
        rotateFace, rotateSide = rubik.getRotationIndex(step)
        
        #get the specific face colors from cube 
        for face in rotateFace:
            faceColor.append(cubeList[face - 1])
        #get the specific side colors from cube     
        for side in rotateSide:
            sideColor.append(cubeList[side - 1])
            
        #rotate the face color in desire direction
        faceColor = faceColor[direction * 2:] + faceColor[:direction * 2]
        #rotate the side in desire direction
        sideColor = sideColor[direction * 3:] + sideColor[:direction * 3]
        
        #put back the rotated color
        for i in range(len(rotateFace)):
            cubeList[rotateFace[i] - 1] = faceColor[i]
        #put back the rotated color
        for i in range(len(rotateSide)):
            cubeList[rotateSide[i] - 1] = sideColor[i]
            
        cube = "".join(cubeList)
    return cube
