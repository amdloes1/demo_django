from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from demo_show.models import *

# Create your views here.
@csrf_exempt
def home_method(request):
   if request.method =='POST':
    user_name = request. POST.get("uname")
    user_age = request.POST.get("uage")
    user_city = request.POST.get("ucity")
    user_model = my_user(name = user_name, age= user_age, city = user_city)
    user_model.save()
    my_user_info = my_user.objects.values()
    my_home_template = loader.get_template('index.html') 
    content = {
    'Myheading':'Welcome to my Modeling Page',
    'my_para': 'We contact you',
    'kidsPictures':'Send your kids pictures',
    'name': 'user_name',
    'age' : 'user_age',
    }
    return HttpResponse(my_home_template.render(content))
   else:
       user_info = my_user.objects.all().values()
      
       my_home_template = loader.get_template('index.html') 
       content = {
      'Myheading':'Welcome to my Modeling Page',
      'my_para': 'We contact you',
      'kidsPictures':'Send your kids pictures',
      'name': 'user_name',
      'age' : 'user_age',
      }
       return HttpResponse(my_home_template.render(content))


 
def about_view(request):
    my_home_template = loader.get_template('about_us.html')
    my_context ={
        "my_text": "This is about us",
        "my_number": 41698888888,
        "my list":[123,456,789]

    }
    return render (request, "about_us.html", my_context)