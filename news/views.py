from django.shortcuts import render, redirect

from .forms import NewsForm, CategoryForm, CommentForm, UserForm,Comment,UserEditForm,LoginForm
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def Logout(request):
    logout(request)
    messages.info(request, "siz muvaffaqiyatli lot out qildingiz !")
    return redirect('home')



def user_edit(request):
    form = UserEditForm(instance = request.user)
    if request.POST:
        form  = UserEditForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
        return redirect ("home")
    return render(request, 'register.html', {'form': form})


def home(request):
    hammasi = News.objects.all()
    if request.POST:
        hammasi_id = request.POST['one']
        ones_news = News.objects.get(id= hammasi_id)
        
        if request.user in ones_news.likes.all():
            ones_news.likes.remove(request.user)
        
        else:
            ones_news.likes.add(request.user)     
    context= {"news":hammasi}
    return render(request, 'home.html',context)




def detail(request,id):
    a = News.objects.get(id = id)
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                izoh = form.cleaned_data['izoh'],
                user = request.user,
                news  = a 
                )
            return redirect('detail',a.id)
    return render(request,'detail.html',{"one" : a, 'form':form})


def createCategory(request):
    form  = CategoryForm()


    if request.POST:
        form =CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    return render(request, 'create_category.html', {'form':form})


def user_register(request):
    form = UserForm()

    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            parol = form.cleaned_data['password']
            user.set_password(parol)
            user.save()
            return redirect('home')
    return render(request, 'register.html',{'form':form})

# def createNew(request, id):
#     news = News.object.get(id = id)
#     form = CommentForm()

#     if request.POST:
#             form = CommentForm(request.POST)
#             if form.is_valid():
#                 news.object.create(
#                     izoh = form.cleaned_data['izoh'],
#                     user = request.user,
#                     news = news
#                 )
#             return redirect('detail',news.id)
#     return render(request,'create_comment.html', {'form':form})

def editnews(request,id):
    edit = News.objects.get(id=id)
    form = NewsForm(instance=edit)
    if request.POST:
        form = NewsForm(request.POST, files = request.FILES, instance=edit)
        if edit.is_valid():
            edit.save()
        return redirect("home")
    return render(request, 'edit.html',{'edit':edit})

def createNew(request):
    form = NewsForm()
    if request.POST:
        form  = NewsForm(request.POST,files=request.FILES)
        if form.is_valid():
            News.objects.create(
                author = request.user,            
                title = form.cleaned_data['title'],
                text = form.cleaned_data['text'],
                tur  = form.cleaned_data['tur'],
                rasm  = form.cleaned_data['rasm']
            )
        return redirect('home')
    return render(request, 'create_news.html',{'form':form})
        

def delete(request , id):
    News.objects.get(id=id).delete()
    return redirect('home')    
    

def Login(request):
    login_form = LoginForm()
    if request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username = username, password = password )
        if user is None:
            login (request, user)
            messages.succces(request,f"siz , {'user'.username},login qilindingiz !")
        return redirect('home')
    return render (request, 'login.html',{'form':login_form})