# -*- coding: utf-8 -*-
# 如果中文字符无法显示， 请换用utf-8编码
"""
Created on Fri Jul 24 03:49:03 2015

@author: Mihawk
"""

import random

points = {"CDEC"    : 31462,
          "Vega"    : 30157,
          "MVP"     : 29431,
          "Archon"  : 23050 }

name = points.keys()
winrate = {}

for i in name:
    winrate[i] = {}
    
for i in name:
    for j in name:
        if i != j:
            winrate[i][j] = points[i]*1.0 / (points[i] + points[j])
        else:
            winrate[i][j] = -1

def gamePlayWin(team1, team2):
    """ 三局两胜 """
    win = 0
    for i in range(3):
        if (random.random() < winrate[team1][team2]):
            win = win + 1
    if win >= 2:
        return True
    else:
        return False
    
def simulate():
    """ "CDEC" vs "Vega" """  
    if (gamePlayWin("CDEC", "Vega")):
        (A1Win, A1Lose)  = ("CDEC", "Vega")
    else:
        (A1Win, A1Lose)  = ("Vega", "CDEC")
    
    """ "MVP" vs "Archon" """
    if (gamePlayWin("MVP", "Archon")):
        (B1Win, B1Lose)  = ("MVP", "Archon")
    else:
        (B1Win, B1Lose)  = ("Archon", "MVP")
    
    """ 胜者组决赛 """
    if (gamePlayWin(A1Win, B1Win)):
        (A2Win, A2Lose)  = (A1Win, B1Win)
    else:
        (A2Win, A2Lose)  = (B1Win, A1Win)
    
    """ 败者组半决赛 """
    if (gamePlayWin(A1Lose, B1Lose)):
        (B2Win, B2Lose)  = (A1Lose, B1Lose)
    else:
        (B2Win, B2Lose)  = (B1Lose, A1Lose)
    
    """ 败者组决赛 """
    if (gamePlayWin(A2Lose, B2Win)):
        (B3Win, B3Lose)  = (A2Lose, B2Win)
    else:
        (B3Win, B3Lose)  = (B2Win, A2Lose)
     
    return "1    " + A2Win +"\n2    " + B3Win + "\n3    " + B3Lose + "\n4    " + B2Lose
    
    """
    # 最后排名 
    print("1    " + A2Win)
    print("2    " + B3Win)
    print("3    " + B3Lose)
    print("4    " + B2Lose)
    """
    
result = {}
for i in range(1000000):
    res = simulate()
    if (result.has_key(res)):
        result[res] = result[res] + 1
    else:
        result[res] = 1

final = sorted(result.items(), key = lambda d:d[1], reverse=True)
for i in range(5):
    print(final[i][0]),
    print(final[i][1])
        

          
          
