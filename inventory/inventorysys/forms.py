from django import forms

from .models import *


class LaptopForm(forms.ModelForm):
    class Meta:
        model = laptop
        fields = ('type', 'price', 'company', 'status')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = desktop
        fields = ('type', 'price', 'company', 'status')


class MouseForm(forms.ModelForm):
    class Meta:
        model = mouse
        fields = ('type', 'price', 'company', 'status')


class PendriveForm(forms.ModelForm):
    class Meta:
        model = pendrive
        fields = ('type', 'price', 'company', 'status')


class DiskForm(forms.ModelForm):
    class Meta:
        model = disk
        fields = ('type', 'price', 'company', 'status')
