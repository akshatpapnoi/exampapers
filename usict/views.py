from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse

from .forms import BranchForm

# Create your views here.

def main(request):
	if request.method == 'POST':
		degree =  request.POST['degree']
		branch =  request.POST['branch']
		semester =  request.POST['semester']
		
		return redirect('usict:papers', degree=degree, branch=branch, semester=semester )

	else:
		context ={
			'page_title': 'USICT',
		}
		return render(request, template_name='usict/main.html', context=context)

def papers(request, degree, branch, semester):
	return HttpResponse("papers")
