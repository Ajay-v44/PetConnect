from django.shortcuts import redirect, render

# Create your views here.

def index (request):
    try:
        return render(request,'base.html')
    except Exception as e:
        print(e)
        return redirect(page404)
        
def page404(request):
    return render(request, '404.html')