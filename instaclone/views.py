# display dependencies 
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponseRedirect
# token dependencies 
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import login
# decorators 
from django.contrib.auth.decorators import login_required
# Create your views here.



def signup(request):
    """ registration for the user """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Isntaclone Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/reg_form.html', {'form': form})

def account_activation_sent(request):
    """ view function to redirect user to the user registration complete page """
    current_user = request.user
    if current_user.is_authenticated():
        return HttpResponseRedirect('/')
    return render(request, 'registration/account_activation_complete.html')

def activate(request, uidb64, token):
    """ funtction to authenticate user activation from the email """
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
        return render(request, 'registration/account_activation_invalid.html')
      
@login_required
def home(request):
    """ displays the landing page """
    return render(request,'all_templates/landing.html')

@login_required
def explore(request):
    """ displays the landing page """
    return render(request,'all_templates/explore.html')

@login_required
def favourites(request):
    """ displays the landing page """
    return render(request,'all_templates/favourites.html')

@login_required
def profile(request):
    """ displays the landing page """
    return render(request,'all_templates/profile.html')




