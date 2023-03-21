from Definiciones import *

CargaArchivos(narCargadas,dirNar,img_naranjas)
CargaArchivos(limCargados,dirLim,img_limones)
CargaArchivos(banCargadas,dirBan,img_bananas)
CargaArchivos(tomCargados,dirTom,img_tomates)

CargaArchivos(narCargadasTest,dirNarTest,img_naranjas_test)
CargaArchivos(limCargadosTest,dirLimTest,img_limones_test)
CargaArchivos(banCargadasTest,dirBanTest,img_bananas_test)
CargaArchivos(tomCargadosTest,dirTomTest,img_tomates_test)

CargaArchivos(narCargadasC,dirNarC,img_naranjas_cortadas)
CargaArchivos(limCargadosC,dirLimC,img_limones_cortadas)
CargaArchivos(banCargadasC,dirBanC,img_bananas_cortadas)
CargaArchivos(tomCargadosC,dirTomC,img_tomates_cortadas)

CargaArchivos(narCargadasCTest,dirNarCTest,img_naranjas_test_cortadas)
CargaArchivos(limCargadosCTest,dirLimCTest,img_limones_test_cortadas)
CargaArchivos(banCargadasCTest,dirBanCTest,img_bananas_test_cortadas)
CargaArchivos(tomCargadosCTest,dirTomCTest,img_tomates_test_cortadas)

BinarizaImg(img_naranjas,naranjaClaro,naranjaOscuro,naranjasProcesadas)
BinarizaImg(img_limones,amarilloClaro,amarilloOscuto,limonesProcesadas)
BinarizaImg(img_bananas,amarilloClaro,amarilloOscuto,bananasProcesadas)
plt.show()
BinarizaImg(img_tomates,rojoClaro,rojoOscuro,tomatesProcesadas)

BinarizaImg(img_naranjas_test,naranjaClaro,naranjaOscuro,naranjasProcesadasTest)
BinarizaImg(img_limones_test,amarilloClaro,amarilloOscuto,limonesProcesadasTest)
BinarizaImg(img_bananas_test,amarilloClaro,amarilloOscuto,bananasProcesadasTest)
BinarizaImg(img_tomates_test,rojoClaro,rojoOscuro,tomatesProcesadasTest)


"""
    Extrae la parte de la fruta de las imagenes originales con las imagenes binarizadas y las devuelve en formato rgb y luego las corta
"""

# cant=len(img_bananas)
# ImagenBinaria2RGB(img_bananas,bananasProcesadas,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/bananasCortadas/')
# cant=len(img_limones)
# ImagenBinaria2RGB(img_limones,limonesProcesadas,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/limonesCortados/')
# cant=len(img_tomates)
# ImagenBinaria2RGB(img_tomates,tomatesProcesadas,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/tomatesCortados/')
# cant=len(img_naranjas)
# ImagenBinaria2RGB(img_naranjas,naranjasProcesadas,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/naranjasCortadas/')

# cant=len(img_bananas_test)
# ImagenBinaria2RGB(img_bananas_test,bananasProcesadasTest,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/bananasCortadas/')
# cant=len(img_limones_test)
# ImagenBinaria2RGB(img_limones_test,limonesProcesadasTest,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/limonesCortados/')
# cant=len(img_tomates_test)
# ImagenBinaria2RGB(img_tomates_test,tomatesProcesadasTest,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/tomatesCortados/')
# cant=len(img_naranjas_test)
# ImagenBinaria2RGB(img_naranjas_test,naranjasProcesadasTest,cant,'/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/naranjasCortadas/')

"""
        Extrae caracteristicas de color 
"""
BGRBananas=np.zeros((len(img_bananas_cortadas),3))
BGRNaranjas=np.zeros((len(img_naranjas_cortadas),3))
BGRLimones=np.zeros((len(img_limones_cortadas),3))
BGRTomates=np.zeros((len(img_tomates_cortadas),3))

BGRBananasTest=np.zeros((len(img_bananas_test_cortadas),3))
BGRNaranjasTest=np.zeros((len(img_naranjas_test_cortadas),3))
BGRLimonesTest=np.zeros((len(img_limones_test_cortadas),3))
BGRTomatesTest=np.zeros((len(img_tomates_test_cortadas),3))

ExtraeCaracteristicasColores(img_bananas_cortadas,BGRBananas)
ExtraeCaracteristicasColores(img_naranjas_cortadas,BGRNaranjas)
ExtraeCaracteristicasColores(img_limones_cortadas,BGRLimones)
ExtraeCaracteristicasColores(img_tomates_cortadas,BGRTomates)

ExtraeCaracteristicasColores(img_bananas_test_cortadas,BGRBananasTest)
ExtraeCaracteristicasColores(img_naranjas_test_cortadas,BGRNaranjasTest)
ExtraeCaracteristicasColores(img_limones_test_cortadas,BGRLimonesTest)
ExtraeCaracteristicasColores(img_tomates_test_cortadas,BGRTomatesTest)

"""
             Recortas las imagenes
"""
# for i in range(0,len(img_naranjas_cortadas)):
#     img_naranjas_cortadas[i]=CortaImagen(img_naranjas_cortadas[i])
# for i in range(0,len(img_bananas_cortadas)):
#     img_bananas_cortadas[i]=CortaImagen(img_bananas_cortadas[i])    
# for i in range(0,len(img_limones_cortadas)):
#     img_limones_cortadas[i]=CortaImagen(img_limones_cortadas[i])       
# for i in range(0,len(img_tomates_cortadas)):
#     img_tomates_cortadas[i]=CortaImagen(img_tomates_cortadas[i])     

# for i in range(0,len(img_naranjas_test_cortadas)):
#     img_naranjas_test_cortadas[i]=CortaImagen(img_naranjas_cortadas[i])
# for i in range(0,len(img_bananas_test_cortadas)):
#     img_bananas_test_cortadas[i]=CortaImagen(img_bananas_test_cortadas[i])    
# for i in range(0,len(img_limones_test_cortadas)):
#     img_limones_test_cortadas[i]=CortaImagen(img_limones_test_cortadas[i])       
# for i in range(0,len(img_tomates_test_cortadas)):
#     img_tomates_test_cortadas[i]=CortaImagen(img_tomates_test_cortadas[i])   
"""
        Extrae los vectores utilizados en los algoritmos de Kmeans y Knn
"""
caracteristicas3d=np.zeros((len(bananasProcesadas)*4,3))
pruebas3d=np.zeros((len(4*bananasProcesadasTest),3))
ArchivosPalgoritmo(img_bananas_test_cortadas,pruebas3d,BGRBananasTest,BGRNaranjasTest,BGRLimonesTest,BGRTomatesTest,3,0,1,2)

ArchivosPalgoritmo(img_bananas_cortadas,caracteristicas3d,BGRBananas,BGRNaranjas,BGRLimones,BGRTomates,3,0,1,2)
#print(caracteristicas3d[0],caracteristicas3d[51])
