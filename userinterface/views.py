from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib import messages
from Accounts.models import profile,classroom,timetable,attendance,posts
from Accounts.forms import Classform,timetableform
from django.contrib.auth.decorators import login_required
from Accounts.decarators import is_class_member,is_class_admin
from Accounts.randgenrator import rand
from django.core.mail import send_mail
import datetime
# Create your views here.
week=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
@login_required
def createclass(request):
    if request.POST:
        form=Classform(request.POST)
        if (form.is_valid()):
            #form.save()
            
            classname=request.POST['class_name']
            class_sub=request.POST['class_subject']
            class_section=request.POST['class_sec']
            cid=rand(6)
            url='classroom/'+cid
            mail=request.user.email
            c=classroom(class_name=classname,class_sec=class_section,class_subject=class_sub,classid=cid,admin=request.user,c_url=url)
            c.save()
            send_mail('CLASS CODE','This is the class code for Verification:'+cid,'adhayayan.scl7maxo@gmail.com',[mail],fail_silently=False)
            return redirect('createclass/'+str(c.id))
    else:
        form=Classform(request.POST)
    return render(request,'home.html',{'form':form})

@login_required
def configure_class(request,cid):
    if request.POST:
        code=request.POST['vercode']
        c=classroom.objects.get(id=cid)
        if code==c.classid:
            url='/classroom/'+c.classid+'/admin'
            messages.success(request,'Classroom Created!!')
            c.members.add(request.user.profile)
            return redirect(url)
        else:
            messages.error(request,'Wrong Credentials! Classroom not Created!!')
    return render(request,'config.html')

@login_required
def joinclass(request):
    flag=0
    if request.POST:
        c_id=request.POST['classid']
        try:
            join_class=classroom.objects.get(classid=c_id)
        except classroom.DoesNotExist:
            messages.error(request,f'No Class Exists')
            return redirect('/classroom')
        user=profile.objects.get(user=request.user)
        if join_class.rem_members is not None:
            if request.user.username in join_class.rem_members.split(','):
                messages.error(request,f'You were Removed from the class!You cannot join Again')
                flag=1
        if flag==0:
            join_class.members.add(user)
        return redirect('classroom/'+c_id)


def home(request):
    form=Classform()
    #user=profile.objects.get(user=request.user)
    #user=profile.objects.all()
    #loc=TEMP
    return render(request,'home.html',{'tittle':'home','form':form})
    #return HttpResponse("<h1>HELLO WORLD</h1>")
def compiler(request,comp):
    return render(request,'compiler.html',{'compiler':comp})
def some(request,idk):
    try:
        a=profile.objects.get(user_id=idk)
    except profile.DoesNotExist:
        raise Http404('USER NOT FOUND')
    return render(request,'help.html',{'a':a})
    #return HttpResponse("<h1><a href="">hi</a></h1>")

def catalogue(request):
    form=Classform(request.POST)
    return render(request,'catalogue.html',{'form':form,'tittle':'catalogue'})

def help(request):
    form=Classform(request.POST)
    return render(request,'help.html',{'form':form,'tittle':'help'})

def about(request):
    form=Classform(request.POST)
    return render(request,'about.html',{'form':form,'tittle':'about'})

@login_required
def class_room(request):
    form=Classform(request.POST)
    userclass=classroom.objects.filter(members=request.user.profile)
    return render(request,'classroom_home.html',{'form':form,'user_classes':userclass})

@login_required
def attend_submit(request,c_id):
    if(request.POST):
        dot=datetime.datetime.now().replace(second=0,microsecond=0)
        dot_mins=dot.minute
        class_obj=classroom.objects.get(classid=c_id)
        user=profile.objects.get(user=request.user)
        for i in range(5):
            try:
                attend_table=attendance.objects.filter(att_class=class_obj).get(attendance_time=dot)
                attend_table.attendees.add(user)
                return redirect('/classroom/'+c_id)
            except attendance.DoesNotExist:
                pass
            dot_mins-=1
            if dot_mins<=0:
                dot_mins=0
            dot=datetime.datetime.now().replace(minute=dot_mins,second=0,microsecond=0)
        return redirect('/classroom/'+c_id)

@login_required
@is_class_member(allowed_class=[])
def CLASSROOM(request,c_id):
    #form=Classform(request.POST)
    attend=False
    dot=datetime.datetime.now().replace(second=0,microsecond=0)
    dot_mins=dot.minute
    class_obj=classroom.objects.get(classid=c_id)
    user=profile.objects.get(user=request.user)
    post=posts.objects.filter(p_class=class_obj).order_by('-upload_date')
    url='/classroom'
    for i in range(5):
         try:
             attend_table=attendance.objects.filter(att_class=class_obj).get(attendance_time=dot)
             if attend_table is not None:
                 attend=True
             if user in attend_table.attendees.all() or user == attend_table.attendees.all():
                 attend=False
             return render(request,'classroom.html',{'classID':c_id,'back':url,'attendance':attend,'now':dot,'attend':attend_table,'posts':post})
         except attendance.DoesNotExist:
             pass
         dot_mins-=1
         if dot_mins<=0:
             dot_mins=0
         dot=datetime.datetime.now().replace(minute=dot_mins,second=0,microsecond=0)
    timetables=timetable.objects.filter(clsobj=class_obj).order_by('class_time')
    message,flag=notify_me(timetables)
    content={'classID':c_id,'back':url,'attendance':attend,'timetables':timetables,'week':week,'posts':post,'notify':message,'classroom':class_obj,'class':flag}
    context=formtimetable(content)
    return render(request,'classroom.html',context)

