# Exemplos de call-backs do Matplotlib para a interação com o usuário
# Para terminar o programa, pressione a tecla 'escape'
 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

centro_eixo_x = 0
centro_eixo_y = 0
escala = 1
rotacao =np.identity(3,dtype=float)
theta = 0

end_loop = False

# Função que gerencia eventos do mouse
def on_press(event):
    print('Você pressionou o botão do mouse:', event.button, event.xdata, event.ydata)
    global centro_eixo_x
    global centro_eixo_y
    
    centro_eixo_x = round(event.xdata,2)
    centro_eixo_y = round(event.ydata,2)   

# Função que gerencia eventos do teclado
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
    
def matriz_rotacao(theta_rad):
    global rotacao      
    rotacao =np.matmul( np.array([ [ np.cos(theta_rad) , -np.sin(theta_rad),0]
                                    ,[  np.sin(theta_rad) , np.cos(theta_rad),0]
                                    ,[0,0,1]]) ,rotacao)


def matriz_escala(escala):
    return np.array([[escala, 0, 0],
                     [0, escala, 0],
                     [0, 0, 1]])

def matriz_translacao(centro_eixo_x, centro_eixo_y):
    return np.array([[1, 0, centro_eixo_x],
                     [0, 1, centro_eixo_y],
                     [0, 0, 1]])
