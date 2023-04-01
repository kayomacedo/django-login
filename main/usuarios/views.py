from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as login_django , logout
from django.contrib.auth.decorators import login_required
from usuarios.models import Question


def cadastro(request):

    if request.method =='GET':
        return render (request,'cadastro.html')
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        #Verificando se existe o usuário no banco de dados
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Ja existe esse usuário")
        
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()

            return HttpResponse("Usuário cadastrado com sucesso!")
        


def login(request):

    
    if request.method =='GET':
        
        return render(request,'login.html')
    
    else:
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user= authenticate(username=username,password=password)

        if user:
            login_django(request,user)
            return redirect('home')
        else:
            return HttpResponse('Email ou senha inválidos')

@login_required
def plataforma(request):

    #if request.user.is_authenticated:
    return HttpResponse('Plataforma')
    
    #return HttpResponse("Você precisa estar logado!")

@login_required
def home(request):
    #pegar dados das perguntas
    #perguntas =Question.objects.all()
    #pegando nome do usuário
    #username =request.user.username
    return render(request,'home.html',{'perguntas':perguntas})

def perguntas(request):
    #pegar dados das perguntas
    perguntas =Question.objects.all()
    #pegando nome do usuário
    username =request.user.username
    return render(request,'pergunta.html',{'perguntas':perguntas})


def usuarios(request):
    #pegar dados das perguntas
    usuarios =User.objects.all()
    #pegando nome do usuário
    #username =request.user.username
    return render(request,'usuarios.html',{'usuarios':usuarios})


def logout_view(request):
    logout(request)
    return redirect('login')



def about(request):
    
    return render(request,'about.html')

