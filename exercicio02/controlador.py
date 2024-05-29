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
encoder_esquerda = robo.getDevice('left wheel sensor')
encoder_direita = robo.getDevice('right wheel sensor')

# inicializa os motores
esquerda.setPosition(float('inf'))
direita.setPosition(float('inf'))
esquerda.setVelocity(0)
direita.setVelocity(0)

# inicializa os encoders
encoder_esquerda.enable(TIME_STEP)
encoder_direita.enable(TIME_STEP)

# essta variavel marca o tempo em 100ms
tempo = 0

## ---- alterar apenas daqui para baixo -------------

esquerda.setVelocity(1.0)
direita.setVelocity(1.0)

# Laço infinito
while robo.step(TIME_STEP) != -1:
   andou_esquerda = encoder_esquerda.getValue()
   andou_direita = encoder_direita.getValue()
   print(andou_esquerda, andou_direita)

   tempo += 1


