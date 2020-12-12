from django import forms

from common.BootstrapFormMixin import BootstrapFormMixin
from paintings.models import Painting


class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control ',
            }
        )
    )


class PaintingForm(forms.ModelForm, BootstrapFormMixin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for (_, field) in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Painting
        exclude = ('user', )
        # fields = '__all__'
        widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }

    def clean_price(self):
        price = self.cleaned_data.get('price', False)
        if price < 0:
            raise forms.ValidationError('Price cannot be negative')
        return price

class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascending'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(
        required=False,
    )
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )
