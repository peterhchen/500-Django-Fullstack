from django.http import HttpResponse
from django.template import loader
from .models import Album

def index (request):
    all_albums = Album.objects.all()
    template = loader.get_template ('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))
    #all_album = Album.objects.all()
    # html = ''
    # for album in all_album:
    #     url = '/music/' + str (album.id) +'/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    # return HttpResponse(html)

def detail(reques, album_id):
    return HttpResponse ("<h2>details for Album id: " + str (album_id) + "</h2>")