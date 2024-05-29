#  Copyright 2024 Visao Robotica Imagem (VRI)
#   - Felipe Bombardelli <felipebombardelli@gmail.com> : 2024
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# =============================================================================
#  Header
# =============================================================================

from controller import Robot, Motor

TIME_STEP = 100   # 100 milisegundos

# =============================================================================
#  main
# =============================================================================

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

   # primeiros 5 segundos, gira sentido horario
   if tempo%100 < 50:
      esquerda.setVelocity(2.0)
      direita.setVelocity(-2.0)

   # outros 5 segundos, gira sentido anti-horario
   else:
      esquerda.setVelocity(-2.0)
      direita.setVelocity(2.0)

   # fim do ciclo
   tempo += 1
