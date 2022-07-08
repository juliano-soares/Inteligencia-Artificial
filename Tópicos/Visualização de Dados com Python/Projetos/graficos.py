# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E8CeUn4TdKQUg1Mtsn-i3F-V_z6Ot_sm
"""

# Visualização de dados em Python

# Gráfico de linhas
import random
import matplotlib.pyplot as plt

x = [1, 2, 5]
y = [2, 3, 7]

# Título
plt.title("Meu primeiro gráfico com Python")

# Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.plot(x, y)
plt.show()

# Gráfico de barras

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x, y)
plt.show()

# Gráfico de barras 2

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label="Grupo 1")
plt.bar(x2, y2, label="Grupo 2")
plt.legend()
plt.show()

# Gráfico Scatterplot

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus Pontos", color="r")
plt.plot(x, y)
plt.legend()
plt.show()

# Boxplot - Diagrama de caixa

vetor = []
for i in range(1000):
    numero_aleatorio = random.randint(0, 50)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
