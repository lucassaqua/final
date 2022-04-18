# Alunos: Lucas Cardoso Gomes e Rafael dos Santos de Oliveira Lima

#%matplotlib qt
import callback as call  
import numpy as np
import matplotlib.pyplot as plt

# Aqui voce pode optar por visualizar um quadrado ou um triangulo 
matriz = np.array([[2,2,1], [4,2,1], [3,4,1]]) # triangulo
# matriz = np.array([[-0.5,-0.5,1],[0.5,-0.5,1],[0.5,0.5,1],[-0.5,0.5,1]]) # quadrado

po = np.transpose(matriz)

xMaior = np.amax(po[0, :])
yMaior = np.amax(po[1, :])

centroX = 0.
centroY = 0.
           
fig, ax = plt.subplots()
cid = fig.canvas.mpl_connect('button_press_event', call.on_press)
cid = fig.canvas.mpl_connect('key_press_event', call.on_key)

while not call.end_loop:             
        if call.end_loop == True:
            break
            
        transformacao = np.matmul( call.matriz_translacao(call.centroX, call.centroY), call.matriz_escala(call.escala))
        
        thetaRadianos = np.radians(call.theta)
        if call.theta != 0:
           call.matriz_rotacao(thetaRadianos)
        
        matriz_final = np.matmul(transformacao, call.rotacao)  
        pT = np.matmul(matriz_final, po)         
        
        print("theta em radianos: ", thetaRadianos)
        print("velocidade de rotacao: ", call.rotacao)
        print("escala: ", call.escala)
        print("centro do eixo x: ", call.centroX)
        print("centro do eixo y: ", call.centroY)
        
        plt.xlim((-xMaior*4, xMaior*4)), plt.ylim((-yMaior*4, yMaior*4)) 
        listaX = np.append(pT[0, :], pT[0, 0])
        listaY = np.append(pT[1, :], pT[1, 0])
        plt.plot(listaX, listaY, '-r',)
        plt.fill_between(listaX, listaY) 
        plt.show()
        plt.pause(0.01)
        plt.clf()
        






