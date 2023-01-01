from django import forms

from core.models import itemModels, ativoModels, saidaModels

class ItemForms(forms.ModelForm):
    class Meta:
        model = itemModels
        fields = '__all__'

class AtivoForms(forms.ModelForm):
    class Meta:
        model = ativoModels
        fields = '__all__'

class SaidaForms(forms.ModelForm):
    class Meta:
        model = saidaModels
        fields = '__all__'