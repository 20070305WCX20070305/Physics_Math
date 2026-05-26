import math
import numpy as np
import matplotlib.pyplot as plt
import tqdm

# 球形无限深势阱，径向方程，考虑有效势能
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

def potential(n: int, l: int) -> list:
    shihanshu = list()
    
    # 调整时修改函数hanshu即可！
    def hanshu(x, n, l):
        return l * (l + 1) / ((x ** 2) * ((n + 1) ** 2))
        
    for i in range(n):
        shihanshu.append(hanshu((i + 1) / n, n, l))
        
    return shihanshu
        

def matrix_solution(matrix: list):
    oprator = np.array(matrix, dtype = float)
    eigenvalues, eigenvectors = np.linalg.eig(oprator)
    
    yingshe = dict()
    for i in tqdm.tqdm(range(0, len(eigenvalues)), leave = False):
        if yingshe.get(eigenvalues[i]) == None:
            if eigenvectors[0][i] < 1:
                yingshe[eigenvalues[i]] = [i]
           
        else:
            if eigenvectors[0][i] < 1:
                yingshe[eigenvalues[i]].append(i)
            
            
    return eigenvalues, eigenvectors, yingshe
            
def picture(n: int, k_th: int, eigenvalues: list, eigenvectors: list, yingshe: dict, energy: list, l: int):
    
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
        energy.append([l, (eigenvalues[i] * (n + 1) ** 2) / 2])
        plt.title(f"Energy = {energy[-1][-1]}")
        
    #plt.show()
    
def main():
    n = int(input("精确度，默认999") or 999)
    k_th = int(input("模拟范围，默认6") or 6)
    energy = list()
    
    for i in range(1, 100):
        energy.append([0, (i ** 2) * (math.pi ** 2) / 2])
    
    for i in tqdm.tqdm(range(1, 30)):
        l = i
        shihanshu = potential(n, l)
    
        juzhen = matrix(n, shihanshu)
    
        eigenvalues, eigenvectors, yingshe = matrix_solution(juzhen)
        
        picture(n, k_th, eigenvalues, eigenvectors, yingshe, energy, l)
    
    eff_energy = list()
    for i in range(0, len(energy)):
        eff_energy.append((energy[i][1], energy[i][0]))
        
    eff_energy.sort()
    print(f"主量子数n\t量子数l\t\t能量\n")
    for i in range(0, 100):
        print(f"{i + 1}\t\t{eff_energy[i][1]}\t\t{eff_energy[i][0]}\n")
    
    # 能级交错
     
if __name__ == "__main__":
    main()