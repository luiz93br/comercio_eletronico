from django.shortcuts import render
from django.http import HttpResponse

def nintendoSwitch(request):
	return render(request,"nintendoSwitch.html")
def ps4(request):
	return render(request,"ps4.html")
def index(request):
	return render(request,"index.html")
def login(request):
	return render(request,"login.html")
def xboxOne(request):
	return render(request,"xboxOne.html")
def cadastro(request):
	return render(request,"cadastro.html")