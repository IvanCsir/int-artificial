import cv2
import copy

def read_images():
        image_px = []
        pixel_list = []
        persona = True
        images_path = "/home/ivan/Escritorio/hdd/Facultad/int-artificial/tp6/fotos1.0/"
        for i in range(10):
            img = cv2.imread(images_path + str(i) + ".jpg", cv2.COLOR_RGB2GRAY)
            pixel_list.clear()
            pixel_list.append(1) #Agrego Vias a la entrada
            for j in range(len(img)):
                for k in range(len(img[0])):
                    px = img[j][k][1]
                    pixel_list.append(px/255)
                    

            # Agrego salida esperada para persona A o B
            if persona:
                pixel_list.append(int(0))
                persona = False
            else:
                pixel_list.append(1)
                persona = True
            image_px.append(copy.deepcopy(pixel_list))
        return image_px
    
if __name__ == '__main__':
    read_images()