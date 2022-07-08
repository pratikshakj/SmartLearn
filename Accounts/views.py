from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import Registrationform,Profileform,Register
from django.contrib import messages
from  .models import profile
from django.contrib.auth.decorators import login_required
from .randgenrator import rand
from .decarators import unauthenticated_user
# Create your views here.
@unauthenticated_user
def register(request):
	if request.POST:
		form=Registrationform(request.POST)
		if(form.is_valid()):
			username=form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username}')
			b=form.save()
			u_id=rand(8)
			a=profile(user=b,Uid=u_id)
			a.save()
			return redirect('/accounts/registeration',{'messages':messages})
	else:
		form=Registrationform()


	return render(request, 'adhyayana.html',{'form':form})
@login_required
def registration(request):
	client=profile.objects.get(user=request.user).Uid
	if request.POST:
		form1=Register(request.POST,instance=request.user)
		form2=Profileform(request.POST,instance=request.user.profile)
		if form2.is_valid():
			form1.save()
			form2.save()
			messages.success(request,f'Registration Complete!!' )
			return redirect('home')

	else:
		form1=Register(instance=request.user)
		form2=Profileform(instance=request.user.profile)

	return render(request,'registration.html',{'form1':form1,'form2':form2,'uid':client})

def userlogout(request):
	logout(request)
	return redirect('home')