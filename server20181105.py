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
#import skvideo.io

print("version cv", cv2.__version__)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def index():
    return 'Bismillah'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/face')
def faceCheck():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return: the rendered template 'home.html'
    """

    #image = face_recognition.load_image_file("/Users/mfstech/PROJECT/siapa1.jpg")
    #face_locations = face_recognition.face_locations(image)
    #values = ','.join(str(v) for v in face_locations)
    #print(values)
    known = request.args.get('known')
    unknown = request.args.get('unknown')

    #known="/Users/mfstech/PROJECT/known_face/ayah.jpg"
    picture_of_me = face_recognition.load_image_file(known)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    #unknown="/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg"
    unknown_picture = face_recognition.load_image_file(unknown)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    # Now we can see the two face encodings are of the same person with `compare_faces`!
    #results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    results2 = face_recognition.face_distance([my_face_encoding], unknown_face_encoding)
    values = ','.join(str(v) for v in results2)

    """if results[0] == True:
        print("It's a picture of me!")
    else:
        print("It's not a picture of me!")
    """

    return values

@app.route('/video')
def videoCheck():
    #known is video
    known = request.args.get('known')
    unknown = request.args.get('unknown')

    picture_of_me = face_recognition.load_image_file(known)
    known_face_me = face_recognition.face_encodings(picture_of_me)[0]



    """vidcap = cv2.VideoCapture(known)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
      #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
      success,image = vidcap.read()
      print("Read a new frame:", success)
      count += 1
    """

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    vidcap = cv2.VideoCapture(unknown)
    #vidcap = skvideo.io.VideoCapture(unknown)
    #vidcap = skvideo.io.vread(unknown)

    success,image = vidcap.read()
    count = 0
    success = True
    data_path="images"

    while success:
      image = imutils.rotate(image, 90)
      img="frame"+str(count)+".png"
      cv2.imwrite(os.path.join(data_path,img), image)     # save frame as JPEG file

      """input_img_resize=cv2.resize(image, None, fx = 0.5, fy=0.5)
      small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
      # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
      rgb_small_frame = small_frame[:, :, ::-1]
      my_file = Path(os.path.join(data_path,img))
      """
      my_file = Path(os.path.join(data_path,img))
      face_load = face_recognition.load_image_file(my_file)
      face_encodings = face_recognition.face_encodings(face_load)[0]

      matches = face_recognition.compare_faces([known_face_me], face_encodings)
      name = "Unknown"

      # If a match was found in known_face_encodings, just use the first one.
      if True in matches:
        print("MATCH")
      if False in matches:
        print("NOT-MATCH")

      success,image = vidcap.read()
      count += 1

          #face_names.append(name)

    # Only process every other frame of video to save time
    """if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame
    """


    """count2=0
    img_list=os.listdir(data_path+'/')
    for img in img_list:
        my_file = Path(os.path.join(data_path,img))
        if my_file.is_file():
            input_img=cv2.imread('/Users/mfstech/python/testing/images/frame0.jpg')
            input_img_resize=cv2.resize(input_img, None, fx = 0.5, fy=0.5)
            #cv2.imwrite(os.path.join(data_path,img), input_img_resize)     # save frame as JPEG file
            print("Read a new frame:",count2)
        count2 += 1
        #small_frame = cv2.resize(input_img, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #rgb_small_frame = small_frame[:, :, ::-1]
    """
    test=str(count)
    return test

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
