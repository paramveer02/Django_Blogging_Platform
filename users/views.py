from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account created! Let's start blogging Herr {username}!!"
            )
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(
        request, "users/register.html", {"form": form, "title": "Registration"}
    )
