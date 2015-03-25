from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from braces import views

from . import forms


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class SignUpView(
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin,
    generic.CreateView
):
    form_class = forms.RegistrationForm
    form_valid_message = "You've signed up, go ahead and log in!"
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class LoginView(
    views.AnonymousRequiredMixin,
    views.FormValidMessageMixin,
    generic.FormView
):
    form_class = forms.LoginForm
    form_valid_message = "You are logged in now."
    success_url = reverse_lazy('home')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(
    views.LoginRequiredMixin,
    views.MessageMixin,
    generic.RedirectView
):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out.")
        return super(LogOutView, self).get(request, *args, **kwargs)
