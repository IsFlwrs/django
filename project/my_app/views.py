from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from django.http import Http404
from django.shortcuts import get_object_or_404
# create your views here
#@login_required
def index(request):
    #print(dir(request))
    #if not request.user.is_autheticated():
     #   print('ñoñoñoñoñoñ')
    if True:
        greet = 'hi'
        #person = models.Person.objects.get(id=1)
        person = get_object_or_404(models.Person, id=1)
        name = person.name

        #return HttpResponse('Hello Word__')
        return render(request, 'index.html', {'object':greet, 'name':name})
    else:
        raise http404('Uoops esto es embarasozo')

#baseView
from django.views  import View
class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'greey':'Hola', 'name':'saja'})

    def post(self, request):
        return render(request, 'index.html', {
            'greey':'Recibi post', 'name':''
        })

    
    def update(self, request):
        return render(request, 'index.html', {
            'greey':'Recibi update', 'name':''
        })

from django.views.generic.base import TemplateView
#templateView
class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
            context = super(HomeTemplateView, self).get_context_data(**kwargs)
            context['greet'] = 'hello desde template view'
            return context


#generic view
'''
    ellos ya traen un template por default
    model_detail.html
'''
from django.views.generic.detail import DetailView

class PersonDetailView(DetailView):
    model = models.Person
    template_name = 'detail.html'

from django.views.generic.list import ListView
#@login_required
class PersonList(ListView):
    model = models.Person
    template_name = 'list.html'


#createView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class PersonCreate(CreateView):
    model = models.Person
    fields = ['name', 'email', 'program', 'age']
    template_name = 'create.html'
    succes_url = reverse_lazy('list')
    

#update view
from django.views.generic.edit import UpdateView
class PersonUpdate(UpdateView):
    model = models.Person
    fields = ['name', 'email']
    template_name = 'create.html'
    succes_url = reverse_lazy('list')

#delete View
from django.views.generic.edit import DeleteView
class PersonDelete(DeleteView):
    model = models.Person
    template_name = 'delete_confirm.html'
    succes_url = reverse_lazy('list')