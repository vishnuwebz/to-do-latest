from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority', 'description']
        widgets = {
            'due_date': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'priority': forms.Select(attrs={'class':'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter task title'})
        self.fields['priority'].widget.attrs.update({'class':'form-select'})
