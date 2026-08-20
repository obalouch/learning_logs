from django.shortcuts import render , redirect
from .models import Topic , Entry
from .forms import TopicForm , EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request) :
    return render(request,'logs_app/index.html')

def mine(request) :
    return render(request,'logs_app/mine.html')
def check_topic_owner(owner , user) :
    if owner != user :
        raise Http404

@login_required
def topics(request) :
    #topic = Topic.objects.order_by('add_date')
    topic = Topic.objects.filter(owner=request.user).order_by('add_date')
    context = {'topics' : topic}
    return render(request,'logs_app/topics.html',context)
@login_required
def topic(request,topic_id) :
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic.owner , request.user) # line 12
    entries = topic.entry_set.order_by("-add_date")
    context = {'topics' : topic , 'entries' : entries}
    return render(request,'logs_app/topic.html',context)
@login_required
def newTopic(request) :
    if request.method != 'POST' :
        form = TopicForm()
    else :
        form = TopicForm(data=request.POST)
        if form.is_valid() :
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('logs_app:topics')

    context = {'form' : form}
    return render(request,'logs_app/newTopic.html',context)
@login_required
def newEntry(request,topic_id) :
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic.owner , request.user)
    if request.method != 'POST' :
        form = EntryForm()
    else :
        form = EntryForm(data=request.POST)
        if form.is_valid() :
            new_entry = form.save(commit=False)
            new_entry.refrence = topic
            new_entry.save()
            return redirect('logs_app:topic',topic_id=topic_id)

    context = {'topic' : topic , 'form' : form}
    return render(request,'logs_app/newEntry.html',context)
@login_required
def editentry(request,entry_id) :
    entry = Entry.objects.get(id=entry_id)
    topic = entry.refrence
    check_topic_owner(topic.owner , request.user)
        
    if request.method != 'POST' :
        form = EntryForm(instance=entry)
    else :
        form = EntryForm(instance=entry , data = request.POST)
        if form.is_valid() :
            form.save()
            return redirect('logs_app:topic',topic_id=topic.id)

    context = {'entry' : entry , 'topic' : topic , 'form' : form}
    return render(request , 'logs_app/editentry.html',context)