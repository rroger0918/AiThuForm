from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django import forms
from WIN.models import student
from WIN.forms import PostForm

def home(request):
    return render(request,'index.html')

def post1(request):  #新增資料，資料不作驗證
	if request.method == "POST":	  #如果是以POST方式才處理
		cName = request.POST['cName'] #取得表單輸入資料
		cPhone =  request.POST['cPhone']
		cAddr =  request.POST['cAddr']
		#新增一筆記錄
		unit = student.objects.create(cName=cName,  cPhone=cPhone, cAddr=cAddr) 
		unit.save()  #寫入資料庫
		return redirect('/index/')	
	else:
		message = '請輸入資料'
	return render(request, "post1.html", locals())	