
Simple Smart API for KYC
------

Installation
------
install python3.5
sudo update-alternatives --config python3
pip install cmake
https://github.com/ageitgey/face_recognition/issues/120
sudo easy_install pip or
sudo easy_install3 pip
export LC_ALL=C


Cd folder 
virtualenv venv
source venv/bin/activate
pip3 install flask
pip3 install face_recognition
pip3 install opencv-python
pip3 install imutils

pip3 install pytesseract
(on OSX make sure install - brew install tesseract)


Running
------

http://localhost:5000/textImage?known=/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg

http://localhost:5000/faceVideo?known=/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg&unknown=/Users/mfstech/PROJECT/unknown_face/video.mp4

http://localhost:5000/faceImage?known=/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg&unknown=/Users/mfstech/PROJECT/unknown_face/siapa3.jpg


Deployment

*#!/bin/bash


cd /apps/ekyc/
source venv/bin/activate
gunicorn -w 5 -b 0.0.0.0:5000 server:app &

