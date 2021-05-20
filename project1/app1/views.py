from django.shortcuts import render

# import pytesseract to convert text in image to string
import pytesseract

# import summarize to summarize the ocred text
from gensim.summarization.summarizer import summarize

from .forms import ImageUpload
import os

# import Image from PIL to read image
from PIL import Image

from django.conf import settings


# Create your views here.
def index(request):
    text = ""
    
    message = ""
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                image = request.FILES['image']
                image = image.name
                path = settings.MEDIA_ROOT
                pathz = path + "/images/" + image
                im1 = Image.open(pathz)
                pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                text = pytesseract.image_to_string(im1, lang = 'eng')
                text1 = image
                

               
            except:
                message = "check your filename and ensure it doesn't have any space or check if it has any text"

    context = {
        'text': text,
        'message': message
    }
    return render(request, 'formpage.html', context)