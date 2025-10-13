from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Atiniz")
    email = forms.EmailField(label = "Emailiniz")
    message = forms.CharField(widget=forms.Textarea, label="Xabariniz")



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('view_count', 'created_at', 'updated_at')
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "content": forms.Textarea(attrs={'class': 'form-control'}),
            "is_published": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            "user": forms.Select(attrs={'class': 'form-select'}),
            "tags": forms.SelectMultiple(attrs={'class': 'form-select'}),     
            "category": forms.Select(attrs={'class': 'form-select'}),
                  
        }