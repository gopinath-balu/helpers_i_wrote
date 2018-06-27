'''to manually validate the FDDB labels which was leabelled manually '''

#import necessaries
import glob, os, cv2

#get location
image_location = '/home/gopi34/aparna/FDDB_images/'
label_location = '/home/gopi34/aparna/FDDB_labels/'
global_location = '/home/gopi34/aparna/'

#list all images and labels
image_list = [image for image in sorted(glob.glob(image_location+'*.jpg'))]
label_list = [label for label in sorted(glob.glob(label_location+'*.txt'))]

#loop all images along with it's respective labels
for image, label in zip(image_list, label_list):
    img = cv2.imread(image)
    img_height, img_width, channel = img.shape
    with open(label, 'r') as file:
        #read contents of file
        file_content = file.read()
        #strip newline binary character '/n'
        face_co_ord = file_content.split('\n')[:-1]
        #loop all face co-ord values in co-ords list
        for face in face_co_ord:
            #get all co-ord values leaving class label 1 in prefix
            bbox_vals = face.split(' ')[1:]
            #assign bbox values
            xcentre, ycentre, width, height = float(bbox_vals[0]), float(bbox_vals[1]), float(bbox_vals[2]), float(bbox_vals[3])
            #de-norm co-ord values relative to the image
            x1, y1, x2, y2 =(int((xcentre - (width/2))*img_width)),(int((ycentre - (height/2))*img_height)),(int((xcentre + (width/2))*img_width)),(int((ycentre +(height/2))*img_height))
            #draw rectangle in the image using the de-norm co-ord values
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.imshow(image, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()