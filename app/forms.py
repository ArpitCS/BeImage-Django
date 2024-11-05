from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'style': 'width: 100%; text-align: center; padding: 60px 50px; outline: 2px solid lightgray; border-radius: 10px'}), label="")
    category = forms.CharField(widget=forms.TextInput(attrs={'style': 'padding: 4px 12px; border-radius: 25px; border:none; outline:1px solid rgb(73, 72, 157); color:rgb(73, 72, 157);', 'placeholder':'Enter the Categories!'}), label="")
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':'', 'category':'Enter the Category'}

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields.pop('is_favorite')

class ToggleFavoriteForm(forms.Form):
    pass