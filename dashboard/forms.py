from django import forms
from .models import InterviewQuestion

class InterviewQuestionForm(forms.ModelForm):
    class Meta:
        model = InterviewQuestion
        fields = ['question_text', 'category', 'difficulty_level', 'is_active']

    question_text = forms.CharField(
        label='Question Text',
        widget=forms.Textarea(attrs={'rows': 3})
    )
    category = forms.ChoiceField(choices=InterviewQuestion.CATEGORY_CHOICES)
    difficulty_level = forms.ChoiceField(choices=InterviewQuestion.DIFFICULTY_LEVEL_CHOICES)
    is_active = forms.BooleanField(required=False)
