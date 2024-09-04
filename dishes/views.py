from django.shortcuts import render
from django.http import HttpResponse
from dishes.models import Dishes
from django.shortcuts import redirect

def recipie(request):
    if request.method=='POST' :
        dish_image=request.FILES.get('dish_image')
        dish_name=request.POST.get('dish_name')
        dish_desc=request.POST.get('dish_desc')
        Dishes.objects.create(dish_name=dish_name,dish_desc=dish_desc,dish_image=dish_image)
    
        return redirect('/dishes/')

    Queryset=Dishes.objects.all()
    if request.GET.get('Search'):
        Queryset=Queryset.filter(dish_name__icontains=request.GET.get('Search'))

    
    return render(request,'recipies.html',context={'dish':Queryset})

def vege(request):
    return HttpResponse("JSAHJSACHSANAJXXAAK")


def Delete_dish(request,id):
    queryset=Dishes.objects.get(id=id)
    queryset.delete()
    return redirect('/dishes/')
# Create your views here.
def update_dish(request,id):
    queryset=Dishes.objects.get(id=id)

    if request.method=='POST':
        dish_image=request.FILES.get('dish_image')
        
        dish_name=request.POST.get('dish_name')
        dish_desc=request.POST.get('dish_desc')
        queryset.dish_name=dish_name
        queryset.dish_desc=dish_desc

        if dish_image:
            queryset.dish_image=dish_image
        queryset.save()
        return redirect('/dishes/')
    return render(request,'update.html',context={'dish':queryset})
 
