from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.http import HttpResponseRedirect
from django.views.generic import FormView


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

		if user is not None and user.is_active and user.is_staff:
			login(self.request, user)
			return redirect("index")
		else:
			return self.form_invalid(form)