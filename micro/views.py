from django.shortcuts import render,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from .forms import Login_Form, Add_User_Form, Change_Password_Form, UserFilter_Form, Add_Video_Form
from .models import Zuke_User, User_Filters, Videos, Zuke_Subscribed, Issue
from django.db import IntegrityError
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import send_mail


def home(request):
    obj = Videos.objects.all()
    paginator = Paginator(obj, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'home2.html', {'contacts':contacts})

def add_user(request):
    form = Add_User_Form()
    if request.method == "POST":
        form = Add_User_Form(request.POST or None)
        if form.is_valid(): 
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            sex = form.cleaned_data['sex']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                o = Zuke_User.objects.create(name=name,dob=dob,sex=sex,phone=phone,email=email,password=password)
                z = Zuke_Subscribed(user_id=o)
                z.save()
                print(z)
                msg = "User Register successfully"
            except IntegrityError:
                msg = "User already exist in database"
                return render(request, 'register.html', {'form':form, 'msg':msg})
        return render(request, 'register.html', {'form':form, 'msg':msg})
    return render(request, 'register.html', {'form':form})

class User_Auth(TemplateView):
    template_name = 'home.html'
    
    def post(self, request):
        if 'userid' not in request.session:
            form = Login_Form(request.POST or None)
            if form.is_valid():
                email = form.cleaned_data["email"]
                password = form.cleaned_data["password"]
                data = [email, password]
                try:
                    email1 = Zuke_User.objects.values_list(
                        "email", flat=True).get(email=email)
                except ObjectDoesNotExist:
                    msg = "Invalid email or password"
                    return render(request, self.template_name, {'form':form, 'msg':msg})
                try:
                    password1 = Zuke_User.objects.values_list("password", flat=True).get(
                        password=password)
                except ObjectDoesNotExist:
                    msg = "Invalid email or password"
                    return render(request, self.template_name, {'form':form, 'msg':msg})

                user = [email1, password1]
                if data == user:
                    did = Zuke_User.objects.get(email=email)
                    request.session["name"] = did.name
                    request.session["email"] = did.email
                    request.session["userid"] = did.user_id
                    return HttpResponseRedirect('/userpage/')

            return render(request, self.template_name, {"form": form})
        else:
            return HttpResponseRedirect('/userpage/')
            
    def get(self, request):
        if 'userid' in request.session:
            return HttpResponseRedirect('/userpage/')
        else:
            form = Login_Form()
            return render(request, self.template_name, {"form": form})

