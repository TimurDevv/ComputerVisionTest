import cv2

capture = cv2.VideoCapture('output.avi')
frameNr = 0


while (True):
    success, frame = capture.read()
    if success and frameNr % 15 == 0:
        cropped_image = frame[210:445,115:350]
        resimage = cv2.resize(cropped_image,(116,116))
        cv2.imwrite(f'dude/frame_{frameNr}.jpg',resimage)
        #cv2.imwrite(f'output/frame_{frameNr}.jpg', frame)
        print(frameNr)

    frameNr = frameNr + 1

capture.release()