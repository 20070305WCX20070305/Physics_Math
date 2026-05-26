
#程序有模拟精度问题，经检验，k = 1,3,5,7,9,11，13模拟精度均可以满足要求，而对于k = 15, 17在x_upper 
#为5时模拟容易发散，但能看出函数走势，建议在该范围内调整x_upper变大，但不要超过10，不建议模拟较大的k
#（大于13）

import matplotlib.pyplot as plt
import numpy as np
import math
import tqdm

def erjiedao(x: float, y: float, k: float) -> float:
    answer = (x ** 2 - k) * y
    return answer

def panduan(k: float):
    if int(k) == k:
        if ((k - 1) // 2) % 2 == 1:
            return [0, 1]
        
        else:
            return [1, 0]
        
    else:
        return [1, 0]
    
#二阶龙格库塔法有问题，精度不够，模拟区间不能太大，容易发散，k较大时建议修正为四阶龙格库塔方法
def shuzhijie(k: float, jingdu: int, x_upper) -> list:
    delta_x = x_upper / jingdu
    
    x_0 = 0
    y_0, y_0_dev = panduan(k)
    
    x_left = list()
    y_left = list()
    y_dev_left = list()
    
    x_left.append(x_0)
    y_left.append(y_0)
    y_dev_left.append(y_0_dev)
    
    for i in tqdm.tqdm(range(0, jingdu), desc = "数值模拟left part:", leave = False):
        x = x_left[-1]
        y = y_left[-1]
        y_dev = y_dev_left[-1]
        
        y_dev2_1 = erjiedao(x, y, k)
        
        x_1 = x - delta_x 
        y_1 = y_dev * (-delta_x) + y
        
        y_dev2_2 = erjiedao(x_1, y_1, k)
        
        y_dev_end = y_dev - delta_x * (y_dev2_1 + y_dev2_2) / 2
        y_end = y - delta_x * y_dev_end   
        
        x_left.append(x_1)
        y_left.append(y_end)
        y_dev_left.append(y_dev_end)
        
        
    x_right = list()
    y_right = list()
    y_dev_right = list()
    
    x_right.append(x_0)
    y_right.append(y_0)
    y_dev_right.append(y_0_dev)
    
    for i in tqdm.tqdm(range(0, jingdu), desc = "数值模拟right part:", leave = False):
        x = x_right[-1]
        y = y_right[-1]
        y_dev = y_dev_right[-1]
        
        y_dev2_1 = erjiedao(x, y, k)
        
        x_1 = x + delta_x 
        y_1 = y_dev * (delta_x) + y
        
        y_dev2_2 = erjiedao(x_1, y_1, k)
        
        y_dev_end = y_dev + delta_x * (y_dev2_1 + y_dev2_2) / 2
        y_end = y + delta_x * y_dev_end   
        
        x_right.append(x_1)
        y_right.append(y_end)
        y_dev_right.append(y_dev_end)
        
    x_zuobiao = np.array(x_left[:0:-1] + x_right)
    y_zuobiao = np.array(y_left[:0:-1] + y_right)
    y_pingfang = y_zuobiao ** 2
    
    
    print("数值模拟已完成！")
    
    return [x_zuobiao, y_zuobiao, k, y_pingfang]

def picture(shujuzu: list):
    if len(shujuzu) > 6:
        print("数据过多！")
        
    else:
        determine = {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [2, 2], 5: [2, 3], 6: [2, 3]}
        a, b = determine[len(shujuzu)]
        for i in range(0, len(shujuzu)):
            x_zuobiao = shujuzu[i][0]
            y_zuobiao = shujuzu[i][1]
            y_pingfang = shujuzu[i][3]
            
            plt.subplot(a, b, i + 1)
            plt.plot(x_zuobiao, y_zuobiao, color = "red")
            plt.plot(x_zuobiao, y_pingfang, color = "blue")
            plt.grid(True)
            plt.title(f"K = {shujuzu[i][2]}")
            
            print(f"{i + 1}-picture finished!")
               
        plt.show()
        
def main():
    value_k = list(map(float, input().split()))
    x_upper = 5
    jingdu = 5000000
    shujuzu = list()
    
    for i in tqdm.tqdm(range(len(value_k)), leave = False):
        shujuzu.append(shuzhijie(value_k[i], jingdu, x_upper))
        
    picture(shujuzu) 
    
if __name__ == "__main__":
    main()