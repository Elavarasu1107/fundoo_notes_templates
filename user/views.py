from django.shortcuts import render, redirect
import logging
from .models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

logging.basicConfig(filename='jinja.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger()


class UserRegistration(View):

    def post(self, request):
        """
        This method add the user to the database
        """
        try:
            User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'),
                                     first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'),
                                     email=request.POST.get('email'), phone=request.POST.get('phone'),
                                     location=request.POST.get('location'))
            return redirect('login')
        except Exception as ex:
            logger.exception(ex)
            print(ex)
            return render(request, 'user/registration.html')

    def get(self, request):
        return render(request, 'user/registration.html')


class UserLogin(View):
    """
    This class check the user in the database
    """
    template_name = 'user/login.html'

    def post(self, request):
        """
        This method use to log in the user
        """
        try:
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('profile')
            return render(request, self.template_name)
        except Exception as ex:
            logger.exception(ex)
            return render(request, self.template_name)

    def get(self, request):
        return render(request, self.template_name)


class UserProfile(View):
    """
    This class get data of the user
    """
    def get(self, request):
        context = {'heading': "Welcome to Fundoo Notes", 'user': request.user}
        return render(request, 'user/profile.html', context=context)


class UserLogout(View):
    """
    This class logout the user from profile page
    """
    def get(self, request):
        logout(request)
        return redirect('login')
