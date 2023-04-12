#from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Kenneth Stanley Barrientos',
            'age': 36,
            'codes': ['Python', 'Ruby', 'C#']
        }
        return render(request, 'hello_world.html', context=data)
