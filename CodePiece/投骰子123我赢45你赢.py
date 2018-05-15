"""
一个骰子，123我赢，45你赢，6重投，我赢的概率是多大
"""
import random

def getWinNum():
    this_result = random.randint(1,60)
    if this_result in [1,2,3]:
        return 0
    elif this_result in [4,5]:
        return 1
    else:
        return getWinNum()

print(getWinNum())

a_win = 0
b_win = 0

game_times = 100000



for _ in range(game_times):
    result = getWinNum()
    #print(result)
    if result == 0:
        a_win += 1
    else:
        b_win += 1
print(a_win/game_times, b_win/game_times)

'''
Result:
#10             0.6 0.4  
#100            0.63 0.37
#1000           0.594 0.406
#10000          0.5922 0.4078
#100000         0.60032 0.39968

结论: 3/5

额外测试：把随机范围由1-6调整到1-60，结果也一样
'''
