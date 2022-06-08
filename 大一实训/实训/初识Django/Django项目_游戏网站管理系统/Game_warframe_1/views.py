from random import random

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from Game_warframe_1.models import user


def index(request):
	return HttpResponse("你好，这里是方法index")




def name(request):
	return HttpResponse("你好，这里是方法name")

def vote(request,question_id):
	return HttpResponse('这里是方法操作 %s.' %question_id)

def add_user(request):
	User = user()
	User.u_Name = '张三 2'
	User.u_PassWord = 'X123 2'
	User.save()
	return render(request,'Game_warframe_1/index.html')

def select_user(request):
	Users = user.objects.all()
	for i in Users:
		print(i.u_Name,i.u_PassWord)
	context = {
		'name':i.u_Name,
		'password':i.u_PassWord,
		'Users':Users
	}
	#return render(request,'Game_warframe_1/index.html',context=context)
	return  render(request,'Game_warframe_1/index.html')
