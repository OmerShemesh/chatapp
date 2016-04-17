from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from itertools import chain
from .forms import MessageForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Message

@login_required
def index(request):
    loggedUser = request.user.username
    users_list = User.objects.filter().exclude(id = request.user.id)
    template = loader.get_template('watsapp/index.html')
    context = RequestContext(request, {
        'users_list':users_list,
        'loggedUser':loggedUser,
    })
    return HttpResponse(template.render(context))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return HttpResponseRedirect('/watsapp')
    else:
        form = UserCreationForm()

    template = loader.get_template('watsapp/register.html')
    context = RequestContext(request,{
                 'form':form,
              })
    return HttpResponse(template.render(context))

def message(request,user_id):
    sender_messages_list = Message.objects.filter(receiver_id = user_id,sender_id=request.user.id)
    receiver_messages_list = Message.objects.filter(sender_id = user_id , receiver_id=request.user.id)
    messages_list = sorted(chain(sender_messages_list,receiver_messages_list),key=lambda x:x.pub_date)
    receiver = User.objects.get(id=user_id).username
    if(request.method == 'POST'):
        form = MessageForm(request.POST)
        if form.is_valid():
            sentMessage = form.save(commit=False)
            sentMessage.pub_date = timezone.now()
            sentMessage.sender = request.user
            sentMessage.receiver = User.objects.get(id=user_id)
            sentMessage.save()
            return HttpResponseRedirect('/watsapp/%s'%user_id)
    else:
         form = MessageForm()

    template = loader.get_template('watsapp/message.html')

    context = RequestContext(request,{
                 'messages_list':messages_list,
                 'form':form,
                 'receiver':receiver,
              })
    return HttpResponse(template.render(context))
