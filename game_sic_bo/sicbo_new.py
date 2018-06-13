# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:27:06 2018

@author: LUMI
"""


import numpy as np
import matplotlib.pyplot as plt  
import itertools



def cumsum(L):
    #if L's length is equal to 1
    if L[:-1] == []:
        return L
        
    ret = cumsum(L[:-1])
    ret.append(ret[-1] + L[-1])
    return ret






chips = 0    # 闲家的筹码量初始值设置
#spend_chips = 0
money_ALL = []   # 每局的盈亏金额 = 庄家的筹码量
money_accum_ALL = []
ROUND_ALL = []

for ii in range(1,11):

    money = []   # 每局的盈亏金额 = 庄家的筹码量
    money_accum = []
    ROUND = []

    for i in range(1,801):
        
        
        # 假设每轮的赔率都是固定不变的 要变化的话就自动设置
        
        ROUND.append(i)
        
        #-----------------------------------------------------
        #闲家买柱
        #-----------------------------------------------------
        #chips = chips + 10000       # 累计增加筹码
        chips = 10000                # 每次都只有10000筹码
        
    #   rest_chips = chips - spend_chips
        
        
        
        # 买大小
        is_buy = np.random.randint(0,2)
        chips_big_small = np.random.randint(0,chips+1) * is_buy
        odds_big_small = 1                                       # 赔率设置
        
        if chips_big_small > 0:
            guess_big_small = np.random.randint(0,2)             # 0:猜小  1:猜大
        
        
        # 买单双
        is_buy = np.random.randint(0,2)
        chips_odd_even = np.random.randint(0,chips-chips_big_small+1) * is_buy
        odds_odd_even = 1                                        # 赔率设置
        
        if chips_odd_even > 0:
            guess_odd_even = np.random.randint(0,2)              # 0:猜双  1:猜单
        
        
        
        #买三个一样数字（任意三个一样就行）
        is_buy = np.random.randint(0,2)
        chips_num = np.random.randint(0,chips-chips_big_small-chips_odd_even+1) * is_buy
        if chips_num > 0:
            guess_A = np.random.randint(1,7)
            guess_B = guess_A
            guess_C = guess_A
            
        #买 1 1 1
        is_buy = np.random.randint(0,2)
        chips_num_1 = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num+1) * is_buy
        if chips_num_1 > 0:
            guess_A = 1
            guess_B = guess_A
            guess_C = guess_A
        
        
        #买 2 2 2
        is_buy = np.random.randint(0,2)
        chips_num_2 = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num-chips_num_1+1) * is_buy
        if chips_num_2 > 0:
            guess_A = 2
            guess_B = guess_A
            guess_C = guess_A
        
        #买 3 3 3
        is_buy = np.random.randint(0,2)
        chips_num_3 = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num-chips_num_1-chips_num_2+1) * is_buy
        if chips_num_3 > 0:
            guess_A = 3
            guess_B = guess_A
            guess_C = guess_A
        
        #买 4 4 4
        is_buy = np.random.randint(0,2)
        chips_num_4 = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num-chips_num_1-chips_num_2-chips_num_3+1) * is_buy
        if chips_num_4 > 0:
            guess_A = 4
            guess_B = guess_A
            guess_C = guess_A
            
        #买 5 5 5
        is_buy = np.random.randint(0,2)
        chips_num_5 = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num-chips_num_1-chips_num_2-chips_num_3-chips_num_4+1) * is_buy
        if chips_num_5 > 0:
            guess_A = 5
            guess_B = guess_A
            guess_C = guess_A
        
        #买 6 6 6
        is_buy = np.random.randint(0,2)
        chips_num_6 = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num-chips_num_1-chips_num_2-chips_num_3-chips_num_4-chips_num_5+1) * is_buy
        if chips_num_6 > 0:
            guess_A = 6
            guess_B = guess_A
            guess_C = guess_A
        
        # 买总和数
        is_buy = np.random.randint(0,2)
        chips_sum_num = np.random.randint(0,chips-chips_big_small-chips_odd_even-chips_num-chips_num_1-chips_num_2-chips_num_3-chips_num_4-chips_num_5-chips_num_6+1) * is_buy
        
        if chips_sum_num > 0:
            guess_sum_num = np.random.randint(4,18)
            
            if guess_sum_num in [4,17]:                          # 赔率设置
                odds_sum_num = 50
            elif guess_sum_num in [5,16]:
                odds_sum_num = 18
            elif guess_sum_num in [6,15]:
                odds_sum_num = 14
            elif guess_sum_num in [7,14]:
                odds_sum_num = 12
            elif guess_sum_num in [8,13]:
                odds_sum_num = 8
            elif guess_sum_num in [9,10,11,12]:
                odds_sum_num = 6
        
        # 全围
        
        
        
        #-----------------------------------------------------
        # 开局
        #-----------------------------------------------------
        A = np.random.randint(1,7)
        B = np.random.randint(1,7)
        C = np.random.randint(1,7)
        
        
        #-----------------------------------------------------
        # 检验结果
        #-----------------------------------------------------
    
        money_sum_num = 0
        money_num = 0
        money_big_small = 0 
        money_odd_even = 0
        kill_money = 0
    
    
    
        # 通杀情况1
        if chips_sum_num > 0:
    
            result_sum_num = A+B+C
            
            if A == B & B == C:                                               # 通杀情况下
                if guess_sum_num == result_sum_num & guess_sum_num not in [3,18]:            # 闲家猜对了
                    money_sum_num = -(chips_sum_num * 24)
                else:                                                                        # 猜错了 
                    kill_money = chips                                       # 通杀，完毕
                              
                    
        # 通杀情况2            
        elif chips_num > 0:
            if A == B & B == C:                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num * 24)
               # else:
                    #kill_money = chips
        
        elif chips_num_1 > 0:
            if A == B & B == C & B == 1 :                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num_1 * 150)
                else:
                    kill_money = chips            
                  
        elif chips_num_2 > 0:
            if A == B & B == C & B == 2 :                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num_1 * 150)
                else:
                    kill_money = chips 
        elif chips_num_3 > 0:
            if A == B & B == C & B == 3 :                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num_1 * 150)
                else:
                    kill_money = chips 
        elif chips_num_4 > 0:
            if A == B & B == C & B == 4  :                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num_1 * 150)
                else:
                    kill_money = chips 
        elif chips_num_5 > 0:
            if A == B & B == C & B == 5 :                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num_1 * 150)
                else:
                    kill_money = chips 
        
        elif chips_num_6 > 0:
            if A == B & B == C & B == 6 :                                           # 通杀情况下
                if guess_A == A:                                                            # 闲家猜中
                    money_num = -(chips_num_1 * 150)
                else:
                    kill_money = chips 
       
                    
                    
        # 买总和数   
        if chips_sum_num > 0:   
            
            if not (A == B & B == C):
                if guess_sum_num == result_sum_num:                             #如果猜中了
                    money_sum_num = -(chips_sum_num*odds_sum_num)
                else:
                    money_sum_num = chips_sum_num
        
                
                    
    
        
        # 买大小
        
        if chips_big_small > 0:
            if A+B+C in list(range(1,11)):
                result_big_small = 0  #结果为 小
            else:
                result_big_small = 1
                
            if guess_big_small == result_big_small:                               # 如果猜对了
                money_big_small = -(chips_big_small*odds_big_small)               # 庄家给相应的钱
            else:
                money_big_small = chips_big_small
        
        # 买单双
        
        if chips_odd_even > 0:
            if (A+B+C)%2 == 1:     # 结果为 单
                result_odd_even = 1
            else:
                result_odd_even = 0
            
            if guess_odd_even == result_odd_even:
                money_odd_even = -(chips_odd_even*odds_odd_even)
            else:
                money_odd_even = chips_odd_even           
                
        
        
        #-----------------------------------------------------
        # 收钱/给钱
        #-----------------------------------------------------
    #    spend_chips = chips_big_small + chips_odd_even + chips_sum_num
        
        if kill_money == chips:
            money.append(kill_money)
        else:
            money.append(money_big_small + money_odd_even + money_sum_num)
            
    money_ALL.append(money)
        
    money_accum = cumsum(money)
    money_accum_ALL.append(money_accum)
    
    ROUND_ALL.append(ROUND)
    
#    plt.bar(ROUND,money)  
#    plt.show() 
#    plt.bar(ROUND,money_accum)  
#    plt.show() 
#    print(money)

        
        
        
money_ALL = list(itertools.chain.from_iterable(money_ALL))
money_accum_ALL = list(itertools.chain.from_iterable(money_accum_ALL))
ROUND_ALL = list(itertools.chain.from_iterable(ROUND_ALL))
ROUND_ALL = list(range(1,len(ROUND_ALL)+1))

plt.bar(ROUND_ALL,money_ALL)  
plt.show() 
plt.bar(ROUND_ALL,money_accum_ALL)  
plt.show() 
    