def userpage(request):
    xid = request.session["userid"] 
    p = Zuke_Subscribed.objects.values_list('video_title', flat=True).filter(user_id=xid)
    obs = Videos.objects.filter(video_id__in=p).reverse()
    paginator = Paginator(obs, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    if request.method=="POST":
        uid = request.session['userid']
        video = request.POST.get('video')
        s = Videos.objects.get(video_id=video)
        x = Zuke_Subscribed.objects.get(user_id=uid)
        x.video_title.remove(s)
        x.save()
        sus = "UnSubscribed!"
        return render(request, "user.html", {'contacts':contacts, 'sus':sus})
    return render(request, "user.html", {'contacts':contacts})

def userpage_love(request):
    xid = request.session["userid"] 
    p = Zuke_Subscribed.objects.values_list('video_title', flat=True).filter(user_id=xid)
    obs = Videos.objects.filter(Q(video_id__in=p)).filter(genere='love')
    paginator = Paginator(obs, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    gen = "Love Genere"
    if request.method=="POST":
        uid = request.session['userid']
        video = request.POST.get('video')
        s = Videos.objects.get(video_id=video)
        x = Zuke_Subscribed.objects.get(user_id=uid)
        x.video_title.remove(s)
        x.save()
        sus = "UnSubscribed!"
        return render(request, "user.html", {'contacts':contacts, 'sus':sus})
    return render(request, "base.html", {'contacts':contacts, 'gen':gen})

def userpage_horror(request):
    xid = request.session["userid"] 
    p = Zuke_Subscribed.objects.values_list('video_title', flat=True).filter(user_id=xid)
    obs = Videos.objects.filter(Q(video_id__in=p)).filter(genere='horror')
    paginator = Paginator(obs, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    gen = "Horror Genere"
    if request.method=="POST":
        uid = request.session['userid']
        video = request.POST.get('video')
        s = Videos.objects.get(video_id=video)
        x = Zuke_Subscribed.objects.get(user_id=uid)
        x.video_title.remove(s)
        x.save()
        sus = "UnSubscribed!"
        return render(request, "user.html", {'contacts':contacts, 'sus':sus})
    return render(request, "base.html", {'contacts':contacts, 'gen':gen})

def userpage_comedy(request):
    xid = request.session["userid"] 
    p = Zuke_Subscribed.objects.values_list('video_title', flat=True).filter(user_id=xid)
    obs = Videos.objects.filter(Q(video_id__in=p)).filter(genere='comedy')
    paginator = Paginator(obs, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    gen = "Comedy Genere"
    if request.method=="POST":
        uid = request.session['userid']
        video = request.POST.get('video')
        s = Videos.objects.get(video_id=video)
        x = Zuke_Subscribed.objects.get(user_id=uid)
        x.video_title.remove(s)
        x.save()
        sus = "UnSubscribed!"
        return render(request, "user.html", {'contacts':contacts, 'sus':sus})
    return render(request, "base.html", {'contacts':contacts, 'gen':gen})

def userpage_action(request):
    xid = request.session["userid"] 
    p = Zuke_Subscribed.objects.values_list('video_title', flat=True).filter(user_id=xid)
    obs = Videos.objects.filter(Q(video_id__in=p)).filter(genere='action')
    paginator = Paginator(obs, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    gen = "Action Genere"
    if request.method=="POST":
        uid = request.session['userid']
        video = request.POST.get('video')
        s = Videos.objects.get(video_id=video)
        x = Zuke_Subscribed.objects.get(user_id=uid)
        x.video_title.remove(s)
        x.save()
        sus = "UnSubscribed!"
        return render(request, "user.html", {'contacts':contacts, 'sus':sus})
    return render(request, "base.html", {'contacts':contacts, 'gen':gen})

def userpage_music(request):
    xid = request.session["userid"] 
    p = Zuke_Subscribed.objects.values_list('video_title', flat=True).filter(user_id=xid)
    obs = Videos.objects.filter(Q(video_id__in=p)).filter(genere='music')
    paginator = Paginator(obs, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    gen = "Music Genere"
    if request.method=="POST":
        uid = request.session['userid']
        video = request.POST.get('video')
        s = Videos.objects.get(video_id=video)
        x = Zuke_Subscribed.objects.get(user_id=uid)
        x.video_title.remove(s)
        x.save()
        sus = "UnSubscribed!"
        return render(request, "user.html", {'contacts':contacts, 'sus':sus})
    return render(request, "base.html", {'contacts':contacts, 'gen':gen})

def userpage_filter(request):
    if 'userid' in request.session:
        form = UserFilter_Form()
        return render(request, 'user_filter.html',{'form':form})
    else:
        form = UserFilter_Form()
        if request.method == "GET":
            form = UserFilter_Form(request.GET or None)
            if form.is_valid():
                search = form.cleaned_data['search']
                qus0 = Videos.objects.filter(Q(genere__contains=search)|Q(contents__contains=search)|Q(vtype__contains=search)
                |Q(no_words__contains=search)|Q(description__contains=search))         
                msg = "No videos found"
                return render(request, 'filters.html',{'form':form,'qus0':qus0,'msg':msg})
        return render(request, 'filters.html',{'form':form})




def user_change_pwd(request):   
    form = Change_Password_Form()
    if request.method == "POST":
        form = Change_Password_Form(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            try:
                stv = Zuke_User.objects.get(email=email)
                print(email)
            except:
                msg = 'Invalid Email'
                return render(request, 'changepwd.html', {'form':form, 'msg':msg})
            pwd = stv.password
            if password == pwd:
                if email == stv.email:
                    stv.password = new_password
                    stv.save()
                    msg = 'Password Changed Successful'
                    return render(request, 'changepwd.html',{'form': form, 'msg':msg})

    return render(request, 'changepwd.html', {'form': form})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        issue = request.POST.get('issue')  
        Issue.objects.create(name=name,email=email,issue=issue)
        send_mail(
            'Greetings from MicroVideos',
            name + ' ' + '\nTHANK YOU FOR CONTACTING!\n We look further about issue\nThis is an automated email!',
            'microvideos@mvs.com',
            [email],
            fail_silently=False,
        )
        ms = "Issue has been submitted!"
        msg = "We will find out solution for problem as soon as possible"
        return render(request, 'contact.html', {'ms':ms,'msg':msg})
    return render(request, 'contact.html')

def filter_user(request):
    if 'userid' not in request.session:
        form = UserFilter_Form()
        if request.method == "GET":
            form = UserFilter_Form(request.GET or None)
            if form.is_valid():
                search = form.cleaned_data['search']
                qus0 = Videos.objects.filter(Q(genere__contains=search)|Q(contents__contains=search)|Q(vtype__contains=search)
                |Q(no_words__contains=search)|Q(description__contains=search))
                paginator = Paginator(qus0, 4)
                page = request.GET.get('page')
                contacts = paginator.get_page(page)         
                msg = "No videos found"
                return render(request, 'filters.html',{'form':form,'contacts':contacts,'msg':msg, 'search':search})
        return render(request, 'filters.html',{'form':form})
    else:
        form = UserFilter_Form()
        if request.method == "GET":
            form = UserFilter_Form(request.GET or None)
            if form.is_valid():
                uid = request.session['userid']
                search = form.cleaned_data['search']
                qus0 = Videos.objects.filter(Q(genere__contains=search)|Q(contents__contains=search)|Q(vtype__contains=search)
                |Q(no_words__contains=search)|Q(description__contains=search))
                paginator = Paginator(qus0, 4)
                page = request.GET.get('page')
                contacts = paginator.get_page(page) 
                msg = "No videos found"
                return render(request, 'user_filter.html',{'form':form,'contacts':contacts,'msg':msg, 'search':search})
        if request.method=="POST":
            uid = request.session['userid']
            video = request.POST.get('video')
            s = Videos.objects.get(video_id=video)
            x = Zuke_Subscribed.objects.get(user_id=uid)
            x.video_title.add(s)
            x.save()
            sus = "Subscribed!"
            return render(request, 'user_filter.html',{'sus':sus,'form':form})
        return render(request, 'user_filter.html',{'form':form})

def log_out(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    lg = "logged out"
    return HttpResponseRedirect("/", {'lg':lg})

def add_video(request):
    form = Add_Video_Form()
    if request.method == "POST":
        form = Add_Video_Form(request.POST,request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data['video_title']
            label = form.cleaned_data['label']
            vtype = form.cleaned_data['vtype']
            cont = form.cleaned_data['contents']
            gen = form.cleaned_data['genere']
            words = form.cleaned_data['no_words']
            sent = form.cleaned_data['no_sentences']
            desc = form.cleaned_data['description']
            video = form.cleaned_data['videos']
            x = Videos.objects.create(video_title=title, label=label, vtype=vtype,contents=cont,genere=gen,no_words =words,no_sentences=sent,description =desc,videos=video)
            msg = "Video Uploaded Successfully"
            return render(request, 'add_video.html', {'form':form, 'msg':msg}) 

    return render(request, 'add_video.html', {'form':form}) 
