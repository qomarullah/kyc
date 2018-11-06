
Simple Smart API for KYC
------

Installation
------
Cd folder 

virtualenv venv

source venv/bin/activate

pip install flask

Pip install make

pip install face_recognition

pip install opencv-python

pip install imutils

pip install pytesseract
(make sure install - brew install tesseract)


Running
------

http://localhost:5000/textImage?known=/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg

http://localhost:5000/faceVideo?known=/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg&unknown=/Users/mfstech/PROJECT/unknown_face/video.mp4

http://localhost:5000/faceImage?known=/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg&unknown=/Users/mfstech/PROJECT/unknown_face/siapa3.jpg


