from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import *
import json
from .forms import *
from . fiilters import *
# Create your views here.
def home(request):
     
     return render(request, 'index.html',{'homeP' : True})
 
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email =request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists ')
                return redirect(register)     
            else:
                user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name, last_name=last_name) 
                user.set_password(password) 
                user.save()
                print("success")
                return redirect('login_user') 


    else:
        print("this is not post method")
        return render(request, 'register.html')

def login_user(request):
      if request.method == 'POST':
          username =request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)

          if user is not None:
              login(request, user)
              return redirect('home')
 
 
          else:
              messages.info(request, 'Invalid Email or Password')
              return redirect('login_user')
 
      else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home') 
 



# def add_interview_question(request):
#     if request.method == 'POST':
#         form = InterviewQuestionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # redirect to success page
#     else:
#         form = InterviewQuestionForm()
    
#     return render(request, 'add_interview_question.html', {'form': form})

# def display_que(request):
#     questions=InterviewQuestion.objects.all()
#     return render(request,'display_que.html',{'questions':questions})

def addIntQues(request):

    frm = QuestionForm()

    if request.method == 'POST':
        try:
            frm = QuestionForm(request.POST)
            if frm.is_valid():
                frm.save()
                messages.success(request,"Question added successfully")
                return render(request, 'forms/addquestion.html', {'form': frm})

            else:
                messages.error(request,'Invalid Input')
                return render(request, 'forms/addquestion.html', {'form': frm})

        except Exception as e:
            print(e)
            messages.error(request,'Something went wrong')
            return render(request, 'forms/addquestion.html', {'form': frm})


    return render(request, 'forms/addquestion.html', {'form': frm})

def addCatg(request):

    frm = CategoryForm()

    if request.method == "POST":
        try:
            frm = CategoryForm(request.POST)
            if frm.is_valid():
                frm.save()
                messages.success(request,"Category added successfully")
                return render(request, 'forms/addCatg.html', {'form': frm})

            else:
                messages.error(request,'Invalid Input')
                return render(request, 'forms/addCatg.html', {'form': frm})

        except Exception as e:
            print(e)
            messages.error(request,'Something went wrong')
            return render(request, 'forms/addCatg.html', {'form': frm})


    return render(request, 'forms/addCatg.html', {'form': frm})


def addAns(request):

    frm = AnswerForm()
  
    if request.method == "POST":
        try:
            frm = AnswerForm(request.POST)
            if frm.is_valid():
                frm.save()
                messages.success(request,"Answer added successfully")
                return render(request, 'forms/addAnswer.html', {'form': frm})

            else:
                messages.error(request,'Invalid Input')
                return render(request, 'forms/addAnswer.html', {'form': frm})

        except Exception as e:
            print(e)
            messages.error(request,'Something went wrong')
            return render(request, 'forms/addAnswer.html', {'form': frm})


    return render(request, 'forms/addAnswer.html', {'form': frm})


def displayQues(request):

    ans = Answers.objects.all()
    ansF = AnsFilter(request.GET, queryset = ans)
    context = {
        'ans' : ansF,
    }
    return render(request,'display_que.html',context)


def getAns(request,pk):

    ques = Questions.objects.get(id = pk)
    ansT = Answers.objects.get(ques = ques)

    answ = ansT.ans

    return JsonResponse(answ,safe=False)

def searchQuest(request):
   
        if request.method == 'POST':

            try:
                questo =  request.POST.get('searchQ')
                questt = Questions.objects.get(quest__contains = questo)
                if questt is None:
                    messages.error(request,'Such question does not exists in the database')
                    return redirect('disQues')
                ans =  Answers.objects.get(ques = questt)
                context = {
                    'ques' : questt,
                    'ans' : ans,
                    'srch' : True
                }
                return render(request,'display_que.html',context)
            except Exception as e:
                messages.error(request,'Not found')
                return redirect('disQues')

            
           

        

def searchRecmd(request):

    query = request.GET.get('searchQ')
    rcmdList = []
    if query:
        ques = Questions.objects.filter(quest__icontains = query)
        for i in ques:
            rcmdList.append(i.quest)
    return JsonResponse({'status':200 , 'data' : rcmdList})

    


        
