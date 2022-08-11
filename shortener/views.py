from django.shortcuts import redirect, render
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')


def shorten(request):
    if request.method == 'POST':
        url = request.POST['link']
        #uid = str(uuid.uuid4())[:5]
        #new_url = Url(link=url, uuid=uid)
        # new_url.save()
        newLink, created = Url.objects.get_or_create(
            link=url, defaults={'uuid': str(uuid.uuid4())[:5]})
        return HttpResponse(newLink.uuid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
