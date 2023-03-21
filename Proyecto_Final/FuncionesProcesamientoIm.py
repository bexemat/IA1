import numpy as np
import matplotlib.pyplot as plt 
import cv2

def CortaImagen(Img):
    img=cv2.cvtColor(Img,cv2.COLOR_RGB2BGR)
    minx=10000000
    miny=10000000
    maxx=0
    maxy=0
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            val=img[i,j]
            if(val[0]!=(255)):
                if(j<minx):
                    minx=j
                elif(i<miny):
                    miny=i
                elif(j>maxx):
                    maxx=j
                elif(i>maxy):
                    maxy=i
    imgs=img[miny:maxy,minx:maxx]
    return imgs

def ExtraeCaracteristicasColores(img,BGR):
    for i in range(0,len(img)):
        car=cv2.mean(img[i])
        for j in range(0,BGR.shape[1]):
            BGR[i,j]=car[j]


def ImagenBinaria2RGB(ImgOriginal,ImgBinaria,cant,dirCarpeta):      
    for z in range(0,cant):
        ImgB=ImgBinaria[z]
        ImO=ImgOriginal[z]
        img=np.zeros((ImO.shape[0],ImO.shape[1],3),np.uint8)  
        for i in range(0,ImO.shape[0]):
            for j in range(0,ImO.shape[1]):
                #print('valor de imagen binaria :',naranja[i,j])
                if(ImgB[i,j]==0):
                    img[i,j]=(255,255,255)
                    #print('valor de imagen modificada ',img[i,j])
                elif(ImgB[i,j]==255):
                    img[i,j]=ImO[i,j]
                    #print('valor de imagen modificada ',img[i,j])
        dir=dirCarpeta+str(z)+'.png'
        img=CortaImagen(img)
        cv2.imwrite(dir,img)

def CargaArchivos(archivosCargados,dirArch,img_frutas):
    for x in range(0,len(archivosCargados)):
        dirArchivo=dirArch+archivosCargados[x]    
        imgBGR=cv2.imread(dirArchivo)
        imgRGB=cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        img_frutas.append(imgRGB) 
          
def MuestraImg(img_frutas):
     for x in range(0,len(img_frutas)):
            plt.subplot(5,5,x+1)
            plt.imshow(img_frutas[x]) 
