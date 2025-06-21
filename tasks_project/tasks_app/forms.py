from django import forms
from tasks_app.models import Task

# Form 
class TaskForm(forms.ModelForm):
    class Meta:
        model =Task
        fields = ['title', 'description', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }
        labels = {
            'title'       : 'Task Title',
            'description' : 'Task Description',
            'priority'    : 'Priority Level',
            'due date'    : 'Due Date',
        }