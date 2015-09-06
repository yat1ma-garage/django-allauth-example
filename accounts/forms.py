from django import forms
from django.contrib.auth import get_user_model


class SignupForm(forms.Form):
    age = forms.IntegerField(label='Your age', max_value=150)
    github_url = forms.URLField(label='Your GitHub page',  max_length=255)

    class Meta:
        model = get_user_model()

    def save(self, user):
        user.age = self.cleaned_data['age']
        user.github_url = self.cleaned_data['github_url']
        user.save()
