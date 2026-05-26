# three body problem

import math
import tqdm
import numpy
import matplotlib.pyplot as plt


def mass_central(body01: list, body02: list, body03: list):
    x0 = (body01[0] * body01[4] + body02[0] * body02[4] + body03[0] * body03[4]) / (body01[4] + body02[4] + body03[4])
    y0 = (body01[1] * body01[4] + body02[1] * body02[4] + body03[1] * body03[4]) / (body01[4] + body02[4] + body03[4])
    vx0 = (body01[2] * body01[4] + body02[2] * body02[4] + body03[2] * body03[4]) / (body01[4] + body02[4] + body03[4])
    vy0 = (body01[3] * body01[4] + body02[3] * body02[4] + body03[3] * body03[4]) / (body01[4] + body02[4] + body03[4])
    
    body01[0] = body01[0] - x0
    body02[0] = body02[0] - x0
    body03[0] = body03[0] - x0
    
    body01[1] = body01[1] - y0
    body02[1] = body02[1] - y0
    body03[1] = body03[1] - y0
    
    body01[2] = body01[2] - vx0
    body02[2] = body02[2] - vx0
    body03[2] = body03[2] - vx0
    
    body01[3] = body01[3] - vy0
    body02[3] = body02[3] - vy0
    body03[3] = body03[3] - vy0
    print("初始化完毕！系统切换为质心系")
    
def sys_energy(body01: list, body02: list, body03: list) -> float:
    #万有引力常数G取为1
    m1 = body01[-1]
    m2 = body02[-1]
    m3 = body03[-1]
    
    ke1 = (body01[2] ** 2 + body01[3] ** 2) * body01[4] / 2 
    ke2 = (body02[2] ** 2 + body02[3] ** 2) * body02[4] / 2 
    ke3 = (body03[2] ** 2 + body03[3] ** 2) * body03[4] / 2
    kinetic_energy = ke1 + ke2 + ke3
    
    r12 = math.sqrt((body01[0] - body02[0]) ** 2 + (body01[1] - body02[1]) ** 2)
    r23 = math.sqrt((body02[0] - body03[0]) ** 2 + (body02[1] - body03[1]) ** 2)
    r31 = math.sqrt((body03[0] - body01[0]) ** 2 + (body03[1] - body01[1]) ** 2)
    
    pe12 = -m1 * m2 / r12
    pe23 = -m2 * m3 / r23
    pe31 = -m3 * m1 / r31
    potential_energy = pe12 + pe23 + pe31
    
    total_energy = kinetic_energy + potential_energy
    return total_energy

def angle_momentum(body01: list, body02: list, body03: list) -> float:

    def one_body(numbers: list) -> float:
        x, y, vx, vy, m = numbers
        return m * (x * vy - y * vx)
    
    l = one_body(body01) + one_body(body02) + one_body(body03)
    return l

def linear_momentum(body01: list, body02: list, body03: list) -> list:
    def onebody(numbers: list) -> list:
        px = numbers[-1] * numbers[2]
        py = numbers[-1] * numbers[3]
        return [px, py]
    
    px1, py1 = onebody(body01)
    px2, py2 = onebody(body02)
    px3, py3 = onebody(body03)
    
    px = px1 + px2 + px3
    py = py1 + py2 + py3
    
    return [px, py]

def acceleration(tar_body: list, body1: list, body2: list) -> list:
    x, y, vx, vy, m = tar_body
    x1, y1, m1 = body1[0], body1[1], body1[-1]
    x2, y2, m2 = body2[0], body2[1], body2[-1]
    
    ax = m1 * (x1 - x) / (((x1 - x) ** 2 + (y1 - y) ** 2) ** 1.5) + m2 * (x2 - x) / (((x2 - x) ** 2 + (y2 - y) ** 2) ** 1.5)
    ay = m1 * (y1 - y) / (((x1 - x) ** 2 + (y1 - y) ** 2) ** 1.5) + m2 * (y2 - y) / (((x2 - x) ** 2 + (y2 - y) ** 2) ** 1.5)
    
    return [vx, vy, ax, ay]

    
