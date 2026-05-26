import numpy as np
import matplotlib.pyplot as plt
import tqdm
import math


def x_bianhualv(x, y, z, a, b, r):
    return a * (y - x)

def y_bianhualv(x, y, z, a, b, r):
    return r * x - y - x * z

def z_bianhualv(x, y, z, a, b, r):
    return x * y - b * z


def huatu(x_0: float, y_0: float, z_0: float, a: float, b: float, r: float, time_range: float, jingdu: float):
    x_zuobiao = list()
    y_zuobiao = list()
    z_zuobiao = list()
    
    x_zuobiao.append(x_0)
    y_zuobiao.append(y_0)
    z_zuobiao.append(z_0)
    
    time = []
    delta_time = time_range / jingdu
    for i in tqdm.tqdm(range(jingdu)):
        time.append(i * delta_time)
        
    for i in tqdm.tqdm(range(jingdu - 1)):
        x = x_zuobiao[-1]
        y = y_zuobiao[-1]
        z = z_zuobiao[-1]
        
        kx1 = x_bianhualv(x, y, z, a, b, r)
        ky1 = y_bianhualv(x, y, z, a, b, r)
        kz1 = z_bianhualv(x, y, z, a ,b ,r)
        
        x1 = x + kx1 * delta_time
        y1 = y + ky1 * delta_time
        z1 = z + kz1 * delta_time
        
        kx2 = x_bianhualv(x1, y1, z1, a, b, r)
        ky2 = y_bianhualv(x1, y1, z1, a, b, r)
        kz2 = z_bianhualv(x1, y1, z1, a ,b ,r)
        
        x2 = x + delta_time * (kx1 + kx2) / 2
        y2 = y + delta_time * (ky1 + ky2) / 2
        z2 = z + delta_time * (kz1 + kz2) / 2
        
        x_zuobiao.append(x2)
        y_zuobiao.append(y2)
        z_zuobiao.append(z2)
    
    plt.subplot(2, 2, 1)    
    plt.plot(x_zuobiao, y_zuobiao)
    plt.title("x-y")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.subplot(2, 2, 2)    
    plt.plot(x_zuobiao, z_zuobiao)
    plt.title("x-z")
    plt.xlabel("x")
    plt.ylabel("z")
    
    plt.subplot(2, 2, 3)
    plt.plot(y_zuobiao, z_zuobiao)
    plt.title("y-z")
    plt.xlabel("y")
    plt.ylabel("z")
    
    plt.show()
    
def main():
    print("洛伦茨方程：数值计算")
    x0, y0, z0 = map(float, input("初始坐标 （x, y, z）：").split())
    a, b, r = map(float, input("参数a, b, r：").split())
    time_range = float(input("模拟时间范围："))
    jingdu = input("精度（默认10000000）：") or 10000000
    jingdu = int(jingdu)
    huatu(x0, y0, z0, a, b, r, time_range, jingdu)
    
if __name__ == "__main__":
    main()
    
        
        