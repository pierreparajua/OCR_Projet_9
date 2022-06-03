from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain

from authentication.models import User
from website.models import Review, UserFollows
from website import forms, models


@login_required
def flux(request):
    users_followed = UserFollows.objects.filter(user_id=request.user)

    reviews = models.Review.objects.filter(user=request.user)
    review_from_followed = models.Review.objects.filter(user__in=[user_followed.followed_user for user_followed
                                                                  in users_followed])
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    review_from_followed = review_from_followed.annotate(content_type=Value('REVIEW', CharField()))

    tickets = models.Ticket.objects.filter(user=request.user)
    tickets_from_followed = models.Ticket.objects.filter(user__in=[user_followed.followed_user for user_followed
                                                                   in users_followed])
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    tickets_from_followed = tickets_from_followed.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(chain(reviews, review_from_followed, tickets, tickets_from_followed),
                   key=lambda post: post.time_created, reverse=True)

    return render(request, 'website/flux.html', context={'posts': posts})


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    context = {"ticket_form": ticket_form}
    return render(request, 'website/create_ticket.html', context=context)


@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = models.Ticket.objects.last()
            review.save()
            return redirect('flux')
    context = {"review_form": review_form, "ticket_form": ticket_form}
    return render(request, 'website/create_review.html', context=context)


@login_required
def display_posts(request):
    posts = models.Ticket.objects.filter(user=request.user)
    return render(request, 'website/posts.html', context={"posts": posts})


@login_required
def follow_users(request):
    users_followed = UserFollows.objects.filter(user_id=request.user)
    users_to_exclude = [user_followed.followed_user.username for user_followed in users_followed]
    users_to_exclude.append(request.user.username)
    users_to_follow = User.objects.exclude(username__in=users_to_exclude)
    print(users_to_follow)

    if request.method == "POST":
        print(request.POST)
    return render(request, 'website/follow_users.html', context={"users_followed": users_followed,
                                                                 "users_to_follow": users_to_follow})


"""
@login_required
def create_review(request):
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('flux')
    context = {"ticket_form": review_form}
    return render(request, 'website/create_review.html', context=context)
"""
