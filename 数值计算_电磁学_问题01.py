'''
问题： 

三维空间的正方体模型，格点之间用导线相连，求解三个位置上的端口的电阻

'''


def main():
    numbers = list(map(int, input("desired N: ").split()))
    error = float(input("error: ") or 1/1000000)
    output = []
    
    for j in range(0, len(numbers)):
        n = numbers[j]
        calcualtion_value = [n]
        
        cases = [[n, 0, 0], [n, n, 0], [n, n, n]]
        for i in range(0, 3):
            tensor = cauculation(error, cases[i], n)
            a, b, c = tensor[(0, 0, 1)], tensor[(0, 1, 0)], tensor[(1, 0, 0)]
            calcualtion_value.append(f"{1/(a + b + c):.3f}")
        output.append(calcualtion_value)
        
    print(f"N\tR1\tR2\tR3\t")        
    for i in range(len(output)):
        a, b, c, d = output[i]
        print(f"{a}\t{b}\t{c}\t{d}")
        
def cauculation(error: float, specialcase: list, n: int):
    a, b, c = specialcase
    
    #张量的初始化
    tensor = dict()
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if i == 0 and j == 0 and k == 0:
                    tensor[(i, j, k)] = 0
                elif i == a and j == b and k == c:
                    tensor[(i, j, k)] = 1
                else:
                    tensor[(i, j, k)] = 1/2
            
    realerror = error + 1
    count = 1
    
    while realerror >= error:
        realerror = 0
        for i in range(0, n + 1):
            for j in range(0, n + 1):
                for k in range(0, n + 1):
                    if (i, j, k) in [(0, 0, 0), (a, b, c)]:
                        continue
                    
                    valuelist = list()
                    for item in [[i + 1, j, k], [i - 1, j, k], [i, j + 1, k], [i, j - 1, k], [i, j, k + 1], [i, j, k - 1]]:
                        if tensor.get(tuple(item)) is not None:
                            valuelist.append(tensor[tuple(item)])
                    
                    new_value = sum(valuelist) / len(valuelist)
                    new_error = abs(tensor[(i, j, k)] - new_value) 
                    tensor[(i, j, k)] = new_value
                    
                    if realerror < new_error:
                        realerror = new_error
        count += 1
        if count % 100 == 0:
            print(f"已经迭代{count}次，误差浮动为{new_error}")
            
    return tensor
               
if __name__ == "__main__":
    main()      
                        
                