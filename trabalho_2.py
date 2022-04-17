#%matplotlib qt
import callback as call  
import numpy as np
import matplotlib.pyplot as plt
import matrizes as mt

 

matriz = np.array([[2,2,1], [4,2,1], [3,4,1]])
# matriz = np.array([[-0.5,-0.5,1],[0.5,-0.5,1],[0.5,0.5,1],[-0.5,0.5,1]])
po = np.transpose(matriz)

xmin = np.amin(po[0,:])
xmax = np.amax(po[0,:])

ymin = np.amin(po[1,:])
ymax = np.amax(po[1,:])

centro_eixo_x = 0.
centro_eixo_y = 0.

           
fig, ax = plt.subplots()

cid = fig.canvas.mpl_connect('button_press_event', call.on_press)
cid = fig.canvas.mpl_connect('key_press_event', call.on_key)


while not call.end_loop:             
        if call.end_loop == True:
            break

            
        prd = np.matmul( call.matriz_translacao(call.centro_eixo_x, call.centro_eixo_y),call.matriz_escala(call.escala))
        
        theta_rad=np.radians(call.theta)
        if call.theta != 0:
           call.matriz_rotacao(theta_rad)
        
        matriz_final = np.matmul(prd, call.rotacao)  
        pT = np.matmul(matriz_final,po)         
        
        
        # plt.title("theta : ",theta)
        print("theta_rad : ",theta_rad)
        print("velocidade_rotacao : ",call.rotacao)
        print("escala",call.escala)
        print("centro_eixo_x",call.centro_eixo_x)
        print("centro_eixo_y",call.centro_eixo_y)
        
        
        plt.xlim((-xmax*4, xmax*4)), plt.ylim((-ymax*4, ymax*4)) 
        xlist = np.append(pT[0, :], pT[0, 0])
        ylist = np.append(pT[1, :], pT[1, 0])
        plt.plot(xlist, ylist, '-r',)
        plt.fill_between(xlist,ylist) 
        plt.show()
        plt.pause(0.01)
        plt.clf()
        
