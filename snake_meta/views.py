from django.shortcuts import render
from .resources import SerpienteResource
# Create your views here.

def export(request):
    resource = SerpienteResource()
    dataset = resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="serpientes.csv"'
    return response
