from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

class ComentariosView(View):

  def __init__(self, **kwargs) -> None:
      super().__init__(**kwargs)


  def get(self,request):

    return HttpResponse('Bienvenidos equipo al proyecto Holding')

    #return render(request,"Bienvenidos")
