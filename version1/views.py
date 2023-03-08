from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm
from .forms import EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'version1/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    entries = Entry.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'version1/topics.html')

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'version1/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topics')

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'version1/new_entry.html', context)



