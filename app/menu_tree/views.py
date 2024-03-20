from django.shortcuts import render

# Create your views here.
from .models import Menu

def index(request):
    context = Menu.objects.all()

    try:
        return render(request, 'menu_tree/index.html', context={"menus": context})
    except Exception as e:
        return "Function error: " + str(e)

def draw_menu(request, path):

    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Draw_menu function failed =')
    print(splitted_path)
    return render(request, 'menu_tree/index.html', {'menu_name': splitted_path[0],'menu_item': splitted_path[-1]})
    
