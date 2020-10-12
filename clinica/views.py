#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.template import loader
from django.http import HttpResponse

@login_required(login_url="/login/")
#class IndexView(TemplateView):
 #   template_name = 'index.html'
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
