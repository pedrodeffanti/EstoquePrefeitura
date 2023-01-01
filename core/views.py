from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import ItemForms, AtivoForms, SaidaForms
from .models import itemModels, ativoModels, saidaModels

@login_required()
def ItemViews(request):
    form = ItemForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = ItemForms
    return render(request, 'item.html', {'form': form})

@login_required()
def listItemViews(request):
    item = itemModels.objects.all()
    return render(request, 'listitem.html', {'item': item})

@login_required()
def alterItemViews(request, id):
    item = itemModels.objects.get(id=id)
    form = ItemForms(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('listitem.html')

    return render(request, 'item.html', {'form': form, 'item': item})

@login_required()
def deleteItemViews(request, id):
    item = itemModels.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('listitem.html')
    return render(request, 'itemdelete.html', {'item': item})

@login_required()
def AtivoViews(request):
    form = AtivoForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = AtivoForms
    return render(request, 'ativo.html', {'form': form})

@login_required()
def listAtivosViews(request):
    ativo = ativoModels.objects.all()
    return render(request, 'listativos.html', {'ativos': ativo})

@login_required()
def alterAtivoViews(request, id):
    ativo = ativoModels.objects.get(id=id)
    form = AtivoForms(request.POST or None, instance=ativo)
    if form.is_valid():
        form.save()
        return redirect('listativos.html')

    return render(request, 'ativo.html', {'form': form, 'ativo': ativo})

@login_required()
def deleteAtivoViews(request, id):
    ativo = ativoModels.objects.get(id=id)

    if request.method == 'POST':
        ativo.delete()
        return redirect('listativos.html')
    return render(request, 'ativodelete.html', {'item': ativo})

@login_required()
def SaidaViews(request):
    form = SaidaForms(request.POST or None)
    if form.is_valid():
        form.save()
        form = SaidaForms
    return render(request, 'saida.html', {'form': form})

@login_required()
def listSaidaViews(request):
    saida = saidaModels.objects.all()
    return render(request, 'listsaida.html', {'saida': saida})