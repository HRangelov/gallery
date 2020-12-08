from django import forms
from paintings.models import Painting


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            }
        )
    )


class PaintingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Painting
        # fields = ''
        # exclude = ('user', )
        fields = '__all__'
        widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }
