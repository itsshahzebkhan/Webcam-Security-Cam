# step 1 - to run this project you need to install PyCharm community edition and VS Code
# step 2 - you need to install a package from your terminal called "cv2" and then import it as shown
# step 3 - you need to import a built in package called "winsound" as shown
# stap 4 - start coding


import cv2
import winsound


webcam = cv2.VideoCapture(0)

while True:
    _, im1 = webcam.read()
    _, im2 = webcam.read()
    diff = cv2.absdiff(im1, im2)

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        if cv2.contourArea(c) < 5000:

            continue

        winsound.Beep(500, 100)

    cv2.imshow("Security Camera", thresh)

    if cv2.waitKey(10) == 27:

        break


webcam.release()

cv2.destroyAllWindows()
