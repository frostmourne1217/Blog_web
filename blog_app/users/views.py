from django.shortcuts import render, redirect
from .forms import RegForm
from django.contrib.auth import authenticate, login

def register(request):
	if request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			users = authenticate(request, username = username, password = password)
			login(request,users)
			return redirect('blog-home')
	else:
		form = RegForm()

	context = {'form': form}
	return render(request, 'users/register.html', context)