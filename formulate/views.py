from django.shortcuts import render, get_object_or_404,redirect

from .models import Formulate

# Create your views here.
def formulate_list(request):
    formulates = Formulate.objects.all().order_by('published_date')
    return render(request, 'formulate/formulate_list.html', {'formulates':formulates})

def formulate_detail(request, pk):
    formulate = get_object_or_404(Formulate, pk=pk)
    return render(request, 'formulate/formulate_details.html', {'formulate': formulate})
