from django.shortcuts import render





def home(request):
	return render(request, "home.html", {})

def about(request):
	from pages.namer import namer
	return render(request, "about.html", {"my_stuff":namer })

def contact(request):
	return render(request, "contact.html", {})

def videos(request):
	return render(request, "videos.html", {})

def gigs(request):
	return render(request, "gigs.html", {})

def login(request):
	return render(request, "login.html", {})