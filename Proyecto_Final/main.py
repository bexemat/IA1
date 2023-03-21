from FuncionesAlgoritmos import *
from miKmeans import *
cant=len(img_bananas_cortadas)
c0=np.zeros(cant)
c1=np.ones(cant)
c2=np.zeros(cant)
c3=np.zeros(cant)
for i in range(0,cant):
    c2[i]=2
    c3[i]=3
X=caracteristicas3d
#clases
C=np.concatenate((c0,c1,c2,c3),axis=0)
C=np.uint8(C)
# nuevos datos a imgClasificadas con KNN
Y=pruebas3d
# iniciar KNN
print('*********************Algoritmo KNN*****************************')
plt.figure()
GraficaCaract3d(BGRNaranjas,BGRLimones,BGRTomates,BGRBananas,0,1,2,'Entrenamiento del Algoritmo de KNN con caracteristicas de color')
plt.figure()
GraficaCaract3d(BGRNaranjasTest,BGRLimonesTest,BGRTomatesTest,BGRBananasTest,0,1,2,'Pruebas para el Algoritmo de KNN con caracteristicas de color ')
plt.show()
clasificador = KNN(k=5)
clasificador.aprendizaje(X,C) # fase de aprendizaje
clasificaknn= clasificador.clasificacion(Y) #resultados obtenidos
indknn=[0,1,2,3] 
#MuestraImgConResultado(len(clasificaknn),len(img_bananas_test_cortadas),indknn,img_bananas_test_cortadas,img_naranjas_test_cortadas,img_limones_test_cortadas,img_tomates_test_cortadas,clasificaknn)
#plt.show()
test=[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]  #resultados esperados para knn
eficiencia=acierto(test,clasificaknn)
print('Eficiencia del Algoritmo KNN :',eficiencia)
"""
    KMEANS
"""
print('*********************Algoritmo KMEANS**************************')

print('--------Algoritmo Kmeans de SKLEARN-----------')
clusters=KMeans(n_clusters=4,max_iter=300,tol=0.0001)
clusters.fit(X)
grupos=clusters.labels_
centroide=clusters.cluster_centers_
GraficaKmeans(grupos,X,centroide,0,'Resultado del Algoritmo Kmeans implementado por SKLEARN ')
indice,correctos1=EfEntrenamineto(grupos,img_bananas,4)
print('El porcentaje de aciertos en el entrenamiento de kmeans de implementacion de sklearn fue de : ',(np.sum(correctos1)/X.shape[0]))
resp=RespuestaEsperada(indice,img_bananas_test)
clasificacion=KmeansClasifica(pruebas3d,centroide)  #clasifica las pruebas con la distancias a los centroides calculados en el entrenamiento
aciertos=acierto(clasificacion,resp)
print('El porcentaje de acierto de las pruebas con kmeans de implementacion de sklearn es de :',aciertos)
MuestraImgConResultado(len(clasificacion),len(img_bananas_test_cortadas),indice,img_bananas_test_cortadas,img_naranjas_test_cortadas,img_limones_test_cortadas,img_tomates_test_cortadas,clasificacion)
plt.show()
print('--------Algoritmo Kmeans Propio-----------')
cluster=KMEANS()
grups,centroides,contador=cluster.Agrupa(X)
indice1,correctos2=EfEntrenamineto(grups,img_bananas,4)
print('El porcentaje de aciertos en el entrenamiento de kmeans de implementacion propia fue de : ',(np.sum(correctos2)/X.shape[0]))
plt.figure()
GraficaKmeans(grups,X,centroides,contador,'Resultado del Algoritmo Kmeans de implementacion propia ')
resp1=RespuestaEsperada(indice1,img_bananas_test)
clasKmeans=KmeansClasifica(pruebas3d,centroides)  #clasifica las pruebas con la distancias a los centroides calculados en el entrenamiento
MuestraImgConResultado(len(clasKmeans),len(img_bananas_test_cortadas),indice1,img_bananas_test_cortadas,img_naranjas_test_cortadas,img_limones_test_cortadas,img_tomates_test_cortadas,clasKmeans)
plt.show()
aciertos1=acierto(clasKmeans,resp1)
print('El porcentaje de acierto de las pruebas con kmeans de implementacion propia es de :',aciertos1)