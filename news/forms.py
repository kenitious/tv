from django import forms


# Create your forms here.

class ContactForm(forms.Form):
    names = forms.CharField(max_length=50)
    #phone = forms.IntegerField()
    subject = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
