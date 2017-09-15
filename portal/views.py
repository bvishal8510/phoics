"""
This is a doc string
"""
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from phoics.settings import EMAIL_HOST_USER
from .forms import SignUpPage
from .forms import forget_password
from .tokens import account_activation_token

def front_page(request):
    return render(request,'portal/front_page.html')

@login_required
def home(request):
    """
    doc string inside a function
    :param request:
    :return: render
    """
    return render(request, 'portal/home.html')

def signup(request):

    if request.method == 'POST':
        form = SignUpPage(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your phoics Account'
            message = render_to_string('portal/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            from_mail=EMAIL_HOST_USER
            to_mail=[user.email]
            send_mail(subject, message,from_mail,to_mail,fail_silently=False)
            return redirect('account_activation_sent')
    else:
        form = SignUpPage()
    return render(request, 'portal/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'portal/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'portal/account_activation_invalid.html')
    if user.is_active is False:
        pass


# def forget_pass(request):
#     if request.method == 'POST':
#         form_forget = forget_password(request.POST)
#         if form_forget.is_valid():
#             fuser = form_forget.save(commit=False)
#
#
#             current_site = get_current_site(request)
#             subject = 'checking for password reset'
#             message = render_to_string('portal/account_activation_email.html', {
#                 'user': fuser,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(fuser.pk)),
#                 'token': account_activation_token.make_token(fuser),
#             })
#             from_mail = EMAIL_HOST_USER
#             to_mail = [fuser.your_email]
#             send_mail(subject, message, from_mail, to_mail, fail_silently=False)
#             return redirect('account_activation_sent')
#
#
#     else:
#         form_forget = forget_password()
#     return render(request, 'portal/forget_page.html')
#



