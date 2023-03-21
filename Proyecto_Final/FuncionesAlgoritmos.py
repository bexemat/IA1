from ExtraeCaract import *
from knn import KNN
from sklearn.cluster import KMeans

def acierto(pruebas,resultado):
    i=0
    sum=0
    cantPruebas=len(pruebas)
    aciertos=0
    while(i<cantPruebas):
        if(pruebas[i]==resultado[i]):
            sum=sum+1
        i=i+1
    aciertos=((sum*100)/(cantPruebas))
    return aciertos
def min(vector):
    min=100000
    indice=0
    for i in range(0,len(vector)):
        if(vector[i]<min):
            min=vector[i]
            indice=i
    return indice
def GraficaKmeans(grupos,X,centroide,iteracion,titulo):
    
    ax =plt.subplot(projection='3d')
    plt.title(titulo+', Iteracion n : '+str(iteracion),fontdict={'family':'serif','color':'darkblue','weight':'bold','size':18})
    for i in range(X.shape[0]):        
        if(grupos[i]==0):
            marcar='o'
            color='blue'
            ax.scatter(xs=X[i,0],ys=X[i,1],zs=X[i,2],c=color,s=100,marker=marcar)
        if(grupos[i]==1):
            marcar='v'
            color='red'
            ax.scatter(xs=X[i,0],ys=X[i,1],zs=X[i,2],c=color,s=100,marker=marcar)
        if(grupos[i]==2):
            marcar='*'
            color='green'
            ax.scatter(xs=X[i,0],ys=X[i,1],zs=X[i,2],c=color,s=100,marker=marcar)
        if(grupos[i]==3):
            marcar='p'
            color='yellow'
            ax.scatter(xs=X[i,0],ys=X[i,1],zs=X[i,2],c=color,s=100,marker=marcar)
    for i in range(0,4):
        ax.scatter(xs=centroide[i,0],ys=centroide[i,1],zs=centroide[i,2],c='black',s=100,marker='x')
    plt.show()
def KmeansClasifica(PuntosNuevos,centroides):
    distancia=np.zeros((PuntosNuevos.shape[0],centroides.shape[0]))
    clasificacion=[]
    for i in range(0,PuntosNuevos.shape[0]):
        for j in range(0,centroides.shape[0]):
            distancia[i,j]=np.sqrt(np.sum(PuntosNuevos[i,:]-centroides[j,:])**2)
    for i in range(0,PuntosNuevos.shape[0]):
        mindis=min(distancia[i,:]) 
        clasificacion.append(mindis) 
    return clasificacion    
def EfEntrenamineto(grupos,img_bananas,k):
    indice=np.zeros(k)
    aciertos=np.zeros(k)
    indice[0],aciertos[0]=EficienciaEntrenamiento(grupos[0:len(img_bananas)],len(img_bananas),'Eficiencia en el entrenamiento en la clase ')
    indice[1],aciertos[1]=EficienciaEntrenamiento(grupos[len(img_bananas):2*len(img_bananas)],len(img_bananas),'Eficiencia en el entrenamiento en la clase ')
    indice[2],aciertos[2]=EficienciaEntrenamiento(grupos[2*len(img_bananas):3*len(img_bananas)],len(img_bananas),'Eficiencia en el entrenamiento en la clase ')
    indice[3],aciertos[3]=EficienciaEntrenamiento(grupos[3*len(img_bananas):4*len(img_bananas)],len(img_bananas),'Eficiencia en el entrenamiento en la clase ')
    return indice,aciertos
def RespuestaEsperada(indice,img_bananas_test):
    resp=[]  #respuesta esperada para kmeans
    for i in range(0,4*len(img_bananas_test)):
        if i<len(img_bananas_test):
            resp.append(indice[0])
        if i>=len(img_bananas_test) and i<2*len(img_bananas_test):
            resp.append(indice[1])
        if i>=2*len(img_bananas_test) and i<3*len(img_bananas_test):
            resp.append(indice[2])
        if i>=3*len(img_bananas_test) and i<4*len(img_bananas_test):
            resp.append(indice[3])
    return resp

