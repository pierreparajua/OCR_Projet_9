
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain

from authentication.models import User
from website.models import Review, UserFollows
from website import forms, models



@login_required
def flux(request):
    reviews = models.Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    tickets = models.Ticket.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    for post in posts:
        if isinstance(post, Review):
            posts.remove(post.ticket)

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
    all_followed = models.UserFollows.objects.all()
    x = [followed.followed_user.username for followed in list(all_followed)]
    x.append(request.user)
    print(x)
    print(request.user)
    users = User.objects.exclude(username__in =x )
    print(users)








    followed_users = UserFollows.objects.filter(user_id=request.user)
    return render(request, 'website/follow_users.html', context={"followed_users": followed_users,
                                                                 "users": users})


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
