from django.db import models
from django.contrib.auth.models import User

class InterviewQuestion(models.Model):
    CATEGORY_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('CNND','CNND')
    ]

    DIFFICULTY_LEVEL_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]

    question_text = models.TextField(null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,null=True)
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_LEVEL_CHOICES,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

class InterviewSession(models.Model):
    """Model for storing interview sessions"""
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interview_sessions')
    interviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interviewee_sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.interviewer.username} interviewing {self.interviewee.username}"

class InterviewAnswer(models.Model):
    """Model for storing interview answers"""
    session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(InterviewQuestion, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer_text[:50]

    
