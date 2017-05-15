import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

def home(request):
    print(request)
    print(request.user)
    print(request.path)
    # return HttpResponse("Hello")
    return render(request, "home.html", {})

class HomeView(View):
    def get(self, request, *aerg, **kwargs):

        context = {
            "name": "Eisuke",
            "random_number": random.randint(500, 1000)
        }
        return render(request, "home.html", context)

    # def post(self, request, *aerg, **kwargs):
    #     return HttpResponse("Hello")
    #
    # def put(self, request, *aerg, **kwargs):
    #     return HttpResponse("Hello")
    #
    # def delete(self, request, *aerg, **kwargs):
    #     return HttpResponse("Hello")
