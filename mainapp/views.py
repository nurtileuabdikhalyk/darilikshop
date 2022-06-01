from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, DariShopterForm, ScientistsForm
from .models import DariShopter, Scientists
from django.views.generic import DeleteView, UpdateView


def index(request):
    context = {'title': 'Басты бет'}
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {'title': 'Біз туралы'}
    return render(request, 'mainapp/about.html', context)


def dariler(request):
    dariler = DariShopter.objects.all()
    context = {'title': 'Дәрішөптер', 'dariler': dariler}
    return render(request, 'mainapp/dariler.html', context)


def daridetails(request, slug):
    question = get_object_or_404(DariShopter, slug=slug)
    context = {'dari': question, 'title': question.name}
    return render(request, 'mainapp/daridetails.html', context)


def dari_create(request):
    form = DariShopterForm()
    context = {
        'form': form,
    }
    return render(request, 'mainapp/dari_create.html', context)


def adddari(request):
    if request.method == 'POST':
        form = DariShopterForm(request.POST)
        if form.is_valid():

            form = form.save(commit=False)
            form.save()
            return redirect('dariler')


class DariDeleteView(DeleteView):
    model = DariShopter
    template_name = 'mainapp/dariler-delete.html'
    success_url = '/dariler/'


class DariUpdateView(UpdateView):
    model = DariShopter
    template_name = 'mainapp/dari_create.html'
    form_class = DariShopterForm


def scientists(request):
    scientists = Scientists.objects.all()
    context = {'title': 'Ғалымдар', 'scientists': scientists}
    return render(request, 'mainapp/scientists.html', context)


def scientist_create(request):
    if request.method == 'POST':
        form = ScientistsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scientists')

    form = ScientistsForm()
    context = {
        'form': form,
    }
    return render(request, 'mainapp/scientist_create.html', context)


def scientistsdetails(request, slug):
    question = get_object_or_404(Scientists, slug=slug)
    context = {'scientist': question, 'title': question.name}
    return render(request, 'mainapp/scientistsdetails.html', context)


class ScientistsUpdateView(UpdateView):
    model = Scientists
    template_name = 'mainapp/scientist_create.html'
    form_class = ScientistsForm


class ScientistsDeleteView(DeleteView):
    model = Scientists
    template_name = 'mainapp/scientist-delete.html'
    success_url = '/scientists/'


def scientist_or_dari(request):
    context = {'title': 'Дәрішөп н/е ғалымдар', }
    return render(request, 'mainapp/scientist_or_dari.html', context)


def contact(request):
    form = ReviewForm()
    context = {'title': 'Контактілер', 'form': form}
    return render(request, 'mainapp/contact.html', context)


def addreview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('home')