def BinarizaImg(imgs,rango1,rango2,imagenSalida):
    for i in range(0,len(imgs)):
        img=cv2.cvtColor(imgs[i],cv2.COLOR_RGB2BGR)
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, rango1, rango2)
        img=cv2.medianBlur(mask,15)
        # if i==0:
        #     plt.figure()
        #     plt.imshow(img)
        #     plt.title('Imagen procesada sin eliminar huecos')
        r,img1=cv2.threshold(img,0,255,cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
        retval,labels,stats,centroids=cv2.connectedComponentsWithStats(img1)
        areamin=10000
        for i in range(0,retval):
            area=stats[i,cv2.CC_STAT_AREA]    
            if area < areamin:
                indices=np.where(labels==i)
                img1[indices]=0
        img2=img1.copy()
        h,w=img2.shape
        mask=np.zeros((h+2,w+2),np.uint8)
        cv2.floodFill(img2,mask,(0,0),255)
        inv=cv2.bitwise_not(img2)
        sinhueco=img1 | inv
        imagenSalida.append(sinhueco)

def ExtraeMomentosHu(ImagenesProcesadas,huMom):
    for i in range(0,len(ImagenesProcesadas)):
        # Calculate Moments
        gris=cv2.cvtColor(ImagenesProcesadas[i],cv2.COLOR_RGB2GRAY)
        moment = cv2.moments(gris) 
        # Calculate Hu Moments
        huMoment_ban= cv2.HuMoments(moment)
        for j in range(0,7):
            huMom[i,j]=huMoment_ban[j]

def GraficaCaract3d(Caracteristicas1,Caracteristicas2,Caracteristicas3,Caracteristicas4,m1,m2,m3,titulo):    
    ax =plt.subplot(projection='3d')
    plt.title(titulo,fontdict={'family':'serif','color':'darkblue','weight':'bold','size':18})
    for i in range(Caracteristicas1.shape[0]-1):        
        marcar='o'
        color='blue'
        ax.scatter(xs=Caracteristicas1[i,m1],ys=Caracteristicas1[i,m2],zs=Caracteristicas1[i,m3],c=color,s=100,marker=marcar)
        marcar='v'
        color='red'
        ax.scatter(xs=Caracteristicas2[i,m1],ys=Caracteristicas2[i,m2],zs=Caracteristicas2[i,m3],c=color,s=100,marker=marcar)
        marcar='*'
        color='green'
        ax.scatter(xs=Caracteristicas3[i,m1],ys=Caracteristicas3[i,m2],zs=Caracteristicas3[i,m3],c=color,s=100,marker=marcar)
        marcar='p'
        color='yellow'
        ax.scatter(xs=Caracteristicas4[i,m1],ys=Caracteristicas4[i,m2],zs=Caracteristicas4[i,m3],c=color,s=100,marker=marcar)
    plt.legend(['bananas','naranjas','limones','tomates'])
     
def GraficaCaract2d(Caracteristicas1,Caracteristicas2,Caracteristicas3,Caracteristicas4,m1,m2,titulo):
    ax =plt
    ax.title(titulo,fontdict={'family':'serif','color':'darkblue','weight':'bold','size':18})
    for i in range(Caracteristicas1.shape[0]-1):        
        marcar='o'
        color='blue'
        ax.scatter(x=Caracteristicas1[i,m1],y=Caracteristicas1[i,m2],c=color,s=100,marker=marcar)
        marcar='v'
        color='red'
        ax.scatter(x=Caracteristicas2[i,m1],y=Caracteristicas2[i,m2],c=color,s=100,marker=marcar)
        marcar='*'
        color='green'
        ax.scatter(x=Caracteristicas3[i,m1],y=Caracteristicas3[i,m2],c=color,s=100,marker=marcar)
        marcar='p'
        color='yellow'
        ax.scatter(x=Caracteristicas4[i,0],y=Caracteristicas4[i,1],c=color,s=100,marker=marcar)
        
def ArchivosPalgoritmo(bananasProcesadas,caracteristicas,huMoment_bananas,huMoment_naranjas,huMoment_limones,huMoment_tomates,nCaracteristicas,m1,m2,m3):#1,3,6
    i=0
    while(i<len(bananasProcesadas)*4):
        if nCaracteristicas==7:
            if(i<len(bananasProcesadas)):
                caracteristicas[i,0]=huMoment_bananas[i,0]
                caracteristicas[i,1]=huMoment_bananas[i,1]
                caracteristicas[i,2]=huMoment_bananas[i,2]
                caracteristicas[i,3]=huMoment_bananas[i,3]
                caracteristicas[i,4]=huMoment_bananas[i,4]
                caracteristicas[i,5]=huMoment_bananas[i,5]
                caracteristicas[i,6]=huMoment_bananas[i,6]
            elif(i>=len(bananasProcesadas) and i<(len(bananasProcesadas)*2)):
                caracteristicas[i,0]=huMoment_naranjas[i-len(bananasProcesadas),0]
                caracteristicas[i,1]=huMoment_naranjas[i-len(bananasProcesadas),1]
                caracteristicas[i,2]=huMoment_naranjas[i-len(bananasProcesadas),2]
                caracteristicas[i,3]=huMoment_naranjas[i-len(bananasProcesadas),3]
                caracteristicas[i,4]=huMoment_naranjas[i-len(bananasProcesadas),4]
                caracteristicas[i,5]=huMoment_naranjas[i-len(bananasProcesadas),5]
                caracteristicas[i,6]=huMoment_naranjas[i-len(bananasProcesadas),6]
              
            elif(i>=(len(bananasProcesadas)*2) and i<(len(bananasProcesadas)*3)):
                caracteristicas[i,0]=huMoment_limones[i-(2*len(bananasProcesadas)),0]
                caracteristicas[i,1]=huMoment_limones[i-(2*len(bananasProcesadas)),1]
                caracteristicas[i,2]=huMoment_limones[i-(2*len(bananasProcesadas)),2]
                caracteristicas[i,3]=huMoment_limones[i-(2*len(bananasProcesadas)),3]
                caracteristicas[i,4]=huMoment_limones[i-(2*len(bananasProcesadas)),4]
                caracteristicas[i,5]=huMoment_limones[i-(2*len(bananasProcesadas)),5]
                caracteristicas[i,6]=huMoment_limones[i-(2*len(bananasProcesadas)),6]
                
            elif(i>=(len(bananasProcesadas)*3) and i<(len(bananasProcesadas)*4)):
                caracteristicas[i,0]=huMoment_tomates[i-(3*len(bananasProcesadas)),0]
                caracteristicas[i,1]=huMoment_tomates[i-(3*len(bananasProcesadas)),1]
                caracteristicas[i,2]=huMoment_tomates[i-(3*len(bananasProcesadas)),2]
                caracteristicas[i,3]=huMoment_tomates[i-(3*len(bananasProcesadas)),3]
                caracteristicas[i,4]=huMoment_tomates[i-(3*len(bananasProcesadas)),4]
                caracteristicas[i,5]=huMoment_tomates[i-(3*len(bananasProcesadas)),5]
                caracteristicas[i,6]=huMoment_tomates[i-(3*len(bananasProcesadas)),6]

                
        if nCaracteristicas==3:
            if(i<len(bananasProcesadas)):
                caracteristicas[i,0]=huMoment_bananas[i,m1]
                caracteristicas[i,1]=huMoment_bananas[i,m2]
                caracteristicas[i,2]=huMoment_bananas[i,m3]
                
            elif(i>=len(bananasProcesadas) and i<(len(bananasProcesadas)*2)):
                caracteristicas[i,0]=huMoment_naranjas[i-len(bananasProcesadas),m1]
                caracteristicas[i,1]=huMoment_naranjas[i-len(bananasProcesadas),m2]
                caracteristicas[i,2]=huMoment_naranjas[i-len(bananasProcesadas),m3]
                
            elif(i>=(len(bananasProcesadas)*2) and i<(len(bananasProcesadas)*3)):
                caracteristicas[i,0]=huMoment_limones[i-(2*len(bananasProcesadas)),m1]
                caracteristicas[i,1]=huMoment_limones[i-(2*len(bananasProcesadas)),m2]
                caracteristicas[i,2]=huMoment_limones[i-(2*len(bananasProcesadas)),m3]
                
            elif(i>=(len(bananasProcesadas)*3) and i<(len(bananasProcesadas)*4)):
                caracteristicas[i,0]=huMoment_tomates[i-(3*len(bananasProcesadas)),m1]
                caracteristicas[i,1]=huMoment_tomates[i-(3*len(bananasProcesadas)),m2]
                caracteristicas[i,2]=huMoment_tomates[i-(3*len(bananasProcesadas)),m3]
              
        if nCaracteristicas==2:  
            if(i<len(bananasProcesadas)):
                caracteristicas[i,0]=huMoment_bananas[i,m1]
                caracteristicas[i,1]=huMoment_bananas[i,m2]
                            
            elif(i>=len(bananasProcesadas) and i<(len(bananasProcesadas)*2)):
                caracteristicas[i,0]=huMoment_naranjas[i-len(bananasProcesadas),m1]
                caracteristicas[i,1]=huMoment_naranjas[i-len(bananasProcesadas),m2]
              
                
            elif(i>=(len(bananasProcesadas)*2) and i<(len(bananasProcesadas)*3)):
                caracteristicas[i,0]=huMoment_limones[i-(2*len(bananasProcesadas)),m1]
                caracteristicas[i,1]=huMoment_limones[i-(2*len(bananasProcesadas)),m2]
               
            elif(i>=(len(bananasProcesadas)*3) and i<(len(bananasProcesadas)*4)):
                caracteristicas[i,0]=huMoment_tomates[i-(3*len(bananasProcesadas)),m1]
                caracteristicas[i,1]=huMoment_tomates[i-(3*len(bananasProcesadas)),m2]
                
        i=i+1


