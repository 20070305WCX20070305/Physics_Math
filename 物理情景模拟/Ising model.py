# program "Ising model", applying Monte Carlo integration, two demenssional problem
import math
import tqdm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap 
import random
import os

def major(data: list[list[float]], repeat: int, size: int, t: float):
    for _ in tqdm.tqdm(range(repeat * size * size), desc= "Major program: ", leave= False):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        top = data[i - 1][j] if i > 0 else data[size - 1][j]
        bottom = data[i + 1][j] if i < size - 1 else data[0][j]
        left = data[i][j - 1] if j > 0 else data[i][size - 1]
        right = data[i][j + 1] if j < size - 1 else data[i][0]
                
        average = (top + bottom + left + right) / 4
        if data[i][j] * average < 0: 
            #the energy will decrease if data -> -data
            data[i][j] = -data[i][j]
            continue
        else:
            rand = random.random()
            energy = 2 * 4 * average * data[i][j]
            if rand < math.exp(- energy / t):
                data[i][j] = -data[i][j]
    

def picture(data: list[list[int]], repeat: int, size: int, t: float, state: bool):
    cmap = ListedColormap(['white', 'black'] if state else ['black', 'white'])  

    plt.figure(figsize=(10, 6))
    plt.imshow(data, cmap=cmap, interpolation='nearest', origin='upper')
    plt.title(f"Monte Carlo method for {size}*{size} two demensional ferromagnet with repeation of {repeat} times(temperture: {t})")

    save_dir = '/home/ubuntu/数学物理仓库/物理情景模拟/images'
    os.makedirs(save_dir, exist_ok=True)  # 自动创建目录，存在也不报错
    save_path = os.path.join(save_dir, f'ising_{size}x{size}_T{t}.png')
    plt.savefig(save_path)
    print(f"图片已保存至: {os.path.abspath(save_path)}")  # 打印完整路径，方便查找
    
size = int(input("the size of the system(100 if no input): ") or 100)
repeat_number = int(input("repeat number(20000 if no input): ") or 20000)
temperature = list(map(float, input("system temperature(0~5 desired, 2.27: phase transform): ").split()))

for tem in temperature:
    # initializing 
    data = np.random.rand(size, size)
    for i in tqdm.tqdm(range(0, size), desc="Initializing: ", leave= False):
        for j in range(0, size):
            data[i][j] = -1 if data[i][j] < 0.5 else 1

    # Core repeatition
    major(data, repeat_number, size, tem)

    # visualize
    count = np.sum(data)
    state = True if count < 0 else False
    picture(data, repeat_number, size, tem, state)

