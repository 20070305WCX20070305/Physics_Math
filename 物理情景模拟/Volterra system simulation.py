# Volterra system simulation

import math
import numpy
import matplotlib.pyplot as plt
import tqdm

def x_zengzhanglv(x: float, y: float, a: float, b: float) -> float:
    zengzhanglv = (b * y - a) * x
    return zengzhanglv

def y_zengzhanglv(x: float, y: float, c: float, d: float) -> float:
    zengzhanglv = (c - d * x) * y
    return zengzhanglv

def num_caculation(x_0: float, y_0: float, a: float, b: float, c: float, d: float, time_range: float, jingdu: int) -> list:
    time = []
    x = [x_0]
    y = [y_0]
    delta_time = time_range / jingdu
    for i in tqdm.tqdm(range(0, jingdu), desc="初始化时间"):
        time.append(delta_time * i)
        
    for i in tqdm.tqdm(range(0, jingdu - 1), desc= "Processing"):
        x_n = x[-1]
        y_n = y[-1]
        
        x_zengzhanglv_1 = x_zengzhanglv(x_n, y_n, a, b)
        y_zengzhanglv_1 = y_zengzhanglv(x_n, y_n, c, d)
        
        x_zhongjian = x_n + delta_time * x_zengzhanglv_1
        y_zhongjian = y_n + delta_time * y_zengzhanglv_1
        
        x_zengzhanglv_2 = x_zengzhanglv(x_zhongjian, y_zhongjian, a, b)
        y_zengzhanglv_2 = y_zengzhanglv(x_zhongjian, y_zhongjian, c, d)
        
        x_yuce = x_n + delta_time * (x_zengzhanglv_1 + x_zengzhanglv_2) / 2
        y_yuce = y_n + delta_time * (y_zengzhanglv_1 + y_zengzhanglv_2) / 2
        
        x.append(x_yuce)
        y.append(y_yuce)
        
        
    return [x, y, time]

def picture(information: list, x_name: str, y_name: str):
    x, y, time = information[0], information[1], information[2]
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.xlabel(f"the number of {x_name}")
    plt.ylabel(f"the number of {y_name}")
    plt.title("{x_name}-{y_name} population graph")
    
    plt.subplot(1, 2, 2)
    plt.plot(time, x, color = "red")
    plt.plot(time, y, color = "blue")
    plt.xlabel("time")
    plt.ylabel("population")
    plt.title(f"population of {x_name}(red) and {y_name}(blue)")
    
    plt.show()
    
def main():
    print("the simulation of the Volterra system")
    x_name, y_name = input("x_name, y_name: ").split()
    a, b, c, d = map(float, input("a, b, c, d: ").split())
    x_0, y_0 = map(float, input(f"inatial population of {x_name} and {y_name}: ").split())
    time_range = float(input("time range: "))
    jingdu = int(input("the desired accuarcy(50000000 if nothing input): ") or 50000000)
    
    information = num_caculation(x_0, y_0, a, b, c, d, time_range, jingdu)
    picture(information, x_name, y_name)
    
if __name__ == "__main__":
    main()
    