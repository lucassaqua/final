# Alunos: Lucas Cardoso Gomes e Rafael dos Santos de Oliveira Lima

#%matplotlib qt
import callback as call  
import numpy as np
import matrizes as mt
import matplotlib.pyplot as plt

# Aqui voce pode optar por visualizar um quadrado ou um triangulo 
matriz = np.array([[2,2,1], [4,2,1], [3,4,1]]) # triangulo
# matriz = np.array([[-0.5,-0.5,1],[0.5,-0.5,1],[0.5,0.5,1],[-0.5,0.5,1]]) # quadrado

po = np.transpose(matriz)

xMenor = np.amin(po[0, :])  # xmenor e ymenor nao sao usadas. No nosso do periodo passado era usados no centro_eixo_x
xMaior = np.amax(po[0, :])

yMenor = np.amin(po[1, :])
yMaior = np.amax(po[1, :])

centroX = 0.
centroY = 0.
           
fig, ax = plt.subplots()
cid = fig.canvas.mpl_connect('button_press_event', call.on_press)
cid = fig.canvas.mpl_connect('key_press_event', call.on_key)

while not call.end_loop:             
        if call.end_loop == True:
            break
            
        # se tu souber o que significa esse prd renomeia ele 
        prd = np.matmul( call.matriz_translacao(call.centroX, call.centroY), call.matriz_escala(call.escala))
        
        thetaRadianos = np.radians(call.theta)
        if call.theta != 0:
           call.matriz_rotacao(thetaRadianos)
        
        matriz_final = np.matmul(prd, call.rotacao)  
        pT = np.matmul(matriz_final, po)         
        
        print("theta em radianos: ", thetaRadianos)
        print("velocidade de rotacao: ", call.rotacao)
        print("escala: ", call.escala)
        print("centro do eixo x: ", call.centroX)
        print("centro do eixo y: ", call.centroY)
        
        plt.xlim((-xMaior*4, xMaior*4)), plt.ylim((-yMaior*4, yMaior*4)) 
        xlist = np.append(pT[0, :], pT[0, 0])
        ylist = np.append(pT[1, :], pT[1, 0])
        plt.plot(xlist, ylist, '-r',)
        plt.fill_between(xlist, ylist) 
        plt.show()
        plt.pause(0.01)
        plt.clf()
        






