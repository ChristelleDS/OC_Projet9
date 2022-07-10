from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from . import models, forms
from itertools import chain
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import Ticket



@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(request, 'reviews/home.html', context={'tickets': tickets, 'reviews': reviews})


@login_required
def createTicket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
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
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
    return render(request, 'reviews/edit_ticket.html', {'edit_form':edit_form})

class delete_Ticket(DeleteView):
    model = Ticket
    success_url = reverse_lazy("home")

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
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')
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
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
               }
    return render(request, 'reviews/createReview.html', context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'reviews/view_review.html', {'review': review})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
            if 'delete_review' in request.POST:
                delete_form = forms.DeleteReviewForm(request.POST)
                if delete_form.is_valid():
                    review.delete()
                    return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'reviews/edit_review.html', context=context)



@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'reviews/follow_users_form.html', context={'form': form})


@login_required
def feed(request):
    reviews = models.Review.objects.filter(
        Q(user__in=request.user.follows))
    tickets = models.Ticket.objects.filter(
        user__in=request.user.follows).exclude(
            reviews__in=reviews
    )
    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets),
        key=lambda reviews: reviews.time_created,
        reverse=True
    )
    return render(request, 'feed.html', context={'posts': posts})


