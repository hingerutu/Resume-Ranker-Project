from django.shortcuts import render
from .models import Resume, Pyresume
from .forms import resumeForm, UserRegistrationForm, pyForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

@login_required
def apply(request):
    if request.method == "POST":
        form = resumeForm(request.POST, request.FILES)
        if form.is_valid():
           
            resume_instance = form.save(commit=False)  
            skills = form.cleaned_data.get('skills') or [] 

          
            resume_instance.score = len(skills)  
           
            resume_instance.user = request.user  

            
            resume_instance.save()

            return redirect('greet') 
    else:
        form = resumeForm() 

   
    return render(request, 'apply.html', {'form': form})
     


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('portal')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'form':form})



def resume_list(request):
    queues = Resume.objects.all().order_by('-score', '-CGPA')
    return render(request, 'resume_list.html', {'queues': queues})


def view_resume(request, session_id):
    session = get_object_or_404(Resume, id=session_id)
    return render(request, 'view_resume.html', {'session': session})




def resume_view(request):
    if request.method == 'POST':
        form = resumeForm(request.POST, request.FILES)
        if form.is_valid():
           
            resume_instance = form.save(commit=False) 
            skills = form.cleaned_data.get('skills')

           
            resume_instance.score = len(skills) 

           
            resume_instance.save()

            return redirect('resume_list')  
    else:
        form = resumeForm()

    return render(request, 'resumeForm.html', {'form': form})




def portal(request):
    return render(request, 'registration/portal.html')


@login_required
def pyapply(request):
    if request.method == "POST":
        form = pyForm(request.POST, request.FILES)
        if form.is_valid():
          
            resume_instance = form.save(commit=False) 
            skills = form.cleaned_data.get('skills') or [] 

            
            resume_instance.score = len(skills) 
            
            
            resume_instance.user = request.user

           
            resume_instance.save()

            return redirect('greet2')
    else:
        form = pyForm()
    return render(request, 'pyapply.html', {'form':form})



def greet(request):
    return render(request, 'greet.html')



def pylist(request):
    queues = Pyresume.objects.all().order_by('-score', '-CGPA')
    return render(request, 'pylist.html', {'queues': queues})


def view_resume2(request, session_id):
    session = get_object_or_404(Pyresume, id=session_id)
    return render(request, 'rem_view.html', {'session': session})



def greet2(request):
    return render(request, 'greet2.html')