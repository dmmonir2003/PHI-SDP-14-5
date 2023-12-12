from django import forms 

class TestForm(forms.Form):
    name=forms.CharField()
    fatrer_name=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree=forms.BooleanField()
    datefild=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    
    BIRTH_YEAR_CHOICES = ['230', '1992', '2003']
    birth_day=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