def MuestraImgConResultado(cantMuestras,cantPorClase,indiceClases,imgBan,imgNar,imgLim,imgTom,imgClasificadas):        
    for i in range(0,cantMuestras):
        if i<cantPorClase:
            if imgClasificadas[i]==indiceClases[0]:
                plt.figure()
                plt.imshow(imgBan[i])
                plt.title('Fruta clasificada como Banana')
            elif imgClasificadas[i]==indiceClases[1]:
                plt.figure()
                plt.imshow(imgBan[i])
                plt.title('Fruta clasificada como Naranja')
            elif imgClasificadas[i]==indiceClases[2]:
                plt.figure()
                plt.imshow(imgBan[i])
                plt.title('Fruta clasificada como Limon')
            elif imgClasificadas[i]==indiceClases[3]:
                plt.figure()
                plt.imshow(imgBan[i])
                plt.title('Fruta clasificada como Tomate')
        elif i<2*cantPorClase and i>=cantPorClase:
            if imgClasificadas[i]==indiceClases[0]:
                plt.figure()
                plt.imshow(imgNar[i-cantPorClase])
                plt.title('Fruta clasificada como Banana')
            elif imgClasificadas[i]==indiceClases[1]:
                plt.figure()
                plt.imshow(imgNar[i-cantPorClase])
                plt.title('Fruta clasificada como Naranja')
            elif imgClasificadas[i]==indiceClases[2]:
                plt.figure()
                plt.imshow(imgNar[i-cantPorClase])
                plt.title('Fruta clasificada como Limon')
            elif imgClasificadas[i]==indiceClases[3]:
                plt.figure()
                plt.imshow(imgNar[i-cantPorClase])
                plt.title('Fruta clasificada como Tomate')
        elif i<3*cantPorClase and i>=2*cantPorClase:
            if imgClasificadas[i]==indiceClases[0]:
                plt.figure()
                plt.imshow(imgLim[i-2*cantPorClase])
                plt.title('Fruta clasificada como Banana')
            elif imgClasificadas[i]==indiceClases[1]:
                plt.figure()
                plt.imshow(imgLim[i-2*cantPorClase])
                plt.title('Fruta clasificada como Naranja')
            elif imgClasificadas[i]==indiceClases[2]:
                plt.figure()
                plt.imshow(imgLim[i-2*cantPorClase])
                plt.title('Fruta clasificada como Limon')
            elif imgClasificadas[i]==indiceClases[3]:
                plt.figure()
                plt.imshow(imgLim[i-2*cantPorClase])
                plt.title('Fruta clasificada como Tomate')
        elif i<4*cantPorClase and i>=3*cantPorClase:
            if imgClasificadas[i]==indiceClases[0]:
                plt.figure()
                plt.imshow(imgTom[i-3*cantPorClase])
                plt.title('Fruta clasificada como Banana')
            elif imgClasificadas[i]==indiceClases[1]:
                plt.figure()
                plt.imshow(imgTom[i-3*cantPorClase])
                plt.title('Fruta clasificada como Naranja')
            elif imgClasificadas[i]==indiceClases[2]:
                plt.figure()
                plt.imshow(imgTom[i-3*cantPorClase])
                plt.title('Fruta clasificada como Limon')
            elif imgClasificadas[i]==indiceClases[3]:
                plt.figure()
                plt.imshow(imgTom[i-3*cantPorClase])
                plt.title('Fruta clasificada como Tomate')   
def EficienciaEntrenamiento(grupos,cant,titulo):
    bananas=grupos  
    x=np.zeros((cant,4))
    #print(x.shape[0])
    for i in range(0,cant):
        if bananas[i]==0:
            x[i,0]=1
        elif bananas[i]==1:
            x[i,1]=1
        elif bananas[i]==2:
            x[i,2]=1
        elif bananas[i]==3:
            x[i,3]=1    
    suma=np.zeros(4)
    for i in range(0,4):
        suma[i]=np.sum(x[:,i])    
    #print(suma)
    maximo=max(suma)
    for i in range(0,4):
        if suma[i]==maximo:
            ind=i
    aciertos=max(suma)    
    return ind,aciertos