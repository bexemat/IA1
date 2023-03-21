from FuncionesProcesamientoIm import *
import os

"""
                    Direcciones de las imagenes capturas
"""
dirNarC='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/naranjasCortadas/'
dirLimC='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/limonesCortados/'
dirBanC='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/bananasCortadas/'
dirTomC='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/tomatesCortados/'

dirNarCTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/naranjasCortadas/'
dirLimCTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/limonesCortados/'
dirBanCTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/bananasCortadas/'
dirTomCTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/tomatesCortados/'


dirNar='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/naranjas/'
dirLim='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/limones/'
dirBan='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/bananas/'
dirTom='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Entrenamiento/tomates/'

dirNarTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/naranjas/'
dirLimTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/limones/'
dirBanTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/bananas/'
dirTomTest='/home/matias/Escritorio/ProyectoIA/ImagenesProyecto/Test/tomates/'




"""
                    Guarda los archivos de la direccion leida anteriormente
"""
tomCargados=os.listdir(dirTom)
narCargadas=os.listdir(dirNar)
limCargados=os.listdir(dirLim)
banCargadas=os.listdir(dirBan)

tomCargadosTest=os.listdir(dirTomTest)
narCargadasTest=os.listdir(dirNarTest)
limCargadosTest=os.listdir(dirLimTest)
banCargadasTest=os.listdir(dirBanTest)


tomCargadosC=os.listdir(dirTomC)
narCargadasC=os.listdir(dirNarC)
limCargadosC=os.listdir(dirLimC)
banCargadasC=os.listdir(dirBanC)

tomCargadosCTest=os.listdir(dirTomCTest)
narCargadasCTest=os.listdir(dirNarCTest)
limCargadosCTest=os.listdir(dirLimCTest)
banCargadasCTest=os.listdir(dirBanCTest)
"""
                    Guarda las imagenes de los archivos de la direccion leida anteriormente
"""
img_naranjas=[]
img_limones=[]
img_bananas=[]
img_tomates=[]

img_naranjas_test=[]
img_limones_test=[]
img_bananas_test=[]
img_tomates_test=[]

img_naranjas_cortadas=[]
img_limones_cortadas=[]
img_bananas_cortadas=[]
img_tomates_cortadas=[]

img_naranjas_test_cortadas=[]
img_limones_test_cortadas=[]
img_bananas_test_cortadas=[]
img_tomates_test_cortadas=[]

"""
                    Rangos de colores hsv para segmentar las imagenes
"""
naranjaClaro= (0, 100, 50)
naranjaOscuro=(21, 255, 230)
amarilloClaro = (18, 100, 50)
amarilloOscuto=(41, 255, 230)
rojoClaro = (1, 100, 50)
rojoOscuro=(10, 255, 230)
"""
                    Imagenes listas para extraer caracteristicas
"""
naranjasProcesadas=[]
limonesProcesadas=[]
bananasProcesadas=[]
tomatesProcesadas=[]

naranjasProcesadasTest=[]
limonesProcesadasTest=[]
bananasProcesadasTest=[]
tomatesProcesadasTest=[]


   
