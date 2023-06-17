from django.http import HttpResponse
from django.shortcuts import render
import pytesseract
from PIL import Image
import html
def extract_details(image):
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text

def upload_invoice(request):
    if request.method == 'POST':
        image = request.FILES['invoice_image']
        scheduled_time = request.POST['scheduled_time']
        
        temp_image = Image.open(image)
        
        extracted_details = extract_details(temp_image)
        extracted_details_html = html.escape(extracted_details).replace('\n', '<br>')
       
        print(extracted_details)
        return render(request, 'success.html',{'extracted_details':extracted_details_html})
    
    return render(request, 'upload.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")