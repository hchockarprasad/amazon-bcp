from django.http import HttpResponse


def index(request):

    return HttpResponse('This is amazon bcp dashboard')
