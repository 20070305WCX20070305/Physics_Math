import math
import numpy as np
import matplotlib.pyplot as plt
import tqdm

# 矩阵法求解薛定谔方程，这个程序，在【0,1】无限深势阱中势能变化，波函数的情况！
def matrix(n: int, potential: list) -> list:
    
    hamiton = list()
    for i in tqdm.tqdm(range(0, n), desc = "preparation", leave = False):
        zhongjianjihe = list()
        for j in range(0, n):
            zhongjianjihe.append(0)
            
        hamiton.append(zhongjianjihe)
        
    for i in tqdm.tqdm(range(n), leave = False):
        for j in range(n):
            
            if abs(i - j) == 1:
                hamiton[i][j] = -1
                
            elif i == j:
                hamiton[i][j] = 2 + potential[i]
                
    return hamiton

def potential(n: int) -> list:
    shihanshu = list()
    
    # 调整时修改函数hanshu即可！
    def hanshu(x):
        return math.sin((1 - x) * math.pi) / 2000
        
    for i in range(n):
        shihanshu.append(hanshu((i + 1) / n))
        
    return shihanshu
        

def matrix_solution(matrix: list):
    oprator = np.array(matrix, dtype = float)
    eigenvalues, eigenvectors = np.linalg.eig(oprator)
    
    yingshe = dict()
    for i in tqdm.tqdm(range(0, len(eigenvalues)), leave = False):
        if yingshe.get(eigenvalues[i]) == None:
            yingshe[eigenvalues[i]] = [i]
           
        else:
            yingshe[eigenvalues[i]].append(i)
            
            
    return eigenvalues, eigenvectors, yingshe
            
def picture(n: int, k_th: int, eigenvalues: list, eigenvectors: list, yingshe: dict):
    
    def tupianguige(k_th):
        yingshezidian = {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [2, 2], 5: [2, 3], 6: [2, 3]}
        
        return yingshezidian[k_th]
    
    delta_x = 1 / (n + 1)
    x_zuobiao = list()
    
    for i in tqdm.tqdm(range(n), leave = False):
        x_zuobiao.append((i + 1) * delta_x)
    
    a, b = tupianguige(k_th)  
    eigenvalues.sort()
    
    for i in tqdm.tqdm(range(0, k_th), leave = False):
        plt.subplot(a, b, i + 1)
        for j in range(0, len(yingshe[eigenvalues[i]])):
            plt.plot(x_zuobiao, eigenvectors[:, yingshe[eigenvalues[i]][j]])
        
        plt.grid(True)    
        plt.title(f"Energy = {eigenvalues[i] / eigenvalues[0]}")
        
    plt.show()
    
def main():
    n = int(input("精确度，默认999") or 999)
    k_th = int(input("模拟范围，默认6") or 6)
    
    shihanshu = potential(n)
    
    juzhen = matrix(n, shihanshu)
    
    eigenvalues, eigenvectors, yingshe = matrix_solution(juzhen)
    picture(n, k_th, eigenvalues, eigenvectors, yingshe)
    
if __name__ == "__main__":
    main()
    
    
    
 