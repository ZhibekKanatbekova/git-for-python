from django.shortcuts import render, HttpResponse

def homepage(request):
  return HttpResponse("Hello, lazy girl")

def test(request):
  return render(request, "test.html")