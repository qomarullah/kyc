
Simple Smart API for KYC
------

Installation
------
install python3.5
sudo update-alternatives --config python3

sudo easy_install pip or
sudo easy_install3 pip
export LC_ALL=C


Cd folder 

virtualenv venv

source venv/bin/activate

pip install flask

pip install cmake
https://github.com/ageitgey/face_recognition/issues/120

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


