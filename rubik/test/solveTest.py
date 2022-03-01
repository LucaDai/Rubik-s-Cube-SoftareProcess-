"""
Feb 17, 2022

@author: Luca Dai
"""

from unittest import TestCase
import rubik.solve as solve 
import unittest

class SolveTest(TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

#Analysis
#    solve(parms)
#    
#    inputs:
#        parms:     dictionary, mandatory, arrives validated

#        parms['op']:    string, "solve"; mandatory; arrives validated

#        parms['cube']:    string, len = 54, [azAZ09], has 9 occurrences of 6 colors,
#                           each middle face has different color,
#                           not having contradictory colors,
#                           mandatory, arrives unvalidated

#        parms['rotate']:    string, len >= 0, [FfRrBbLlUuDd]; optional, default to F is missing;
#                            arrives unvalidated
#    outputs:
#        side-effects:    no state change; no external effects
#        returns: dictionary
#        nominal:
#                dictionary['cube'] : string, len = 54
#                dictionary['status'] : 'ok'
#        abnormal:
#                dictionary['status'] : 'error: xxx' where xxx is a dev-selected message
#
#    confidence level: boundary value analysis

#Analysis: checkRotate(rotate) 
#    inputs:    string
#    outputs:   array
#        side-effects:    none   
#        nominal: get different face and side indexes decided by input letter
#        abnormal : NA 

#Analysis: rotateCube(rotate, cube) 
#    inputs:    string, string
#    outputs:   string
#        side-effects:    none   
#        nominal: following rotate command, step by step to rotate the cube
#        abnormal : the result of cube might be incorrect
#Happy path
#    test 001:    nominal cube with R rotation, side test, clockwise
#                 result: {'cube': 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb', 'status': 'ok'}
#    test 002:    nominal cube with 'Rr' rotation, should return original cube, direction test
#                 result: {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'status': 'ok'}
#    test 003:    nominal cube with missing rotation, default to F
#                 result: {'cube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 'status': 'ok'}
#    test 004:    nominal cube with "" rotation, default to F
#                 result: {'cube': 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy', 'status': 'ok'}
#    test 005:    nominal cube with 'FfRrBbLlUuDd' rotation, should return original cube, all direction test
#                 result: {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'status': 'ok'}
#    test 006:    nominal cube with 'B' rotation, side test
#                 result: {'cube': 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo', 'status': 'ok'}
#    test 007:    nominal cube with 'L' rotation, side test
#                 result: {'cube': 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy', 'status': 'ok'}
#    test 008:    nominal cube with 'U' rotation, side test
#                 result: {'cube': 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy', 'status': 'ok'}
#    test 009:    nominal cube with 'D' rotation, side test
#                 result: {'cube': 'ggggggooorrrrrrgggbbbbbbrrroooooobbbwwwwwwwwwyyyyyyyyy', 'status': 'ok'}
#    test 010:    nominal unsolved cube with 'FLFFBUUdLfDrFLdRRdLLdRRu' rotation, should return solved cube
#                         test all face and side rotation, and all direction
#                 result: {'cube': 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy', 'status': 'ok'}
#    test 011:    nominal cube with r rotation, side test, counterclockwise
#                 result: {'cube': 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg', 'status': 'ok'}
#Sad path : 
#    test 901:    missing cube
#                 (since check.py is used to qualify the cube string.
#                  I only test it once, to see the check.py works )
#                 result: {'status': 'error: xxx'}
#    test 902:    nominal cube with abnormal rotation, rotate is digits
#                 result: {'status': 'error: xxx'}
#    test 903:    nominal cube with abnormal rotation, rotate contains other letters, 'frRBq'
#                 result: {'status': 'error: xxx'}
#    test 904:    Invalid rotate elements, 'R r'
#                 result: {'status': 'error: xxx'}



    def test_solve_001_SouldRotateValidNominalCubeR(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_solve_002_SouldRotateValidNominalCubeRr(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'Rr'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
    def test_solve_003_SouldReturnOriginalCubeSinceRotateNotExist(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_solve_004_SouldReturnOriginalCubeSinceRotateIsEmpty(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['op'] = 'solve'
        inputDict['rotate'] = ''
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solve_005_SouldRotateValidNominalCubeFfRrBbLlUuDd(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'FfRrBbLlUuDd'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solve_006_SouldRotateValidNominalCubeB(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'B'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_007_SouldRotateValidNominalCubeL(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'L'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'wggwggwggrrrrrrrrrbbybbybbyooooooooobwwbwwbwwgyygyygyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult, actualResult)
       
    def test_solve_008_SouldRotateValidNominalCubeU(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'U'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'rrrggggggbbbrrrrrrooobbbbbbgggoooooowwwwwwwwwyyyyyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_009_SouldRotateValidNominalCubeD(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'D'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'ggggggooorrrrrrgggbbbbbbrrroooooobbbwwwwwwwwwyyyyyyyyy'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult, actualResult)
       
    def test_solve_010_SouldRotateValidNominalCubeFfRrBbLlUuDd(self):
        inputDict = {}
        inputDict['cube'] = 'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
        inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult, actualResult)
    
    def test_solve_011_SouldRotateValidNominalCuber(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'r'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 'ggwggwggwrrrrrrrrrybbybbybbooooooooowwbwwbwwbyygyygyyg'
        expectedResult['status'] = 'ok'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
        
    def test_solve_901_MissingCubeShouldReturnError(self):
        inputDict = {}
        inputDict['cube'] = ''
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid cube, cube length does not match'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_solve_902_AbnormalRotateMessageShouldReturnError_digits(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 123
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid rotation, rotate is not string'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solve_903_AbnormalRotateMessageShouldReturnError_unvalidLetter(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'frRBq'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid rotation, rotate input contains invalid letters'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)
        
        
    def test_solve_903_AbnormalRotateMessageShouldReturnError_unvalidElement(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'R r'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['status'] = 'error: Invalid rotation, rotate input contains invalid letters'
        
        actualResult = solve._solve(inputDict)
        
        self.assertEqual(expectedResult, actualResult)