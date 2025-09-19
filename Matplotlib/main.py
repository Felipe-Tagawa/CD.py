import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = x * 2
y2 = x * x

plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Plotando o gráfico
plt.plot(x,y, 's:r', x, y2, 'p--g', linewidth = 1, markersize=10) # Separado por entrela, linha tracejada, da cor vermelha
#plt.show()

plt.subplot(1, 2, 1) # 1 linha, 2 colunas e colocar na primeira célula
plt.plot(x, y, 's:r', linewidth = 3, markersize=10)
plt.subplot(1, 2, 2)
plt.plot(x, y2, 'p--g', linewidth = 3, markersize=10)

#plt.show()
