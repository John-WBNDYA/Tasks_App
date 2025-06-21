from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import TaskForm
from .models import Task
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here
def index(request):
    """
    Home function
    """
    return render(request, "app/index.html")


def login_view(request):
    """
    Login View for Users
    """
    
    # Check the request method
    if request.method == "POST":
        # Get the login data from the post request
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Verify user vredentials
        user = authenticate(request, username=username, password=password)
        
        # Check if the user exists
        if user is not None:
            login(request, user=user)
            return redirect("user_account")
        
    
    return render(request, "app/login.html")


def sign_up(request):
    """
    Registration View
    """
    form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid() :
            # Just save form and User will be created
            form.save()
            messages.success(request, "Account created successfully!!")
            return redirect("login")

    context = {
        "form" : form
    }
    return render(request, "app/registration.html", context=context)    


def logout_view(request):
    """
    The logout view
    """
    logout(request)
    return render(request, "app/index.html")


def user_account(request):
    """
    The user account
    """
    task = Task.objects.filter(user=request.user).order_by('-date_created')

    context = {
        'tasks' : task
    }
    return render(request, "app/user_account.html", context=context)


def add_task(request):
    """
    The page for adding tasks.
    """

    if request.method == "POST":
        task_form = TaskForm(request.POST)

        # Check if form is valid
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect(user_account)
    else:
        context = {
            'task_form' : TaskForm()
        }

        return render(request, 'app/add_task.html', context=context)
