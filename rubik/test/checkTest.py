"""
Jan 31, 2022

@author: Luca Dai
"""

from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):

#Analysis
#    _check(parm)
#    
#    inputs:
#        parm:     dictionary, 2 keys, mandatory, unvalidated
#            keys: 
#                'op', string, mandatory, validated
#                'cube',string, 54 characters,
#                       has 9 occurrences of 6 colors,
#                       each middle face has different color,
#                       not having contradictory colors,
#                       mandatory, unvalidated
#    outputs:
#        side-effects:    no state change
#        returns:    dictionary, 1 key, one of the follow:
#                    fail: {'status': 'error: xxx'} or pass: {'status': 'ok'}
#
#    confidence level:    BVA
#
#Happy path
#    test 101:    the 'cube' value of parm is represent a solved cube:
#                 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
#                 result: {'status': 'ok'}
#    test 102:    the 'cube' value of parm is represent an unsolved but perfect cube:
#                 'gybrbgggoobgowwwyboboggryorbbwwygwyyywyorrrbwrygroobwr'
#                 result: {'status': 'ok'}
#    test 103:    the 'cube' value of parm is represent an unsolvable corner rotated cube:
#                 'bbrbbbbbbyrrrrrrrrgggggggggoooooooooyyyyyyyybwwwwwwwww'
#                 result: {'status': 'ok'}
#
#Sad path
#    test 901:    Key 'cube' does not exist: parm = {'op':'check'}
#                 result: {'status': 'error: xxx'}
#    test 902:    Value of cube is not string: 'cube' is integer
#                 result: {'status': 'error: xxx'}
#    test 903:    Bottom case of parm: string length is 0, 'cube' = ''
#                 result: {'status': 'error: xxx'}
#    test 904:    Less than low bound: length of 'cube' is 53
#                 result: {'status': 'error: xxx'}
#    test 905:    Greater than high bound: length of 'cube' is 55
#                 result: {'status': 'error: xxx'}
#    test 906:    Very big value: length of 'cube' is 108
#                 result: {'status': 'error: xxx'}
#    test 907:    Less than low bound: 'cube' only has 5 colors
#                 result: {'status': 'error: xxx'}
#    test 908:    Greater than high bound: 'cube' has 7 colors
#                 result: {'status': 'error: xxx'}
#    test 909:    Beginning of the String： Value of cube has different occurrences of 6 colors: 10 'b's and 8 'r's
#                 result: {'status': 'error: xxx'}
#    test 910:    End of string:： Value of cube has different occurrences of 6 colors: 8 'b's and 10 'w's
#                 result: {'status': 'error: xxx'}
#    test 911:    Beginning of the String： Value of cube has middle face being same color: [r,r,g,o,y,w]
#                 result: {'status': 'error: xxx'}
#    test 912:    End of the String： Value of cube has middle face being same color: [b,r,g,o,y,b] 
#                 result: {'status': 'error: xxx'}
#    test 913:    Edge case: one edge has contradictory color: 
#                 swap position 20 and 44 for solved cube
#                 result: {'status': 'error: xxx'}
#    test 914:    Edge case 2: one edge has contradictory color: 
#                 swap position 13 and 48 for solved cube
#                 result: {'status': 'error: xxx'}
#    test 915:    Edge case: a edge has two side in same color:
#                 switch 6 and 44 for solved cube
#                 result: {'status': 'error: xxx'}
#    test 916:    Corner case: one corner has contradictory color:
#                 swap position 19 and 43 for solved cube
#                 result: {'status': 'error: xxx'}
#    test 917:    Corner case: one corner has contradictory color:
#                 corner for unsolved cube: 27, 34, 52 is y, r, b 
#                 opposite of b is g, therefore switch y to a corner g
#                 result: {'status': 'error: xxx'}
#    test 918:    Corner case: a corner has two side in same color:
#                 switch 30,o and 7,b for solved cube
#                 result: {'status': 'error: xxx'}

    #Happy path tests:
    def test_check_101_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_102_ShouldReturnOkOnUnsolvedCube(self):
        parm = {'op':'check',
                'cube':'gybrbgggoobgowwwyboboggryorbbwwygwyyywyorrrbwrygroobwr'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
    def test_check_103_ShouldReturnOkOnUnsolvedCube(self):
        parm = {'op':'check',
                'cube':'bbrbbbbbbyrrrrrrrrgggggggggoooooooooyyyyyyyybwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
        
    #Sad path tests:    
    def test_check_901_ShouldReturnXxxForCubeNotExist(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_902_ShouldReturnXxxForNotString(self): 
        parm = {'op':'check',
                'cube': 111111111222222222333333333444444444555555555666666666}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_903_ShouldReturnXxxForEmptyString(self): 
        parm = {'op':'check',
                'cube':''}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx') 
        
    def test_check_904_ShouldReturnXxxForCubelengthOf53(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx') 
        
    def test_check_905_ShouldReturnXxxForCubelengthOf55(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx') 
        
    def test_check_906_ShouldReturnXxxForCubelengthOf108(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww\
                        bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx') 
        
    def test_check_907_ShouldReturnXxxFor5ColorCube(self): 
        parm = {'op':'check',
                'cube':'abcdebbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_908_ShouldReturnXxxFor7ColorCube(self): 
        parm = {'op':'check',
                'cube':'abcdefgbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_909_ShouldReturnXxxForOccurrenceNotMatchAtTheBeginning(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_910_ShouldReturnXxxForOccurrenceNotMatchAtTheEnd(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_911_ShouldReturnXxxForFaceColorNotMatchAtTheBeginning(self): 
        parm = {'op':'check',
                'cube':'bbbbrbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')   
        
    def test_check_912_ShouldReturnXxxForFaceColorNotMatchAtTheEnd(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbwrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwbwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
    
    def test_check_913_ShouldReturnXxxForContradictoryEdge(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrrgygggggggoooooooooyyyyyyygywwwwwwwww'}        
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
    def test_check_914_ShouldReturnXxxForContradictoryEdge2(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrwrrrrrgggggggggoooooooooyyyyyyyyywwrwwwwww'}        
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_915_ShouldReturnXxxForSameColorEdge(self): 
        parm = {'op':'check',
                'cube':'bbbbbybbbrrrrrrrrrgggggggggoooooooooyyyyyyybywwwwwwwww'}                       
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx') 
      
    def test_check_916_ShouldReturnXxxForContradictoryCorner(self): 
        parm = {'op':'check',
                'cube':'bbbbbbbbbrrrrrrrrryggggggggoooooooooyyyyyygyywwwwwwwww'}        
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_917_ShouldReturnXxxForContradictoryCorner2(self): 
        parm = {'op':'check',
                'cube':'yobybgggwwbgwrrrobwbwggyowgbbrrogrooorowyyybryogywwbry'}       
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')
        
    def test_check_918_ShouldReturnXxxForSameColorCorner(self): 
        parm = {'op':'check',
                'cube':'bbbbbbobbrrrrrrrrrgggggggggoobooooooyyyyyyyyywwwwwwwww'}   
                            
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: xxx')