from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils import timezone
from . import models, forms
from itertools import chain
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Ticket, Review
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def createTicket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.time_created = timezone.now()
            ticket.save()
            return redirect('posts')
    context = {'ticket_form': ticket_form}
    return render(request, 'reviews/createTicket.html', context=context)


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    reviews = models.Review.objects.filter(Q(ticket=ticket))
    return render(request, 'reviews/view_ticket.html', {'ticket': ticket, 'reviews': reviews})


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        edit_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_form.is_valid():
            ticket = edit_form.save(commit=False)
            ticket.last_edited = timezone.now()
            ticket.save()
            return redirect('view_ticket', ticket_id)
    return render(request, 'reviews/edit_ticket.html', {'edit_form': edit_form, 'ticket': ticket})


@login_required
def deleteTicket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')
    return render(request,
                  'reviews/ticket_delete.html',
                  {'ticket': ticket})


@login_required
def createReview_Ticket(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.time_created = timezone.now()
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.time_created = timezone.now()
            review.save()
            return redirect('feed')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'reviews/createTicketwithReview.html', context=context)


@login_required
def createReview(request, ticket_id):
    review_form = forms.ReviewForm()
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.time_created = timezone.now()
            review.save()
            return redirect('feed')
    context = {
        'review_form': review_form,
        'ticket': ticket,
    }
    return render(request, 'reviews/createReview.html', context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket = get_object_or_404(models.Ticket, id=review.ticket.id)
    return render(request, 'reviews/view_review.html', {'review': review, 'ticket': ticket})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket = get_object_or_404(models.Ticket, id=review.ticket.id)
    edit_form = forms.ReviewForm(instance=review)
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                form = edit_form.save(commit=False)
                form.last_edited = timezone.now()
                form.save()
                return redirect('feed')
    context = {
        'edit_form': edit_form,
        'ticket': ticket,
        'review': review
    }
    return render(request, 'reviews/edit_review.html', context=context)


@login_required
def deleteReview(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('feed')
    return render(request,
                  'reviews/review_delete.html',
                  {'review': review})


@login_required
def follow_users(request):
    followform = forms.FollowForm()
    if request.method == 'POST':
        followform = forms.FollowForm(request.POST)
        if followform.is_valid():
            user_input = followform.cleaned_data['user_input']
            return redirect('follow', user_input)
        return redirect('follow_users')
    context = {
               'followform': followform, }
    return render(request, 'reviews/follow_users_form.html', context=context)


@login_required
def follow(request, user_input):
    current_user = request.user
    follows = current_user.follows.all()
    u_input = User.objects.get(username=user_input)
    if u_input.id not in follows:
        current_user.follows.add(u_input.id)
        current_user.save()
    return redirect('follow_users')


@login_required
def unfollow(request, user_unfollow):
    current_user = request.user
    follows = current_user.follows.all()
    u_input = User.objects.get(username=user_unfollow)
    if u_input in follows:
        current_user.follows.remove(u_input)
        current_user.save()
    return redirect('follow_users')


@login_required
def feed(request):
    tickets = Ticket.objects.filter(
        user__in=request.user.follows.all())
    reviews = Review.objects.filter(
        user__in=request.user.follows.all())
    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    return render(request, 'reviews/feed.html', context=context)


@login_required
def posts(request):
    tickets = Ticket.objects.filter(Q(user=request.user))
    reviews = Review.objects.filter(Q(user=request.user))
    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    return render(request, 'reviews/posts.html', context=context)
