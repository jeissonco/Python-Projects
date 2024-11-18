import cv2
from pyzbar import pyzbar



#Object that records the video
camera = cv2.VideoCapture(0)

#Create a loop while the capture of the video is open
while camera.isOpened():
    ret,frame = camera.read()
    if not ret:
        break

    #save the barcodes that the camera can check and store on barcodes
    barcodes = pyzbar.decode(frame)


    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), ( x + w, y + h), (0, 255, 0), 2)
        barcode_value = barcode.data.decode('utf-8')
        cv2.putText(frame, barcode_value, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    cv2.imshow('Barcode Scanner', frame)
    if cv2.waitKey(1) % 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()