from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import url_type
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def all(request):
    if request.method == 'POST':
        url_long = request.POST["url_long"]
        url_short = request.POST["url_short"]
        c = url_type(url_long = url_long, url_short = url_short)
        c.save()

    out = ""
    out += '<form action="" method="POST">\n'
    out += 'original: <input type="text" name="url_long">\n'
    out += '<br>short: <input type="text" name="url_short">\n'
    out += '<br><input type="submit" value="SEND">\n'
    out += '</form>'


    url_list = url_type.objects.all()
    out += "<ul>\n"
    for row in url_list:
        out += "<li><a href=/" + row.url_short +  " > " + row.url_short + "</a></li>\n"
    out += "</ul\n"
        
    return HttpResponse(out)


def info (request, resource):
    out = ''
    try:
        show = url_type.objects.get(url_short=resource)
        out += show.url_short
        out += " = "
        out += "<a href=" + show.url_long + ">" + show.url_long + "</a>\n" 
    except url_type.DoesNotExist:
        out += "does not exist yet in DB, " 
        out += "<a href=/> click here to add </a>\n"
    return HttpResponse (out)

def notfound (request, resource):
    out = ("Not found: " + resource)
    return HttpResponseNotFound(out)

