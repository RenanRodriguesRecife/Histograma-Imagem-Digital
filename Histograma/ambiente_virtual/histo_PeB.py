# Histograma preto e branco

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imágem e preto e branco
img = cv2.imread("img.jpg",0)

#ravel -> pega matriz 2d (que é imagem) e tranforma em um vetor de uma dimenção
#bins -> quanto menos bins mais tons tem em um ponto do eixo x do histograma
#256 garante que cada bin tem um ton
#intervalo do histograma
plt.hist(img.ravel(), 256, [0, 256])

#exibe a imagem
cv2.imshow("Imagem Original",img)
#exibe o histograma
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()