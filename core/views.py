from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .utils import get_ai_response

def dietitian_bot(request):
    response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        prompt = f"As a dietitian, provide advice based on: {user_input}"
        response = get_ai_response(prompt)
    return render(request, 'dietitian_bot.html', {'response': response})

def trainer_bot(request):
    response = None
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        prompt = f"As a personal trainer, provide a workout plan for: {user_input}"
        response = get_ai_response(prompt)
    return render(request, 'trainer_bot.html', {'response': response})



def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm()
    return render(request, 'user_profile.html', {'form': form})
