from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """The home page for the app."""
    return render(request, 'index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data, make blank form.
        form = TopicForm()
    else:
        # POST data available, processing.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for selected topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data, creating blank form.
        form = EntryForm()
    else:
        # POST data available, processing.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display blank/invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)


def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Initial request
        form = EntryForm(instance=entry)
    else:
        # POST data submitted, processing
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)