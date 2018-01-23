from django import forms

class contactForm(forms.Form):
    name=forms.CharField(required=False,max_length=30,help_text='30 charactes max')
    email=forms.EmailField(required=True)
    comment=forms.CharField(required=True,widget=forms.Textarea)

