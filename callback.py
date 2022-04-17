# Exemplos de call-backs do Matplotlib para a interação com o usuário
# Para terminar o programa, pressione a tecla 'escape'

import numpy as np

centroX = 0
centroY = 0
escala = 1
rotacao = np.identity(3, dtype = float)
theta = 0

end_loop = False

def on_press(event):
    print('Você pressionou o botão do mouse: ', event.button, event.xdata, event.ydata)
    global centroX
    global centroY
    
    centroX = round(event.xdata, 2)
    centroY = round(event.ydata, 2)   

def on_key(event):
    global end_loop
    global escala
    global theta
    
    print('Você pressionou a tecla: "', event.key, '"', event.xdata, event.ydata)
    if event.key == 'escape': 
        end_loop = True
    elif event.key == 'up':
        escala += 0.5
    elif event.key == 'down':
        escala -= 0.5
    elif event.key == 'left':
        theta += 2
        matriz_rotacao(0)
    elif event.key == 'right':
        theta -= 2
        matriz_rotacao(0)
    
def matriz_rotacao(thetaRadianos):
    global rotacao      
    rotacao = np.matmul( np.array([[np.cos(thetaRadianos) , -np.sin(thetaRadianos), 0]
                                    , [np.sin(thetaRadianos) , np.cos(thetaRadianos), 0]
                                    , [0 ,0 , 1]]), rotacao)

def matriz_escala(escala):
    return np.array([[escala, 0, 0],
                     [0, escala, 0],
                     [0, 0, 1]])

def matriz_translacao(centroX, centroY):
    return np.array([[1, 0, centroX],
                     [0, 1, centroY],
                     [0, 0, 1]])






