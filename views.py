from django.conf import settings
from django.shortcuts import render_to_response
from blog.models import post,link
from django.conf import settings

def defaults(request):
    posts = post.objects.all().order_by('-time')[0:5]
    title = settings.SITE_NAME
    links = link.objects.all()
    return render_to_response('index.html',{
        'posts':posts,
        'SITE_NAME':title,
	'links':links,
	'index':'http://'+request.get_host()+'/',
        })

def article(request,num):
    NO = str(num)
    links = link.objects.all()
    value = post.objects.select_related().get(id=int(NO)) 
    title = settings.SITE_NAME
    return render_to_response('blog.html',{
	'post':value,
	'SITE_NAME':title,
	'links':links,
	'index':'http://'+request.get_host()+'/',
	})

def page(request,num):
    num = int(num)
    sub = num-1
    index = request.get_host()
    title = settings.SITE_NAME
    max = len(post.objects.all())
    links = link.objects.all()
    if max > 5*num:
        posts = post.objects.all().order_by('-time')[5*num-5:5*num]
    else:
        posts = post.objects.all().order_by('-time')[5*num-5:max]
    return render_to_response('page.html',{
	'posts':posts,
	'SITE_NAME':title,
	'index':'http://'+request.get_host()+'/',
	'page_no':num,
	'page_no_sub':sub,
	'index':index,
	'links':links
	})
