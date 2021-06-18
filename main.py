import cv2 as cv
import time
import math

def vid_cap():
    crowd   =   "/home/somnerd/crowd1.jpeg"
    face = "/home/somnerd/face.jpeg"
    couple = "young_couple.jpg"
    test_face = ("crowd.jpeg")

    frame = cv.imread("three_people.jpg")
    #video   =   cv.VideoCapture(1)

    face_cascade    =   cv.CascadeClassifier("haarcascade_frontalface_default.xml")

    while True:
            a = 0       #a frame counter
            #check , frame = video.read()   #video input

            #the faces variable are of type numpy.ndarray

            gray_frame    =   cv.cvtColor(frame,cv.COLOR_BGR2GRAY)  #turns the image into grayscale so the cpu has less load
            faces   =   face_cascade.detectMultiScale(gray_frame,scaleFactor  =   1.3,minNeighbors   =   3) #detects the faces based on the parameter we gave it
            i = 0
            for x,y,w,h in faces:
                frame   =   cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)   #draws a rectangle around the face

                converted_faces = face_convert(faces)   #converts the faces variable into an int list so its more maliable
                coords  =  face_coords(converted_faces)                   #finds the faces coords
                depth =  face_depth(converted_faces)          #finds the faces depth

                true_distance(converted_faces,coords,depth)


            cv.imshow("Capturing",frame)                #prints the frame
            a+=1        #increase the frame counter at the end of every loop
            key = cv.waitKey(1)


            if key == ord(' '):
                break

    print('l36 frames:',a)
    video.release()
    cv.destroyAllWindows

def face_convert(faces):
    face_list = []
    for x,y,w,h in faces:
        x   =   int(x)
        y   =   int(y)
        w   =   int(w)
        h   =   int(h)
        face_list.append([x,y,w,h])
    return face_list

def face_depth(faces):

#sum((x+(x+w))/2) , sum((y+y)/2))   horizontal coordinates
#sum((x+x)/2) , sum((y+(h+y))/2))   vertical coordinates


    if len(faces) > 1:
        for i in range(0,len(faces)):
            face_dif = (sum(faces[i+1])/sum(faces[i]))*10
            i+=1
            face_dif_depth = int(face_dif/100 * 56)
            return face_dif_depth

def face_coords(faces):
    coord = []
    for i in range(0,len(faces)-1,1):

        x   =   faces[i][0]
        y   =   faces[i][1]
        w   =   faces[i][2]
        h   =   faces[i][3]


        coord.append(x + (x+w)/2)
        coord.append(y + (h+y)/2)

    return coord

def true_distance(faces,coords,depth):
        for i in range(0,len(faces)-1,2):

            x   =   faces[i][0]
            y   =   faces[i][1]
            w   =   faces[i][2]
            h   =   faces[i][3]

            coords_dif = (coords[i+1]+y/coords[i]+x)*1
            distance = int(coords_dif/100 * 56)
            i+=1

            true_distance = math.sqrt(distance**2 + depth ** 2)
            true_distance = int(true_distance/100 * 56)
            #print("true distance :",true_distance,"cm")
            if true_distance < 200 :
                print("==========WARNING=========="
                    '\n'
                    "PEOPLE DETECT WITHIN :",true_distance,"CM OF EACH OTHER")
                print('\a')

#Opensource trueDistance_Covid_Assist_Tool

cv.VideoCapture(1).release
#cam_detect()
#cam_port=0
vid_cap()
