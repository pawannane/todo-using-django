from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from .models import todo

# Create your views here.
def home(request):
    if request.method == "POST":
        user = request.user
        task = request.POST["todo"]

        new_todo = todo.objects.create(user=user, task=task)
        new_todo.save()

    todos = todo.objects.filter(user=request.user)
    return render(request, 'index.html', {'todos': todos})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # the authentication was successful, we can sign in the user.
            auth.login(request, user)
            return redirect('home')
        
    return render(request, 'login.html')

def register_user(request):
    if request.POST:
        # Get the user information from the form
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST['email']
        password = request.POST['password']

        data = User.objects.create_user(first_name=firstname, last_name=lastname, password=password, username=email)
        data.save()

        return redirect('login')
    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect("home")


def delete_todo(request, id):
    # delete todo from todos
    myTodo = todo.objects.get(id=id)
    myTodo.delete()
    return redirect('home')

def update_todo(request, id):
    myTodo = todo.objects.get(id=id)
    myTodo.completed = not myTodo.completed
    myTodo.save()
    return redirect('home')