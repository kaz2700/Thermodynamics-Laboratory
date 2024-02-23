import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("Hoja de errores para Laboratorio de Termodinamica\n Aviso: Solo usar propagación de errores en la variable y!")

def n(data):#numero de datos; data = medidas
    return len(data)

def media(data): #data = medidas
    return np.mean(data)

def desviacion_tipica(data): #o_n-1 / sigma_n-1; data = medidas
    return np.std(data) * np.sqrt(len(data)) / np.sqrt(len(data)-1)

def err_estadistico(data): #k = 2; data = medidas
    k = 2
    return k*stats.sem(data)

def err_escala(data): #data = errores escalares de la medida
    s = 0
    for i in data:
        s += i**2
    return s**0.5

def plot(errorBar):
    plt.errorbar(X, Y, yerr=er_Y, fmt='o', capsize=5, capthick=2) if errorBar else plt.plot(X,Y, ".")
    plt.show()

def info(X, Y, er_X, er_Y):
    print("Información de\nX=", X, "erX=", er_X, "\nY=", Y, " erY=", er_Y)
    print("n =", n(Y))
    print("media =", media(Y))

#datos
X=[1, 2, 3]
Y=[2, 4, 6]

#errores escalares de los datos
er_X=[0.2, 0.4, 0.6]
er_Y=[0.4, 0.6, 0.8]

info(X, Y, er_X, er_Y)
plot(True)