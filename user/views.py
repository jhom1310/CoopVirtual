from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import Oferta
from django.core.mail import send_mail
from django.conf import settings
from reportlab.pdfgen import canvas


@login_required(login_url='/login')
def pdf(request, id):
    ofertas = Oferta.objects.get(ativacao=True, id=id)

    c = canvas.Canvas("hello.pdf")
    c.drawString(30, 800, ofertas.produto)
    c.drawString(30, 780, "Endereço:")
    c.drawString(30, 760, ofertas.endereco)
    c.drawString(30, 740, "Descrição:")
    c.drawString(30, 720, ofertas.description)
    c.save()

    return redirect('/')



def login_inicial (request):
    return render(request, 'login.html')



def cadastro (request):
    return render(request, 'register.html')


@require_POST
def cadastro_submit(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux :
            messages.error(request, 'Email ou Usuario já em uso.')
            return render(request, 'register.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
     first_name = request.POST['name']
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']

    novoUsuario = User.objects.create_user(username=username, email=email, password=password, first_name= first_name)
    novoUsuario.save()

    return redirect('/login/')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou Senha inválido.')
    return redirect('/login/')



def logout_user(request):
    logout(request)
    return redirect('/login/')



@login_required(login_url='/login')
def principal_coop(request):
    ofertas = Oferta.objects.filter(ativacao=True)
    return render(request, 'principal_coop.html', {'ofertas': ofertas})

@login_required(login_url='/login')
def meus_imoveis(request):
    ofertas = Oferta.objects.filter(ativacao=True, usuario=request.user)
    return render(request, 'principal_coop.html', {'ofertas': ofertas})

@login_required(login_url='/login')
def detalhes(request, id):
    ofertas = Oferta.objects.get(ativacao=True, id=id)

    if request.POST:
        mensagem = request.POST.get('mensagem')
        send_mail('Interesse em Imóvel - Imóveis Souza' ,
              mensagem,
              'aleff.jonathan@hotmail.com',
              ['dr.ant.madson@gmail.com'],
              fail_silently=True)
    return render(request, 'detalhes.html', {'ofertas': ofertas})

@login_required(login_url='/login')
def detalhes_submit(request, id):
    ofertas = Oferta.objects.get(ativacao=True, id=id)

    if request.POST:
        mensagem = request.POST.get('mensagem')
        proprietario = User.objects.get(username=ofertas.usuario)
        print(proprietario.email)
        send_mail('Interesse em Imóvel - Imóveis Souza' ,
              mensagem,
              'aleff.jonathan@hotmail.com',
              [proprietario.email],
              fail_silently=True)
    return redirect('/')

@login_required(login_url='/login')
def index(request):
    return render(request, 'model-header.html')

@login_required(login_url='/login')
def teste(request):
    return render(request, 'teste.html')

@login_required(login_url='/login')
def cadastro_oferta(request):
    oferta_id = request.GET.get('id')
    if oferta_id:
        oferta = Oferta.objects.get(id=oferta_id)
        if oferta.usuario == request.user:
            return render(request, 'cadastro_oferta.html',{'oferta': oferta})
    return render(request, 'cadastro_oferta.html')

@login_required(login_url='/login')
def set_oferta(request):
    produto = request.POST.get('produto')
    endereco = request.POST.get('endereco')
    valor = request.POST.get('valor')
    qtd_quartos = request.POST.get('qtd_quartos')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    conservacao = request.POST.get('conservacao')
    photo = request.FILES.get('photo')
    oferta_id = request.POST.get('oferta-id')
    usuario = request.user
    if oferta_id:
        oferta = Oferta.objects.get(id=oferta_id)
        if usuario == oferta.usuario:
            oferta.produto = produto
            oferta.endereco = endereco
            oferta.valor = valor
            oferta.qtd_quartos = qtd_quartos
            oferta.phone = phone
            oferta.description = description
            oferta.conservacao = conservacao
            if photo:
                oferta.photo = photo
            oferta.save()
    else:

        oferta = Oferta.objects.create(produto=produto,endereco=endereco,valor=valor,qtd_quartos=qtd_quartos,
                                       phone=phone,description=description,conservacao=conservacao,photo=photo, usuario=usuario)

    return redirect('/meus_imoveis')

@login_required(login_url='/login')
def delete(request, id):
    ofertas = Oferta.objects.get(id=id)
    if ofertas.usuario == request.user:
        ofertas.delete()

    return redirect('/')