from django import forms 
import datetime
class TestForm(forms.Form):
    name=forms.CharField()
    fatrer_name=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree=forms.BooleanField()
    datefild=forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    
    BIRTH_YEAR_CHOICES = ['230', '1992', '2003']
    birth_day=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    email =forms.EmailField(required=False)
    day=forms.DateTimeField(initial=datetime.date.today)
    roll_number=forms.IntegerField(help_text="Enter Minimum 6 digit")
    password = forms.CharField(widget = forms.PasswordInput()) 



