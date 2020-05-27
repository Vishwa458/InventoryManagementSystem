from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, mixins
from .forms import *
from .serializers import LaptopSerializer
from .models import *

# Create your views here.

class LaptopViewset(viewsets.ModelViewSet):
    queryset = laptop.objects.all()
    serializer_class = LaptopSerializer

def index(request):
    return render(request, 'index.html')


def display_device(request, cls, hdr):
    items = cls.objects.all()
    context = {
        'items': items,
        'header': hdr
    }
    return render(request, 'index.html', context)


def laptops(request):
    return display_device(request, laptop, 'laptops')


def desktops(request):
    return display_device(request, desktop, 'desktops')


def pendrives(request):
    return display_device(request, pendrive, 'pendrives')


def mouses(request):
    return display_device(request, mouse, 'mouses')


def disks(request):
    return display_device(request, disk, 'disks')


'''def laptops(request):
    items= laptop.objects.all()
    context = {
        'items' : items,
        'header': 'laptops',
    }
    return render(request, 'index.html', context)

def desktops(request):
    items= desktop.objects.all()
    context = {
        'items' : items,
        'header': 'desktops',
    }
    return render(request, 'index.html', context)

def mouses(request):
    items= mouse.objects.all()
    context = {
        'items' : items,
        'header': 'mouses',
    }
    return render(request, 'index.html', context)
    
def pendrives(request):
    items= pendrive.objects.all()
    context = {
        'items' : items,
        'header': 'pendrives',
    }
    return render(request, 'index.html', context)

def disks(request):
    items= disk.objects.all()
    context = {
        'items' : items,
        'header': 'disks',
    }
    return render(request, 'index.html', context)
'''


def add_Device(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(request.GET)
        return render(request, "add_new.html", {'form': form})


def add_Laptop(request):
    return add_Device(request, LaptopForm)


def add_Desktop(request):
    return add_Device(request, DesktopForm)


def add_Mouse(request):
    return add_Device(request, MouseForm)


def add_Pendrive(request):
    return add_Device(request, PendriveForm)


def add_Disk(request):
    return add_Device(request, DiskForm)


'''  
if request.method == "POST":
        form = DesktopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DesktopForm(request.GET)
        return render(request, "add_new.html", {'form': form})

def add_Disk(request):                             # Function based View for Disk data save and extraction
    if request.method == "POST":
        form = DiskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DiskForm(request.GET)
        return render(request, "add_new.html", {'form': form})

def add_Mouse(request):                            # Function based View for Mouse data save and extraction
    if request.method == "POST":
        form = MouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MouseForm(request.GET)
        return render(request, "add_new.html", {'form': form})

def add_Pendrive(request):
    if request.method == "POST":
        form = PendriveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PendriveForm(request.GET)
        return render(request, "add_new.html", {'form': form})
'''


def edit_Device(request, cls, pk, model):
    item = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return render(request, 'index.html', {'form': form})
    else:
        form = cls(instance=item)
        return render(request, 'edit_item.html', {'form': form})


def edit_laptop(request, pk):
    return edit_Device(request, LaptopForm, pk, laptop)


def edit_desktop(request, pk):
    return edit_Device(request, DesktopForm, pk, desktop)


def edit_mouse(request, pk):
    return edit_Device(request, MouseForm, pk, mouse)


def edit_pendrive(request, pk):
    return edit_Device(request, PendriveForm, pk, pendrive)


def edit_disk(request, pk):
    return edit_Device(request, DiskForm, pk, disk)


# Deleting items

def delete_device(request, pk, model):
    model.objects.filter(id=pk).delete()
    items = model.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)


def delete_laptop(request, pk):
    return delete_device(request, pk, laptop)


def delete_desktop(request, pk):
    return delete_device(request, pk, desktop)


def delete_mouse(request, pk):
    return delete_device(request, pk, mouse)


def delete_pendrive(request, pk):
    return delete_device(request, pk, pendrive)


def delete_disk(request, pk):
    return delete_device(request, pk, disk)
