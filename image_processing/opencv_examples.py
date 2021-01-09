import glob
import time
from pathlib import Path

import cv2


def read_image():
    img = cv2.imread("images/galaxy.jpg", 0)
    print(type(img))
    print(img)
    print(img.shape)
    print(img.ndim)

    cv2.imshow("Galaxy", img)
    cv2.waitKey(2000)
    resized_img1 = cv2.resize(img, (1000, 500))
    cv2.imshow("Galaxy resized", resized_img1)
    cv2.waitKey(2000)
    resized_img2 = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
    cv2.imshow("Galaxy resized ratio", resized_img2)
    cv2.imwrite("images/galaxy_resized.jpg", resized_img2)
    cv2.waitKey(2000)

    cv2.destroyAllWindows()


def read_images_exercise():
    available_files = glob.glob("images/*.jpg")
    for fn in available_files:
        filename = Path(fn).stem
        img = cv2.imread(fn, 0)
        cv2.imshow(filename, img)
        cv2.waitKey(2000)
        resized_img = cv2.resize(img, (100, 100))
        cv2.imshow(f"{filename} resized", resized_img)
        cv2.waitKey(2000)
        cv2.imwrite(f"images100x100/resized_{filename}.jpg", resized_img)
        cv2.destroyAllWindows()


def face_detection():
    face_cascade = cv2.CascadeClassifier("face_detection/haarcascade_frontalface_default.xml")
    img = cv2.imread("face_detection/news.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

    print(type(faces))
    print(faces)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
        cv2.imshow("face marked", img)
        cv2.waitKey(1000)

    resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

    cv2.imshow("Gray", resized)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


def capture_video():
    video = cv2.VideoCapture(0)
    a = 0
    while True:
        a += 1
        check, frame = video.read()
        print(check)
        print(frame)
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow(f"Capturing", gray_img)

        # time.sleep(1)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    print(f"frames {a}")
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # read_image()
    # read_images_exercise()
    # face_detection()
    capture_video()
    pass
