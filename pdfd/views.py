from django.shortcuts import render,get_object_or_404
from .models import notices
from .scraping_utils import download_pdf
from django.http import FileResponse
def index(request):
    url = 'https://iost.tu.edu.np/notices/'
    download_pdf(url)
    names=notices.objects.all()
    return render(request, 'pdfd/index.html',{'names':names})


def pindex(request,pdfs_id):  
    pdf = get_object_or_404(notices, pk=pdfs_id)
    response = FileResponse(pdf.pdf_content,content_type='application/pdf')
    return response