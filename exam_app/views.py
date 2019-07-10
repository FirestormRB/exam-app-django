from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect
from django.views.generic import FormView


@login_required
def home(request):
    return render(request, 'index.html')


def signupchoice(request):
	if request.method == 'POST':
		if 'teacher' in request.POST:
			#role = "Teacher"
			print("hey Teacher")
			
			return redirect('signup')
		elif 'student' in request.POST:
			#role = "Student"
			print("hey student")
			
			return redirect('signup')

	return render(request, 'signupchoice.html')





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = SignUpForm()
    #print(role)
    return render(request, 'signup.html', {'form': form})

def index(request):
	return render(request, "index.html")

class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'login.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username  = username, password = password)
		print(user.role)

		if user is not None and user.is_active:
			login(self.request, user)
			return redirect("index")
		else:
			return self.form_invalid(form)