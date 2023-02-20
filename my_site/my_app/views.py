from django.shortcuts import render

# Create your views here.
def exmaple_view(request):
    return render(request, 'my_app/example.html')