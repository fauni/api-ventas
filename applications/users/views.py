from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken


from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    CreateView,
    View
)

from django.views.generic.edit import (
    FormView
)

from .models import User
from .serializers import UserSerializer

from .forms import UserRegisterForm, LoginForm



from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import jwt


class Login(FormView):
    template_name = "users/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('producto_app:almacenes')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data = request.data, context={ 'request': request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if user is not None:
            token,_ = Token.objects.get_or_create(user = user)
            user_data = {
                'id': user.id,
                'username': user.username,
                'nombres': user.nombres,
                'apellidos': user.apellidos
            }
            return Response({
                'token': token.key,
                'user': user_data
            })
        else:
            return Response({'error': 'Credenciales Invalidas'}, status = status.HTTP_401_UNAUTHORIZED)



class Logout(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request, format = None):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            logout(request)
        return Response(status = status.HTTP_200_OK)


class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
        )
        #

        return super(UserRegisterView, self).form_valid(form)

class LoginUser(FormView):
    template_name = 'users/login2.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)

class LogoutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )