import numpy as np
import matplotlib.pyplot as plt
import random
from ExtraeCaract import *
from FuncionesAlgoritmos import *

class KMEANS():
    def __init__(self, k=4, max_iter=100, error=0.001):
        self.k=k
        self.max_iter=max_iter
        self.error=error
    def Agrupa(self,X):
        self.datos=X
        self.n_datos=X.shape[0]
        self.centroides=np.zeros((self.k,X.shape[1]))     
    #inicia centroides con datos aleatorios obtenidos de los datos de muentra del entrenamiento
        for i in range(0,self.k):            
            centroid=random.randint(int((i)*(self.n_datos/self.k)),int((i+1)*(self.n_datos/self.k)))          
            self.centroides[i,:]=self.datos[centroid,:]     
    #crea grupos y calcula la distancia a cada centroide y asigna clase a cada valor
        self.grupos=np.zeros(self.n_datos)
        self.DistanciaGrupos=np.zeros((self.n_datos,self.k))
        err=10000
        cont=0
        while(self.error<err or cont>self.max_iter) :
            CalculaDistanciaAsignaGrupos(self.n_datos,self.DistanciaGrupos,self.grupos,self.datos,self.centroides,self.k)         
        #calcula nuevo centroide
            self.nuevoCentroide=NuevoCentroide(self.grupos,self.k,self.n_datos,self.datos)           
        #grafico los puntos y el nuevo centroide
            GraficaKmeans(self.grupos,self.datos,self.nuevoCentroide,cont,'Resultado del Algoritmo Kmeans implementado por mi ')
        #calculo el error
            err=Error(self.centroides,self.nuevoCentroide)
            #print('Error en la iteracion : '+str(cont)+' = '+str(err))
            self.centroides=self.nuevoCentroide
            cont=cont+1
        return self.grupos,self.centroides,cont
def Euclideana(x,y):
    return np.sqrt(np.sum(x-y)**2)
def Error(cenAct,cenNue):
    return np.abs(np.sum((cenNue-cenAct)/(cenAct)))
def CalculaDistanciaAsignaGrupos(cantDatos,distanciaGrupo,grupos,X,centroides,k):
    for i in range(0,cantDatos):
            for j in range(0,k):
                distanciaGrupo[i,j]=Euclideana(X[i,:],centroides[j,:])
            grupos[i]=min(distanciaGrupo[i,:])
def NuevoCentroide(grupos,k,cantDatos,x):  
    nuevoCentro=np.zeros((k,x.shape[1]))  
    ind1=[]
    ind2=[]
    ind3=[]
    ind4=[]    
    for i in range(0,cantDatos):
        if grupos[i]==0:
            ind1.append(i)
        elif grupos[i]==1:
            ind2.append(i)
        elif grupos[i]==2:
            ind3.append(i)
        elif grupos[i]==3:
            ind4.append(i)
    g1=np.zeros((len(ind1),x.shape[1]))
    g2=np.zeros((len(ind2),x.shape[1]))
    g3=np.zeros((len(ind3),x.shape[1]))
    g4=np.zeros((len(ind4),x.shape[1]))
    for i in range(0,len(ind1)):
        g1[i,:]=x[ind1[i],:]
    for i in range(0,len(ind2)):
        g2[i,:]=x[ind2[i],:]
    for i in range(0,len(ind3)):
        g3[i,:]=x[ind3[i],:]
    for i in range(0,len(ind4)):
        g4[i,:]=x[ind4[i],:]
   
    for j in range(0,x.shape[1]):
        nuevoCentro[0,j]=np.mean(g1[:,j])
    for j in range(0,x.shape[1]):
        nuevoCentro[1,j]=np.mean(g2[:,j])
    for j in range(0,x.shape[1]):
        nuevoCentro[2,j]=np.mean(g3[:,j])
    for j in range(0,x.shape[1]):
        nuevoCentro[3,j]=np.mean(g4[:,j])    
    return nuevoCentro
