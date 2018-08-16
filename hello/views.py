from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .nlp import sentiment

from .models import Greeting

# Create your views here.
def index(request):
    q = request.GET.get('input')
    print("query= "+q)
    # q=q.split("/")
    if q :
        data = sentiment(q)
        # print(data)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Request param expected.")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

# changes

