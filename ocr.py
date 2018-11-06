try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



# Simple image to string
print(pytesseract.image_to_string(Image.open('/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg')))

#print(pytesseract.image_to_string(Image.open('/Users/mfstech/PROJECT/known_face/ktp2.jpg')))
#print(pytesseract.image_to_data(Image.open('/Users/mfstech/PROJECT/known_face/ktp2.jpg')))

print(pytesseract.image_to_osd(Image.open('/Users/mfstech/PROJECT/known_face/ktp2.jpg')))

print(pytesseract.image_to_osd(Image.open('/Users/mfstech/PROJECT/known_face/ayah-ktp.jpg')))
