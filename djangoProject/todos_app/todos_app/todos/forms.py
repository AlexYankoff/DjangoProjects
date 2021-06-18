from django import forms
from django.core.exceptions import ValidationError

from todos_app.todos.models import Todo


def validate_dot(value):
    if '.' in value:
        raise forms.ValidationError('\'.\' is present in value')
#model form
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ('categories',)



class CreateTodoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        validators= [
            validate_dot,
        ]
    )
    description = forms.CharField()

    boots_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_boots_catcher(self):
        value = self.cleaned_data['boots_catcher']

        if value:
            raise ValidationError('You are a bot')


class UpdateTodoForm(CreateTodoForm):
    state = forms.BooleanField()
