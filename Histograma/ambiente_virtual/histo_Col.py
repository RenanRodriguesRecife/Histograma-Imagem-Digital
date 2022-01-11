# Histograma colorido

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imágem
img = cv2.imread("img.jpg")

# Um histograma colorido não é nada
#  mais do que 3 histórgrama que representa
#  um canal de cor (vermelho, verde e azul)

color = ('b','g','r')

for i, col in enumerate(color):
#    print(i, col)
    #no caso de um histograma de cores é melhor 
    #você fazer 3 no opencv e depois passar para 
    #a matplotlib para juntar os 3 em um único canal
    
    #parametros de .calcHist()
    #imagem 
    #identificador do histograma
    #mascara - o opencv permite calcular o histograma de um parte da imagem
    #bin
    #intervalor
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    #.plot vai construir o hitograma
    plt.plot(histr, color = col)
    #.xlim vai definir quais são os limites
    plt.xlim([0,256])


#exibe a imagem
cv2.imshow("Imagem Original",img)
#exibe o histograma
plt.show()

#.waitkey para o programa não fechar rápido
cv2.waitKey(0)
#.destroyAllWindows para fazer a limpesa adequada
cv2.destroyAllWindows()