from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistrationForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     obj = form.save(commit=Flase)
    #     obj.created_by = self.request.user
    #     return super(PlaceFormView, self).form_valid(form)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('post_list')


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('post_list')


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        user = self.request.user
        profile = self.request.user.profile

        context['profile'] = profile
        context['profile_form'] = ProfileForm(instance=profile)
        context['user_form'] = UserForm(instance=user)

        return context

    # def get(self, request, *args, **kwargs):

    #     profile = self.request.user.profile
    #     user = self.request.user

    #     profile_form = ProfileForm(instance=profile)
    #     user_form = UserForm(instance=user)

    #     return self.render_to_response({'profile_form': profile_form, 'user_form': user_form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            profile_form = ProfileForm(
                request.POST, request.FILES, instance=request.user.profile)
            user_form = UserForm(request.POST, instance=request.user)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile', pk=self.request.user.profile.pk)
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)

        return request
