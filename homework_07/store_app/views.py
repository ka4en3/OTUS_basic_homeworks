from django.http import HttpResponse


def index(request):
    return HttpResponse(
        f"<p>Main page</p>Request: {request.user}<br>GET:<br>{request.GET}<br>META:<br>{request.META}"
    )


def about(request):
    return HttpResponse("Testing Django. Otus Basic. Implementation of Store app.")
