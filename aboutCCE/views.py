from django.shortcuts import render

from aboutCCE.models import *
from website.models import Faculty, Gallery, Hero_Image

# Create your views here.
def management_page(request):
    management_data = Management.objects.all().order_by('order')
    hero_img = Hero_Image.objects.filter(page="management").first()
    context = {
        "management_data": management_data,
         'hero_img':hero_img,
         "hero_title":'Management',
         'gallery':Gallery.objects.all(),
         }
    return render(request, 'aboutCCE/management.html',context=context)

def directors_desk_page(request):
    executive_director = Faculty.objects.filter(role__role="Executive Director").first()
    joint_director_administration = Faculty.objects.filter(role__role="Joint Director Admin").first()
    joint_director_finance = Faculty.objects.filter(role__role="Joint Director Finan").first()
    hero_img = Hero_Image.objects.filter(page="directors_desk").first()
    context = {
        "executive_director": executive_director,
        "joint_director_administration": joint_director_administration,
        "joint_director_finance": joint_director_finance,
        'hero_img':hero_img,
         "hero_title":'Director\'s Desk',
    }
    return render(request, 'aboutCCE/directors_desk.html',context) 

def principals_desk_page(request):
    hero_img = Hero_Image.objects.filter(page="principals_desk").first()
    principal = Faculty.objects.filter(role__role="Principal").first()
    vice_principal = Faculty.objects.filter(role__role="Vice Principal").first()
    context={
        'hero_title':'Principal\'s Desk',
        'hero_img':hero_img,
        'principal':principal,
        "vice_principal":vice_principal,
    }
    return render(request, 'aboutCCE/principals_desk.html',context=context)

def cce_in_media_page(request):
    hero_img = Hero_Image.objects.filter(page="cce_in_media").first()
    cce_in_media_main =  CCEinMedia.objects.all().first()
    cce_in_media_data = CCEinMedia.objects.all()[1:4]
    more_about_cce_data= MoreAboutCCE.objects.all().order_by('-date')
    context = {"cce_in_media_main":cce_in_media_main,"cce_in_media_data": cce_in_media_data,"more_about_cce_data": more_about_cce_data,'hero_img':hero_img,"hero_title":'CCE in Media',}
    return render(request, 'aboutCCE/cce_in_media.html',context=context)