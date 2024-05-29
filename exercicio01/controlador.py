# =======================================================================================
#  Header
# =======================================================================================

from controller import Robot, Motor

TIME_STEP = 100   # 100 milisegundos

# =======================================================================================
#  main
# =======================================================================================

robo = Robot()

# pega os dispositivos
esquerda = robo.getDevice('left wheel')
direita = robo.getDevice('right wheel')

# inicializa os motores
esquerda.setPosition(float('inf'))
direita.setPosition(float('inf'))
esquerda.setVelocity(0)
direita.setVelocity(0)

# essta variavel marca o tempo em 100ms
tempo = 0

## ---- alterar apenas daqui para baixo -------------

while robo.step(TIME_STEP) != -1:
   esquerda.setVelocity(2.0)
   direita.setVelocity(2.0)

   # fim do ciclo
   tempo += 1


