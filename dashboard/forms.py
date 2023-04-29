from django import forms
from django.forms import ModelForm
from . models import *




class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    labels = {
        'name' : 'Name of the category',
        'difficultyLvl' : 'Difficulty level'

    }


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Questions
        fields = '__all__'

    labels = {
        'quest' : 'Add question text: ',
        'catg' : 'Category of the question',
        'qDiffLvl' : 'Difficulty level'

    }

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = '__all__'

    label = {
        'ques' : 'Question: ',
        'ans' : "Add answer: "
    }
