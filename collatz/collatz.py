# 3X+1
num = int(input('Ensira o valor para ser calculado: '))
steps = 0
import matplotlib.pyplot as plt
y = [num]
x = [steps]
while num > 1:
    if num % 2 == 0:
        num = num / 2
        steps+=1
    else:
        num = (num * 3)+1
        steps+=1
    y.append(num)
    x.append(steps)

plt.plot(x, y, marker='o', markerfacecolor='purple')

plt.xlabel('x - quantidade de cálculos')

plt.ylabel('y - Valor atual')

plt.show()