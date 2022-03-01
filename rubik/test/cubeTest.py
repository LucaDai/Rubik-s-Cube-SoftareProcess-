"""
Feb 22, 2022

@author: Luca Dai
"""

import unittest
import rubik.cube as cube

class CubeTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

#Analysis: cube
#            method: load
#                    get
#                    get

#Analysis: cube.load(parms)
#    inputs:    parms
#               type: dictionary
#
#    outputs:    type: dictionary
#        side-effects:    none
#        nominal: load values from input
#        abnormal : NA    

#Analysis: cube.get(parms, key)
#    inputs:    parms, string
#                type: dictionary,key
#    outputs:    string
#        side-effects:    none
#        nominal: get variable from load method
#        abnormal : NA       
#
#    confidence level: boundary value analysis

#Analysis: getEdge() - tested in check.py
#    inputs:    none
#    outputs:   array
#        side-effects:    none   
#        nominal: get edge index
#        abnormal : NA  

#Analysis: getCorner() - tested in check.py
#    inputs:    none
#    outputs:   array
#        side-effects:    none   
#        nominal: get corner index
#        abnormal : NA  

#Analysis: getRotationIndex(char) - tested in solve.py
#    inputs:    string
#    outputs:   array
#        side-effects:    none   
#        nominal: get different face and side indexes decided by input letter
#        abnormal : NA 

#Happy path
#    test 001:    load(parms) cube correctly 
#                    
#    test 002:    get 'cube' element from dictionary
#                 result: 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
#    test 003:    get 'rotate' element from dictionary
#                 result: 'R'
#Sad path
#    test 901:    missing cube string
#                 result: error

    def test_init_001_ShouldLoadCube(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult['rotate'] = 'R'
        expectedResult['status'] = 'ok'
        actualResult = cube.load(inputDict)
        self.assertEqual(expectedResult, actualResult)
        
    def test_init_002_ShouldGetCube(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        actualResult = cube.getElement(inputDict, 'cube')
        self.assertEqual(expectedResult, actualResult)
        
    def test_init_003_ShouldGetRotate(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = 'R'
        actualResult = cube.getElement(inputDict, 'rotate')
        self.assertEqual(expectedResult, actualResult)

    def test_init_901_MissingCubeShouldReturnStatusError(self):
        inputDict = {}
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = 'error: xxx'
        actualResult = cube.getElement(inputDict, 'status')
        self.assertEqual(expectedResult, actualResult)
        