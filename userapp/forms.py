from django import forms

# from userapp.models import PlantList


from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']