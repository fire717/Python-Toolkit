import random
import numpy as np

class Trader(object):
    """docstring for ClassName"""
    def __init__(self, init_money):
        super(Trader, self).__init__()
        self.money = init_money
            
        self.strat_trade_money = 1
        self.this_round_pay = self.strat_trade_money
        #self.trade_money
        self.this_round_money = 0 #记录当轮策略累积收益

    def trade_money(self, get_money):
        this_round_result = get_money-self.this_round_pay
        if this_round_result>0:
            self.this_round_money = 0
            return  self.strat_trade_money
        else:
            self.this_round_money = (-this_round_result)*2+1
            return self.this_round_money

    def pay(self, money):
        self.money -= money 

        if self.money <=0:
            print("Breakout!!!")

    def get(self, money):
        assert money>=0
        self.money += money

    def trade_once(self):
        
        self.pay(self.this_round_pay)
        get_money = half_machine(self.this_round_pay)
        #print(self.this_round_pay, self.this_round_money,get_money, self.money)
        self.get(get_money)
        #print( self.money)
        self.this_round_pay = self.trade_money(get_money)



def half_machine(money):
    if random.random()<=0.5:
        return money*2
    else:
        return 0


def trade(trader, trade_count):


    money_result = []
    for i in range(trade_count):
        if trader.money<=0:
            continue
        trader.trade_once()
        #print("Time %d: %d" % (i,trader.money))
        money_result.append(trader.money)

    print("Max:%d, min:%d, final:%d" % (np.max(money_result),np.min(money_result),trader.money))
    return trader.money

if __name__ == '__main__':
    start_money = 100000
    trade_count = 10000
    test_count = 1000

    print("Start trade, init money is %d, trade_count is %d" % (start_money, trade_count))
    win = 0 
    lose = 0
    for i in range(test_count):
        trader = Trader(start_money)
        last_money = trade(trader, trade_count)
        if last_money>=start_money:
            win+=1
        else:
            lose+=1
    print("win:%d lose:%d" % (win, lose))

