import math
import cv2
import copy

class Neuron():

    def __init__(self):
        self.entradas = []
        self.list_pesos = []
        self.salida = 0
        self.LR = 0.5

    def calculate(self):
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        return SR
    
    def calculate_final_neuron(self,row):
        lista_pesos_fn = []
        x = float()
        for i in range(len(self.entradas)):
            x = x + float(self.entradas[i]*self.list_pesos[i])
        SR = 1/(1+(math.e)**(-x))
        error = row[-1] - SR
        epsilon = SR*(1-(SR))*error

        for i in range(len(self.entradas)):
            gen_delta = self.LR*self.entradas[i]*epsilon
            w_gen = self.list_pesos[i] + gen_delta
            lista_pesos_fn.append(w_gen)

        return SR, epsilon, lista_pesos_fn, error
    
    def calculate_pesos(self, df):
        lista_pesos_nuevos = []
        for i in range(len(self.list_pesos)):
                gen_soc = self.salida * (1 - (self.salida)) * df
                delta_gen_soc = self.LR * self.entradas[i] * gen_soc
                peso = delta_gen_soc + self.list_pesos[i]
                lista_pesos_nuevos.append(peso)
        return lista_pesos_nuevos

class Task_images():

    def read_images():
        image_pixels = []
        pixel_list = []
        persona = True
        path = "C:/Users/ivanf/OneDrive/Escritorio/Facultad/4Ano/int-artificial/tp7/fotos2.0/"
        for i in range(6):
            img = cv2.imread( path + str(i) + ".jpg", 0)
            ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) 
            pixel_list.clear()
            pixel_list.append(int(1)) 
            for j in range(len(img)):
                for k in range(len(img[j])):
                    px = img[j][k]
                    if px == 0:
                        pixel_list.append(int(0))
                    else:
                        pixel_list.append(int(1))    
            if persona:
                pixel_list.append(int(0))
                persona = False
            else:
                pixel_list.append(1)
                persona = True
            image_pixels.append(copy.deepcopy(pixel_list))
        return image_pixels

    def read_pesos():
        list_pesos_hl = []
        list_pesos_fn = []
        with open('pesos_co.txt', 'r') as pesos:
            for line in pesos:
                list_pesos_hl.append(float(line))
        with open('pesos_fn.txt', 'r') as pesos:
            for line in pesos:
                list_pesos_fn.append(float(line))
        return (list_pesos_hl),(list_pesos_fn)


    

        
        

                



    
