from django.shortcuts import render

# Create your views here.
def jinja_tag(request):
    d={'name':'swetha'}
    return render(request,'jinja_tag.html',d)