# display dependencies 
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponseRedirect
# token dependencies 
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm,ImageForm
from .tokens import account_activation_token
from .models import User_prof, Comments, Image
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
    current_user = request.user
    all_images = Image.objects.all()
    # return_list = []
    # for image in all_images:
    #     return_list.append((image, image.image_likes.filter(profile_owner=request.user)))

    return render(request,'all_templates/landing.html',{'images':all_images})

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
    #searching for users inpu
    return render(request,'all_templates/profile.html')

@login_required
def post(request):
    current_user = request.user
    print(current_user)
    prof = User_prof.objects.get(user = current_user)
    print(prof)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.prof = prof
            post.save()
        return redirect(home)
    else:
        form = ImageForm()

    return render(request, 'all_templates/post.html', {"form": form})

@login_required
def profile(request):
    """ rendering images by profile owner """
    current_user = request.user
    prof_details = User_prof.objects.filter(username = current_user.id).all()
    user_images  = Image.objects.filter(username = current_user).all()

    return render(request, 'all_templates/profile.html', {'prof_data': prof_details,'user_images':user_images})

@login_required
def explore(request):
    """ rendering discover images """
    discover_images = Image.objects.filter(category = 'public').all()
    return render(request, 'all_templates/explore.html',{'discover_images':discover_images})

@login_required
def search(request,name):
    """ rendering search images """
    if 'name' in request.Get and request.Get['name']:
        search_term = request.GET.get("name")
        try:
            images = Image.object.filter(image_name = search_term).all()
            return render(request, "all_templates/search.html",{'images':images})
        except:
            message ='Image for search term not found'
            return render(request,"all_templates/search.html",{'message':message})

    else: 
        message = 'please enter a search term '
        return render(request,"all_templates/search.html",{'message': message})