"""
Jan 31, 2022

@author: Luca Dai
"""

import rubik.cube as rubik
#Return {'status': 'ok'} if pass all conditions 
#Return {'status': 'error: xxx'} where 'xxx' is an appropriate error message 
def _check(parms):
    result={}
    #Value of cube is present
    encodedCube = parms.get('cube',None) 
    if (encodedCube == None):
        result['status'] = 'error: Missing cube'
        
    #Value of cube is a string
    if not result:
        if (isinstance(encodedCube, str) == False):
            result['status'] = 'error: Invalid cube, cube is not a string'
        
    #Value of cube has 54 elements
    if not result:
        if (len(encodedCube) != 54):
            result['status'] = 'error: Invalid cube, cube length does not match'
    
    if not result:
        for i in range(len(encodedCube)):
            element = encodedCube[i]
            if(element.isdecimal() != True) and (element.isalpha() != True):
                result['status'] = 'error: Invalid cube, cube should only contain digits or alphabets'
                break
    #Value of cube has 9 occurrences of 6 colors
    if not result:
        color_dict = {}
        for element in range(0, len(encodedCube)):
            if (encodedCube[element] in color_dict):
                color_dict[encodedCube[element]] += 1
            else:
                color_dict[encodedCube[element]] = 1
        #Value of cube has of 6 colors
        if (len(color_dict) != 6):
            result['status'] = 'error: Invalid cube, cube colors do not equal to 6'
            return result
        #And each color has 9 characters
        for element in color_dict:
            if (color_dict[element] != 9):
                result['status'] = 'error: Invalid cube, each color elements do not equal to 9' 
                break
            
    #Value of cube has each middle face being a different color
    if not result:
    #Middle face start from number 5(index 4), and increasing 9 every time    
        mid_color = []
        mid_face = 4
        for element in range(6):
            if(encodedCube[mid_face] in mid_color):
                result['status'] = 'error: Invalid cube, face colors are not unique' 
                break 
            mid_color.append(encodedCube[mid_face])
            mid_face += 9   
            
    #Extra: Value of cube does not has contradictory color
    if not result:    
        #Insert index number of 12 edges
        edge = rubik.getEdge()
        #Transfer index in to color
        edge_color = []
        for element in edge:
            ec1 = encodedCube[element[0] - 1]
            ec2 = encodedCube[element[1] - 1]
            edge_color.append([ec1, ec2])
        #Insert index number of 12 edges
        corner = rubik.getCorner()
        #Transfer index in to color
        corner_color = []
        for element in corner:
            cc1 = encodedCube[element[0] - 1]
            cc2 = encodedCube[element[1] - 1]
            cc3 = encodedCube[element[2] - 1]
            corner_color.append([cc1, cc2, cc3])
        #Get all middle face color in a list
        mid_color = []
        mid_face = 4
        for element in range(6):
            mid_color.append(encodedCube[mid_face])
            mid_face += 9
        #list position: cube index
        #1:5, 2:14, 3: 23, 4:32, 5:41, 6:50
        #Face 5 against 23, 14 against 32, 41 against 50
        #In order to use loop, swap position 2 and 3
        #color contradictory: x with x+1
        mid_color[1], mid_color[2] = mid_color[2], mid_color[1]
        #Ready to check the color contradictory
        #Check edges color contradictory
        for element in edge_color:
            if result:
                break
            for x in range(0, 6, 2):
                if result:
                    break
                front = mid_color[x]
                back = mid_color[x+1]
                #same color
                if (element[0] == element[1]):
                    result['status'] = 'error: Invalid cube, cube edges contains same color' 
                #contradictory color
                if (front in element) and (back in element):
                    result['status'] = 'error: Invalid cube, cube edges contains contradictory color' 
                    
        #Check corners color contradictory
        for element in corner_color:
            if result:
                break
            for x in range(0, 6, 2):
                if result:
                    break
                front = mid_color[x]
                back = mid_color[x+1]
                #same color
                if (element[0] == element[1]) or (element[0] == element[2]) or (element[1] == element[2]):
                    result['status'] = 'error: Invalid cube, cube corners contains same color'  
                #contradictory color
                if (front in element) and (back in element):
                    result['status'] = 'error: Invalid cube, cube corners contains contradictory color' 
                
                
    #The cube string fits all conditions
    if not result:
        result['status'] = 'ok'
    return result
