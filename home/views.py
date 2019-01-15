from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'page_title' : 'Home',
    }
    return render(request, template_name='index.html', context=context)

def papers(request):
    context = {
        'page_title' : 'Papers',
    }
    return render(request, template_name='papers.html', context=context)