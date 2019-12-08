from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

# def event_list(request):
#     search_query = request.GET.get('search', '')
#     if search_query:
#         posts = Event.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
#     else:
#         posts = Event.objects.all()
#
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page', 1)
#     page = paginator.get_page(page_number)
#
#     is_paginated = page.has_other_pages()
#     if page.has_previous():
#         prev_url = f'?page={page.previous_page_number()}'
#     else:
#         prev_url = ''
#
#     if page.has_next():
#         next_url = f'?page={page.next_page_number()}'
#     else:
#         next_url = ''
#
#     context = {
#         'page_object': page,
#         'is_paginated': is_paginated,
#         'prev_url': prev_url,
#         'next_url': next_url
#     }
#     return render(request, 'event/index.html', context=context)


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
