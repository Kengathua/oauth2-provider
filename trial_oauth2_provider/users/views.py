import json
from django.http import HttpResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from rest_framework import viewsets
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.models import AccessToken
from oauth2_provider.decorators import protected_resource

from trial_oauth2_provider.users import serializers
from trial_oauth2_provider.users.models import User


def sign_in(request):
	return render(request,'registration/login.html')


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			email = request.POST.get('email')
			password =request.POST.get('password')

			user = authenticate(request, username=email, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, f'Username OR password is incorrect {email, password, user}')

		context = {}
		return render(request, 'registration/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('/v1/users/sign-in/')

@login_required(login_url='/v1/users/sign-in/')
def home(request):
    # return HttpResponse('Successful will display registered apps here')
    return redirect('o/applications/')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

@protected_resource(scopes=['read'])
def profile(request):
    return HttpResponse(json.dumps({
        "guid": str(request.resource_owner.id),
        "email": request.resource_owner.email,
        "first_name": request.resource_owner.first_name,
        "last_name": request.resource_owner.last_name,
        "other_names": request.resource_owner.other_names,
        "phone_no": request.resource_owner.phone_no,
        "date_of_birth": str(request.resource_owner.date_of_birth),
        "date_joined": str(request.resource_owner.date_joined),
        "is_staff": request.resource_owner.is_staff,
        "is_admin": request.resource_owner.is_admin,
        "is_active": request.resource_owner.is_active,
    }), content_type="application/json")
