from django import forms


class PostForm(forms.Form):
    photo = forms.ImageField()
    comment = forms.CharField(widget=forms.TextInput)