@login_required
@is_class_member(allowed_class=[])
def people(request,c_id):
    url='/classroom/'+c_id
    class_members=classroom.objects.get(classid=c_id).members.all()
    userclass=classroom.objects.get(classid=c_id)
    if request.POST:
        rem_student=profile.objects.get(Uid=request.POST['rem_student'])
        student=rem_student.user.username
        rmembers=userclass.rem_members
        if rmembers is not None:
            removed_list=rmembers.split(',')
        else:
            removed_list=[]
        removed_list.append(student)
        rem_str=','.join(removed_list)
        userclass.rem_members=rem_str
        userclass.members.remove(rem_student)
        userclass.save()
    return render(request,'people.html',{'classID':c_id,'back':url,'members':class_members,'userclass':userclass})

def notify_me(timetables):
    today=datetime.datetime.today()
    weekday=today.strftime('%A')
    date=datetime.date.today()
    hrs,mins,secs=today.strftime("%H:%M:%S").split(':')
    hrs=int(hrs)
    mins=int(mins)
    secs=int(secs)
    flag=False
    time=datetime.time(hrs,mins,secs)
    time1=datetime.datetime.combine(date,time)
    for item in timetables:
        if item.class_day==weekday.upper():
            if datetime.datetime.combine(date,item.class_time)>time1:
                we=datetime.datetime.combine(date,item.class_time)-time1
                hours, remainder = divmod(we.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                if hours==1:
                    messag=f'YOU HAVE CLASS IN {hours} HOUR!!'
                elif hours<1:
                    messag=f'YOU HAVE CLASS TODAY IN {minutes} MINUTES!!'
                else:
                    messag='You have Class Today!!'
                flag=True
                break
    if not flag:
        messag='YOU DONT HAVE CLASS TODAY!!'
    return messag,flag

@is_class_admin
def classadmin(request,c_id):
    url='/classroom'
    class_obj=classroom.objects.get(classid=c_id)
    timetables=timetable.objects.filter(clsobj=class_obj).order_by('class_time')
    message,flag=notify_me(timetables)
    post=posts.objects.filter(p_class=class_obj).order_by('-upload_date')
    content={'classID':c_id,'back':url,'timetables':timetables,'week':week,'posts':post,'notify':message,'class':flag,'admin':True,'classroom':class_obj}
    context=formtimetable(content)
    return render(request,'classroom.html',context)
    
def formtimetable(contents):
    context=contents
    flag=0
    if context['timetables']:
        items={}
        list1=[]
        list2=[]
        for day in week:
            c=0
            for ct in contents['timetables']:
                if day==ct.class_day:
                    if(c==0):
                        list1.append(ct.class_time)
                        c+=1
                    elif(c==1):
                        list2.append(ct.class_time)
                        c+=1
            if(c==0):
                list1.append('None')
                list2.append('None')
            if(c==1):
                list2.append('None')
        context['timetables']=[list1,list2]
    else:
        context['timetables']=None
    return context
    

@is_class_admin
def classconfig(request,c_id):
    class_obj=classroom.objects.get(classid=c_id)
    cnt=0
    url='/classroom/'+c_id
    if request.POST:
        form=timetableform(request.POST)
        day=request.POST['class_day']
        time=request.POST['class_time']
        clink=request.POST['clink']
        if clink is not '':
            class_obj.c_link=clink
            class_obj.save()
        time_day=timetable.objects.filter(clsobj=class_obj)
        for classt in time_day:
            if day in classt.class_day:
                cnt+=1
        if(cnt==2):
            messages.error(request,f'You have already added maximum number of classes per Day')
            return redirect('/classroom/'+c_id+'/classconfig')
        else:
            time_table=timetable(clsobj=class_obj,class_day=day,class_time=time)
            time_table.save()
            messages.success(request,f'Class Updated')
            return redirect('/classroom/'+c_id+'/classconfig')
    else:
        timetables=timetable.objects.filter(clsobj=class_obj)
        form=timetableform()
        content={'classID':c_id,'form':form,'timetables':timetables,'week':week,'userclass':class_obj,'back':url}
        context=formtimetable(content)
    return render(request, 'classconfig.html',context)

def class_attend(request,c_id):
    class_obj=classroom.objects.get(classid=c_id)
    if request.POST:
        dat_time=request.POST['attendance_time']
        create_attendance=attendance(att_class=class_obj,attendance_time=dat_time)
        create_attendance.save()
        messages.success(request,'Attendance Added SuccessFully!')
        return redirect('/classroom/'+c_id+'/attendance')

    url='/classroom/'+c_id
    attend_table=attendance.objects.filter(att_class=class_obj).order_by('-attendance_time')
    return render(request,'attend.html',{'classID':c_id,'attendances':attend_table,'back':url,'userclass':class_obj})

def upload(request,c_id):
    class_obj=classroom.objects.get(classid=c_id)
    if request.method =="POST":
       announcement=request.POST['announce']
       desc=request.POST['desc']
       try:
            file_to=request.FILES['upfile']
            dat=datetime.datetime.now()
            f_upload=posts(posted_by=request.user,p_class=class_obj,notes=file_to,post=announcement,description=desc,upload_date=dat)
            f_upload.save()
       except :
            dat=datetime.datetime.now()
            f_upload=posts(posted_by=request.user,p_class=class_obj,post=announcement,description=desc,upload_date=dat)
            f_upload.save()
            messages.success(request,f'Posted Successfully!!')
       return redirect('/classroom/'+c_id+'/admin')
    else:
        return render(request,'upload.html')
        




