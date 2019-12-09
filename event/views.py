from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *



class EventList(ListView):
    model = Event
    template_name = 'event/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class EventDetail(DetailView):
    model = Event
    template_name = 'event/event_detail.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def filter_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    filtered_event = Event.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'event/category.html', {

        'category': category,
        'filtered_event': filtered_event,
        'categories': categories
    })


def filter_by_tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    filtered_event = Event.objects.filter(tags=tag)
    categories = Category.objects.all()
    return render(request, 'event/tag.html', {

        'tag': tag,
        'filtered_event': filtered_event,
        'categories': categories
    })

def filter_by_date(request):

    date = request.GET.get('calendar')
    filtered_event = Event.objects.filter(date=date)
    categories = Category.objects.all()
    return render(request, 'event/date.html', {
        'date': date,
        'filtered_event': filtered_event,
        'categories': categories
    })
