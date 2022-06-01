from django import forms
from .models import Reviews, DariShopter, Scientists


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "title", "email", "text")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Есіміңіз"}),
            "title": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тақырыбы"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Почтаңыз"}),
            "text": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Хабарлама..."}),

        }


class DariShopterForm(forms.ModelForm):
    class Meta:
        model = DariShopter
        fields = (
            "name", "type", "anyqtama", "description", 'qoldanui', 'count', 'scientists', 'region', 'image', 'slug'
        )
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Дәрішөп аты"}),
            "anyqtama": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Анықтама"}),
            "description": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Сипаттамасы"}),
            "qoldanui": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Қолдануы"}),
            "slug": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Slug"}),
        }


class ScientistsForm(forms.ModelForm):
    class Meta:
        model = Scientists
        fields = ("name", "surname", "lauazym", "ainalasu_salasy", 'dariler', 'image', 'slug')
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Есімі"}),
            "surname": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Тегі"}),
            "lauazym": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Лауазымы"}),
            "slug": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Slug"}),
            "ainalasu_salasy": forms.TextInput(
                attrs={"class": "form-control border", "placeholder": "Айналысу саласы"}),

        }
