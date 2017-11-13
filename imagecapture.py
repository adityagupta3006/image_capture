import cv2
import time
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        break
    elif k%256 == 32:
        img_name = time.strftime("%Y_%m_%d_%H-%M-%S")
        cv2.imwrite(img_name+".png", frame)
        
cam.release()
cv2.destroyAllWindows()
