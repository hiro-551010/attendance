from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from accounts.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm

class Login(LoginView):
    template_name = 'accounts/auth.html'

    def form_valid(self, form):
        messages.success(self.request,'ログイン完了しました')
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,'エラーがありました')
        return super().form_invalid(form)

def signup(request):
    context = {}
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            user.save()
            login(request, user)
            messages.success(request,'登録完了しました')
            return redirect('/')
    return render(request, 'accounts/auth.html', context)

def mypage(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)    
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request,'更新完了しました')
    return render(request, 'accounts/mypage.html')


