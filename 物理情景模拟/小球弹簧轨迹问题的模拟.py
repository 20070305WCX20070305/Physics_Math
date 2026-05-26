#问题描述：小球与弹簧一段相连，弹簧另一端与水平面固定点相连，不计摩擦，模拟小球在水平面上的轨迹方程

import tqdm
import numpy 
import matplotlib.pyplot as plt

#求出微分系数
def zengzhanglv(shuzu: list, a: float, b: float) -> list:
    r, sita, u, v = shuzu[0], shuzu[1], shuzu[2], shuzu[3]
    
    r_zengzhanglv = u
    sita_zengzhanglv = v
    u_zengzhanglv = r * v ** 2 - a * r + b
    v_zengzhanglv = (-2 * u * v) / r
    
    return [r_zengzhanglv, sita_zengzhanglv, u_zengzhanglv, v_zengzhanglv]

#系统能量的处理，l为弹簧原长
def energy_caculation(v_r: float, v_sita: float, r: float, k: float, m: float, l: float) -> list:
    k_energy = m * (v_r ** 2 + (r * v_sita) ** 2) / 2
    p_energy = (k * (r - l) ** 2) / 2
    total_energy = k_energy + p_energy
    return [k_energy, p_energy, total_energy]
    
#画图，轨迹图，能量时间关系图（检验误差)
# m质量，k劲度系数，l原长，time_range时间范围，jingdu精度
#r_0 初始坐标，r_zengzhanglv_0 初始径向速度，sita_zengzhanglv_0 初始角向速度
def shuzhimoni(r_0: float, r_zengzhanglv_0: float, sita_zengzhanglv_0: float, m: float, k: float, l: float, time_range: float, jingdu: int):
    #初始化参数与存储集合
    sita_0 = 0
    u_0 = r_zengzhanglv_0
    v_0 = sita_zengzhanglv_0
    
    a = k / m
    b = k * l / m
    
    delta_time = time_range / jingdu
    time = list()
    for i in tqdm.tqdm(range(0, jingdu)):
        time.append(delta_time * i)
    
    #坐标集合   
    r = [r_0]
    sita = [sita_0]
    u = [u_0]
    v = [v_0]
    
    #系统能量状态集合
    total = list()
    k_energy = list()
    potential = list()
    
    energy = energy_caculation(u_0, v_0, r_0, k, m, l)
    k_energy.append(energy[0])
    potential.append(energy[1])
    total.append(energy[2])
    
    for _ in tqdm.tqdm(range(0, jingdu - 1)):
        #迭代预测
        r_zuobiao = r[-1]
        sita_zuobiao = sita[-1]
        u_zuobiao = u[-1]
        v_zuobiao = v[-1]
        
        zengzhangyuce = zengzhanglv([r_zuobiao, sita_zuobiao, u_zuobiao, v_zuobiao], a, b)
        r_zengzhanglv_1 = zengzhangyuce[0]
        sita_zengzhanglv_1 = zengzhangyuce[1]
        u_zengzhanglv_1 = zengzhangyuce[2]
        v_zengzhanglv_1 = zengzhangyuce[3]
        
        r_yuce = r_zuobiao + delta_time * r_zengzhanglv_1
        sita_yuce = sita_zuobiao + delta_time * sita_zengzhanglv_1
        u_yuce = u_zuobiao + delta_time * u_zengzhanglv_1
        v_yuce = v_zuobiao + delta_time * v_zengzhanglv_1
        
        zengzhangyuce_2 = zengzhanglv([r_yuce, sita_yuce, u_yuce, v_yuce], a, b)
        r_zengzhanglv_2 = zengzhangyuce_2[0]
        sita_zengzhanglv_2 = zengzhangyuce_2[1]
        u_zengzhanglv_2 = zengzhangyuce_2[2]
        v_zengzhanglv_2 = zengzhangyuce_2[3]
        
        r_yuce = r_zuobiao + delta_time * (r_zengzhanglv_1 + r_zengzhanglv_2) / 2
        sita_yuce = sita_zuobiao + delta_time * (sita_zengzhanglv_1 + sita_zengzhanglv_2) / 2
        u_yuce = u_zuobiao + delta_time * (u_zengzhanglv_1 + u_zengzhanglv_2) / 2
        v_yuce = v_zuobiao + delta_time * (v_zengzhanglv_1 + v_zengzhanglv_2) / 2  
        
        r.append(r_yuce)
        sita.append(sita_yuce)
        u.append(u_yuce)
        v.append(v_yuce)
        
        #处理能量
        energy = energy_caculation(u_yuce, v_yuce, r_yuce, k, m, l)  
        k_energy.append(energy[0])
        potential.append(energy[1])
        total.append(energy[2])
        
    x = r * numpy.cos(sita)
    y = r * numpy.sin(sita)
    energy_0 = total[0]
    
    for i in tqdm.tqdm(range(0, len(total))):
        total[i] = total[i] - energy_0
        
    total = numpy.divide(total, energy_0)
        
    
    plt.subplot(2, 3, 1)
    plt.plot(x, y, color = "black")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"y-x motion picture within {time_range}s")
    print("picture-1 completed")
    
    plt.subplot(2, 3, 2)
    plt.plot(time, x, color = "blue")
    plt.plot(time, y, color = "red")
    plt.xlabel("time")
    plt.ylabel("position x and y")
    plt.title("x-t(blue) and y-t(red)")
    print("picture-2 completed")
    
    plt.subplot(2, 3, 3)
    plt.plot(time, u, color = "blue")
    plt.plot(time, v, color = "red")
    plt.xlabel("time")
    plt.ylabel("linear velocity and angle celocity")
    plt.title("linear velocity(blue)-t and angle velocity(red)-t")
    print("picture-3 completed")
    
    plt.subplot(2, 3, 4)
    plt.plot(time, k_energy, color = "blue")
    plt.xlabel("time")
    plt.ylabel("kinetic energy")
    plt.title("relation graph of kinetic energy and time")
    print("picture-4 completed")
    
    plt.subplot(2, 3, 5)
    plt.plot(time, potential, color = "blue")
    plt.xlabel("time")
    plt.ylabel("potential energy")
    plt.title("relation graph of potential energy and time")
    print("picture-5 completed")
    
    #利用总能量的波动大小估计模拟精确度
    plt.subplot(2, 3, 6)
    plt.plot(time, total, color = "red")
    plt.xlabel("time")
    plt.ylabel("accuarcy")
    plt.title("accuarcy - time graph")
    print("picture-6 completed")
    
    plt.show()
    
def main():
    print("the caculation of the system consisting a spring and a ball, sita = 0 at time = 0")
    m = float(input("the mass of the ball: "))
    k = float(input("the stiffness coefficient of the spring: "))
    l = float(input("the length of the spring: "))
    
    r_0 = float(input("the distance at time = 0: "))
    v_r = float(input("v_r(m/s): "))
    v_sita = float(input("v_sita(rad/s):"))
    
    time_range = float(input("the range of the time:"))
    jingdu = int(input("the deisred accuracy(10000000 if input nothing):") or 10000000)
    
    shuzhimoni(r_0, v_r, v_sita, m, k, l, time_range, jingdu)
    
if __name__ == "__main__":
    main()