def three_body(body1_0: list, body2_0: list, body3_0: list, time_range: float, jingdu: int):
    #运动学参量初始化
    x1 = [body1_0[0]]
    y1 = [body1_0[1]]
    vx1 = [body1_0[2]]
    vy1 = [body1_0[3]]
    
    x2 = [body2_0[0]]
    y2 = [body2_0[1]]
    vx2 = [body2_0[2]]
    vy2 = [body2_0[3]]
    
    x3 = [body3_0[0]]
    y3 = [body3_0[1]]
    vx3 = [body3_0[2]]
    vy3 = [body3_0[3]]
    
    #质量
    m1, m2, m3 = body1_0[-1], body2_0[-1], body3_0[-1]
    
    #守恒量初始化
    angle_mom = [angle_momentum(body1_0, body2_0, body3_0)]
    energy = [sys_energy(body1_0, body2_0, body3_0)]
    
    #时间初始化
    delta_time = time_range / jingdu
    time = list()
    for i in tqdm.tqdm(range(0, jingdu), desc = "时间初始化"):
        time.append(i * delta_time)
        
    for i in tqdm.tqdm(range(0, jingdu - 1), desc = "数值模拟"):
        body1_x = x1[-1]
        body1_y = y1[-1]
        body1_vx = vx1[-1]
        body1_vy = vy1[-1]
        
        body2_x = x2[-1]
        body2_y = y2[-1]
        body2_vx = vx2[-1]
        body2_vy = vy2[-1]
        
        body3_x = x3[-1]
        body3_y = y3[-1]
        body3_vx = vx3[-1]
        body3_vy = vy3[-1]
        
        try:
            # 四阶龙格库塔法迭代
            body1 = [body1_x, body1_y, body1_vx, body1_vy, m1]
            body2 = [body2_x, body2_y, body2_vx, body2_vy, m2]
            body3 = [body3_x, body3_y, body3_vx, body3_vy, m3]
            body = [body1.copy(), body2.copy(), body3.copy()]
            
            k_1_1 = acceleration(body1, body2, body3)
            k_2_1 = acceleration(body2, body1, body3)
            k_3_1 = acceleration(body3, body2, body1)
            k_i_1 = [k_1_1, k_2_1, k_3_1]
            
            for i in range(0, 3):
                for j in range(0, 4):
                    body[i][j] = body[i][j] + delta_time * k_i_1[i][j] / 2
                    
            k_1_2 = acceleration(body[0], body[1], body[2])
            k_2_2 = acceleration(body[1], body[0], body[2])
            k_3_2 = acceleration(body[2], body[1], body[0])
            k_i_2 = [k_1_2, k_2_2, k_3_2]
            
            body = [body1.copy(), body2.copy(), body3.copy()]
            for i in range(0, 3):
                for j in range(0, 4):
                    body[i][j] = body[i][j] + delta_time * k_i_2[i][j] / 2
                    
            k_1_3 = acceleration(body[0], body[1], body[2])
            k_2_3 = acceleration(body[1], body[0], body[2])
            k_3_3 = acceleration(body[2], body[1], body[0])
            k_i_3 = [k_1_3, k_2_3, k_3_3]
            
            body = [body1.copy(), body2.copy(), body3.copy()]
            for i in range(0, 3):
                for j in range(0, 4):
                    body[i][j] = body[i][j] + delta_time * k_i_3[i][j]
                    
            k_1_4 = acceleration(body[0], body[1], body[2])
            k_2_4 = acceleration(body[1], body[0], body[2])
            k_3_4 = acceleration(body[2], body[1], body[0])
            k_i_4 = [k_1_4, k_2_4, k_3_4]
            
            body = [body1.copy(), body2.copy(), body3.copy()]
            k_i = [k_i_1, k_i_2, k_i_3, k_i_4]
            for i in range(0, 3):
                for j in range(0, 4):
                    body[i][j] = body[i][j] + delta_time * (k_i[0][i][j] + 2 * k_i[1][i][j] + 2 * k_i[2][i][j] + k_i[3][i][j]) / 6
                    
                    
            # 迭代后能量角动量录入
            energy.append(sys_energy(body[0], body[1], body[2]))
            angle_mom.append(angle_momentum(body[0], body[1], body[2]))
            
            #迭代后运动参量录入
            x1.append(body[0][0])
            y1.append(body[0][1])
            vx1.append(body[0][2])
            vy1.append(body[0][3])

            x2.append(body[1][0])
            y2.append(body[1][1])
            vx2.append(body[1][2])
            vy2.append(body[1][3])

            x3.append(body[2][0])
            y3.append(body[2][1])
            vx3.append(body[2][2])
            vy3.append(body[2][3])
            
            
        except OverflowError:
            print("数值溢出！计算终止，现在根据已有数据绘图···")
            break
        
        except ZeroDivisionError:
            print("数值溢出！计算终止，现在根据已有数据绘图···")
            break
        
    a = min(len(x1), len(x2), len(x3), len(y1), len(y2), len(y3), len(energy), len(angle_mom)) 
    x1 = x1[:a + 1:]
    y1 = y1[:a + 1:]
    x2 = x2[:a + 1:]
    y2 = y2[:a + 1:]
    x3 = x3[:a + 1:]
    y3 = y3[:a + 1:]
    energy = energy[:a + 1:]
    angle_mom = angle_mom[:a + 1:]
    time = time[: a + 1]
       
    # 计算守恒量，估计误差大小    
    e = energy[0]
    j = angle_mom[0]
    for i in tqdm.tqdm(range(0, len(energy)), desc = "能量，角动量校验计算"):
        energy[i] = (energy[i] - e) / e
        angle_mom[i] = (angle_mom[i] - j) / j
        
        
    plt.subplot(2, 3, 1)
    plt.plot(x1, y1, color = "red")
    plt.plot(x2, y2, color = "blue")
    plt.plot(x3, y3, color = "black")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("trace of the three body")
    print("picture-1 completed!")
    
    plt.subplot(2, 3, 2)
    plt.plot(time, x1, color = "red")
    plt.plot(time, y1, color = "blue")
    plt.xlabel("time")
    plt.ylabel("position x or y")
    plt.title("body 1")
    print("picture-2 completed!")
    
    plt.subplot(2, 3, 3)
    plt.plot(time, x2, color = "red")
    plt.plot(time, y2, color = "blue")
    plt.xlabel("time")
    plt.ylabel("position x or y")
    plt.title("body 2")
    print("picture-3 completed!")  
    
    plt.subplot(2, 3, 4)
    plt.plot(time, x3, color = "red")
    plt.plot(time, y3, color = "blue")
    plt.xlabel("time")
    plt.ylabel("position x or y")
    plt.title("body 3")
    print("picture-4 completed!")
    
    plt.subplot(2, 3, 5)
    plt.plot(time, energy, color = "red")
    print("picture-5 completed!")
    
    plt.subplot(2, 3, 6)
    plt.plot(time, angle_mom, color = "red")
    print("picture-6 completed!")
    
    plt.show()
    
    
def main():
    print("三体问题数值模拟, 万有引力常数G取值为1")
    m1 = float(input("the mass of the body1: "))
    x10, y10 = map(float, input("the initial position x, y of the body1: ").split())
    vx10, vy10 = map(float, input("the initial velocity of body1 in x, y direction: ").split())
    
    m2 = float(input("the mass of the body2: "))
    x20, y20 = map(float, input("the initial position x, y of the body2: ").split())
    vx20, vy20 = map(float, input("the initial velocity of body2 in x, y direction: ").split())
    
    m3 = float(input("the mass of the body3: "))
    x30, y30 = map(float, input("the initial position x, y of the body3: ").split())
    vx30, vy30 = map(float, input("the initial velocity of body3 in x, y direction: ").split())
    
    body01 = [x10, y10, vx10, vy10, m1]
    body02 = [x20, y20, vx20, vy20, m2]
    body03 = [x30, y30, vx30, vy30, m3]
    
    mass_central(body01, body02, body03)
    
    time_range = float(input("the desired time range: "))
    jingdu = int(input("the desired accuarcy(10000000 if nothing input): ") or 10000000)
    
    three_body(body01, body02, body03, time_range, jingdu)
    

if __name__ == "__main__":
    main()
    
    
   