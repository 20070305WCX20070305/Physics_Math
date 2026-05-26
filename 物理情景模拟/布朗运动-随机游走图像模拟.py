import random
import matplotlib.pyplot as plt
import numpy as np
import tqdm

def random_moving(numbers: int, ave_ziyoucheng: int) -> list:
    
    def moving_direction() -> list:
        num_x = random.uniform(-1, 1)
        num_y = random.uniform(-1, 1)
    
        move_sin = num_y / (num_x ** 2 + num_y ** 2) ** 0.5
        move_cos = num_x / (num_x ** 2 + num_y ** 2) ** 0.5
        
        return [move_cos, move_sin] 
    
    xiangdui_yucewucha = [0]
    x = [0]
    y = [0]
    
    for n in tqdm.tqdm(range(1, numbers + 1), desc = "data generation process:"):
        move_cos, move_sin = moving_direction()
        
        particle_x = x[-1] + move_cos * ave_ziyoucheng
        particle_y = y[-1] + move_sin * ave_ziyoucheng
        
        x.append(particle_x)
        y.append(particle_y)
        
        yuce = ave_ziyoucheng * (n ** 0.5)
        xiangduiwucha = (particle_x ** 2 + particle_y ** 2) ** 0.5 - yuce / ((particle_x ** 2 + particle_y ** 2) ** 0.5)
        
        xiangdui_yucewucha.append(xiangduiwucha)
        
    return [x, y, xiangdui_yucewucha]

def picture(shujuzu):
    x, y, wucha = shujuzu[0], shujuzu[1], shujuzu[2]
    
    bianhao = list()
    for i in tqdm.tqdm(range(0, len(wucha))):
        bianhao.append(i)
    print("数据导入及初始化完成")    
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y, color = "red")
    plt.xlabel("deplacement of x direction")
    plt.ylabel("deplacement of y direction")
    plt.title("random moving")
    print("第一张图片完成")
    
    plt.subplot(1, 2, 2)
    plt.plot(bianhao, wucha, color = "blue")
    plt.title("prediction and reality")
    print("第二张图片完成")
    
    plt.show()
    
def main():
    numbers = int(input("模拟次数(默认5000000)：") or 5000000)
    ziyoucheng = float(input("自由程(默认0.000001)：") or 0.000001)
    
    data = random_moving(numbers, ziyoucheng)
    picture(data)
    
if __name__ == "__main__":
    main()
     
    