from django import forms
from .models import Stud, Project

class StudForm(forms.ModelForm):
    topic = forms.CharField(max_length=100)
    languages_used = forms.CharField(max_length=200)
    duration = forms.CharField(max_length=50)

    class Meta:
        model = Stud
        fields = ['fname', 'lname', 'email', 'joining_date']

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
            Project.objects.create(
                student=student,
                topic=self.cleaned_data['topic'],
                languages_used=self.cleaned_data['languages_used'],
                duration=self.cleaned_data['duration']
            )
        return student