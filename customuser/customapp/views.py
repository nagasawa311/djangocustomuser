from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Todo


@login_required
def home(request):
	user = request.user
	return render(request,"home.html",{"user":user})


def signup(request):
	if request.method=="POST":
		username2=request.POST["username"]
		password2=request.POST["password"]
		if username2 and password2 :
			try:
				User.objects.get(username=username2)
				return render(request,"signup.html",{"error":"this user has already been registered"})
			except:
				user = User.objects.create_user(username2, '', password2)
				user.save()
				user2 = authenticate(request, username=username2, password=password2)
				login(request,user2)
				return redirect("home")
		else:
			return render(request,"signup.html",{"error":"fill the blank"})

	else:
		return render(request,"signup.html",{})

def signin(request):
	if request.method=="POST":
		username2=request.POST["username"]
		password2=request.POST["password"]
		user = authenticate(request, username=username2, password=password2)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return render(request,"signin.html",{"error":"there is no user"})
	else:
		return render(request,"signin.html",{})

@login_required
def log_out(request):
	logout(request)
	return redirect("signin")

@login_required
def list(request):
	login_user = request.user
	if request.method == 'POST':
		todo2=request.POST["todo"]
		u=User.objects.get(username=login_user)
		u.save()
		t=Todo(user=u,task=todo2)
		t.save()
		return redirect("list")
	else:
		t=Todo.objects.filter(user=login_user)
		task=[]
		for item in t:
			task.append(item)

		return render(request,"list.html",{"user":login_user,"task":task})



@login_required
def delete(request):
	item=request.POST["item"]
	
	task=Todo.objects.filter(task=item)
	task.delete()
	return redirect("list")
