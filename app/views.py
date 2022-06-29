from django.shortcuts import render

# Create your views here.
def bootstrap_cdn(request):
    return render(request,'bootstrap_cdn.html')

def bs_download(request):
    return render(request,'bs_download.html')