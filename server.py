from flask import (
    Flask,
    request
    #render_template
)
import face_recognition
import array as arr
import cv2
import os
from pathlib import Path
import imutils
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def index():
    return 'Bismillah'



@app.route('/textImage')
def textImage():

    known = request.args.get('known')
    text = pytesseract.image_to_string(Image.open(known))
    return text

@app.route('/faceImage')
def faceImage():

    known = request.args.get('known')
    unknown = request.args.get('unknown')

    picture_of_me = face_recognition.load_image_file(known)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!
    unknown_picture = face_recognition.load_image_file(unknown)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    # Now we can see the two face encodings are of the same person with `compare_faces`!
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    #results2 = face_recognition.face_distance([my_face_encoding], unknown_face_encoding)
    #values = ','.join(str(v) for v in results2)

    """if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")
    """
    #return values
    return str(results[0])

@app.route('/faceVideo')
def faceVideo():

    #known is video
    known = request.args.get('known')
    unknown = request.args.get('unknown')

    picture_of_me = face_recognition.load_image_file(known)
    known_face_me = face_recognition.face_encodings(picture_of_me)[0]

    # Initialize some variables
    count = 0
    found = 0
    success = True

    vidcap = cv2.VideoCapture(unknown)
    #play first
    success,image = vidcap.read()

    while success:
      image = imutils.rotate(image, 90)
      face_encodings = face_recognition.face_encodings(image)[0]
      matches = face_recognition.compare_faces([known_face_me], face_encodings)
      # If a match was found in known_face_encodings, just use the first one.
      if True in matches:
        #print("MATCH")
        found += 1
      #if False in matches:
        #print("NOT-MATCH")
      if found>10:
        break
      #play next
      success,image = vidcap.read()
      count += 1

    resp = False
    if(found/count>0.5):
        resp = True

    return str(resp)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
