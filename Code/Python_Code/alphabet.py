'''
File Name:alphabet.py
Funtions:character
Global Variable:
                    
'''
'''
Function Name:character
Input:k(ascii value of key pressed),path(list),goal(lsit)
Output:goal,path
Logic:predefined path points 
Example Call:
'''
def character(k,goal,path):

    #goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

    if k==101: #  e
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path= [(237, 160), (350, 179), (419, 132), (370, 69), (278, 79), (255, 273), (347, 296), (434, 279)]


    if k==65:
        #  A
        #path=[(272, 96), (211, 182), (343, 178), (176, 264), (372, 261), (151, 329), (405, 336), (272, 259)]#[(190, 284), (269, 67), (357, 285), (314, 176), (221, 177)]
        x=0# x offset
        y=0 #y ofsett
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(306+x, 42+y), (250+x, 130+y), (214+x, 193+y), (183+x, 263+y), (362+x, 129+y), (398+x, 198+y), (429+x, 266+y),(304+x, 196+y)]
    if k==90:#Z
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(193, 113), (314, 111), (433, 108), (366, 186), (282, 245), (193, 310), (317, 312), (439, 316)]
    if k==78:#N
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(213, 318), (216, 197), (219, 88), (419, 87), (416, 199), (418, 320), (280, 160), (345, 241)]
    if k==89: #Y
        y=30
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(174, 37+y), (236, 96+y), (292, 147+y), (346, 93+y), (387, 30+y), (239, 212+y), (194, 269+y), (147, 324+y)]
        #[(199, 89), (440, 85), (334, 203), (244, 295), (176, 364)]
    if k==69: #E
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(231, 76), (385, 74), (233, 187), (311, 186), (233, 297), (398, 301), (317, 299), (312, 74)]
    if k==73:#I
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(198, 60), (310, 61), (407, 61), (309, 125), (309, 212), (309, 277), (407, 278), (192, 276)]
    if k==79:#O
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(302, 48), (307, 296), (458, 165), (166, 168), (195, 74), (420, 72), (416, 280), (190, 262)]
    if k==85:#U
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(235, 201), (438, 202), (304, 251), (384, 250), (434, 118), (430, 30), (238, 120), (237, 34)]        
    if k==84: #T
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(310, 62), (407, 62), (493, 63), (215, 63), (126, 64), (311, 144), (313, 226), (315, 300)]
    if k==82:#R
        goal=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        path=[(350, 134), (351, 228), (262, 182), (267, 288), (406, 289), (398, 93), (347, 44), (268, 43)]
        






    return goal,path
    
