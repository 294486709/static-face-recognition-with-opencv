import cv2

face_cascade = cv2.CascadeClassifier( r'./haarcascade_frontalface_default.xml')

image = cv2.imread( 'HET.jpg')
gray =  cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)
print('{0} faces founded!'.format(len(faces)))

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
cv2.imshow("Find Faces!",image)
cv2.waitKey(1)
print "Press"
