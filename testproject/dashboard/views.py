from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from testapp.models import CustomUser, CustomUserManager

# new imports
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from testapp.tokens import account_activation_token
from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):

    return render(request, 'dashboard/auth/signin.html', {})


@login_required
def dash(request):
    return render(request, 'dashboard/dashboard/courses.html')

def create_user(request):
    
    if request.method == "POST":
        user = User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your account.'
        message = render_to_string('bbvoy/emails/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token':account_activation_token.make_token(user),
        })
        to_email = request.POST['email']
        email = EmailMessage(
                    mail_subject, message,  from_email='bbvoytest@gmail.com', to=[to_email]
        )
        email.send()

        return HttpResponse("pleas echeck your email to activate account")
    else:
        return render(request, 'dashboard/auth/signup.html', {})
    
    return HttpResponse()

def sign_in(request):

    if request.method == "POST":

        user = authenticate(request, username=request.POST['email'], passsword=request.POST['password'])
        if user is not None:
            login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/dashboard')
            
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('email or password information invalid')
    else:
        pass

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        # return redirect('home')
        return redirect('/dashboard')
    else:
        return HttpResponse('Activation link is invalid!')