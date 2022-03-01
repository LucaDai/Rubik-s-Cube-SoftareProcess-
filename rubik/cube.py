import rubik.check as check 
'''
Rubik's cube
'''

def __init__(self):
    pass

#load return a dictionary contains cube, rotate and checked status
def load(parms):
    cube = {}
    cube['cube'] = parms.get('cube',None)
    cube['rotate'] = parms.get('rotate',None)
    cube.update(check._check(parms))
    return cube

#get element from load() dictionary   
def getElement(parms, key):
    cube = load(parms)
    return cube.get(key,None)

#edges array: return index number of 12 edges
def getEdge():
    edge = [[2, 44], [4, 33], [6, 13], [8, 47], [11, 42], [15, 22],
                [17, 51], [20, 38], [24, 31], [26, 53], [29, 40], [35, 48]]
    return edge
#corners array: return index number of 12 edges
def getCorner():
    corner = [[1, 30, 43], [3, 10, 45], [7, 36, 46], [9, 16, 48],
                  [12, 19, 39], [18, 25, 54], [21, 37, 28], [27, 34, 52]]
    return corner


#get the face and side index for "char" rotation from top left clockwise
def getRotationIndex(char):
    char = char.lower()
    #first array: face 8 elements
    #second array: side 12 elements
    faceAndSideSwitcher = {
        'f': [[1, 2, 3, 6, 9, 8, 7, 4],
              [43, 44, 45, 10, 13, 16, 48, 47, 46, 36, 33, 30]],
        'r': [[10, 11, 12, 15, 18, 17, 16, 13],
              [45, 42, 39, 19, 22, 25, 54, 51, 48, 9, 6, 3]],
        'b': [[19, 20, 21, 24, 27, 26, 25, 22],
              [39, 38, 37, 28, 31, 34, 52, 53, 54, 18, 15, 12]],
        'l': [[28, 29, 30, 33, 36, 35, 34, 31],
              [37, 40, 43, 1, 4, 7, 46, 49, 52, 27, 24, 21]],
        'u': [[37, 38, 39, 42, 45, 44, 43, 40],
              [21, 20, 19, 12, 11, 10, 3, 2, 1, 30, 29, 28]],
        'd': [[46, 47, 48, 51, 54, 53, 52, 49],
              [7, 8, 9, 16, 17, 18, 25, 26, 27, 34, 35, 36]]
    }
    return faceAndSideSwitcher.get(char);





