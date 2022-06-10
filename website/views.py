from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain

from authentication.models import User
from website.models import Review, UserFollows, Ticket
from website import forms


@login_required
def flux(request):
    users_followed = UserFollows.objects.filter(user_id=request.user)

    reviews = Review.objects.filter(user=request.user)
    reviews_from_followed = Review.objects.filter(user__in=[user_followed.followed_user for user_followed
                                                            in users_followed])
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    reviews_from_followed = reviews_from_followed.annotate(content_type=Value('REVIEW', CharField()))

    tickets = Ticket.objects.filter(user=request.user)
    tickets_from_followed = Ticket.objects.filter(user__in=[user_followed.followed_user for user_followed
                                                            in users_followed])
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    tickets_from_followed = tickets_from_followed.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(chain(reviews, reviews_from_followed, tickets, tickets_from_followed),
                   key=lambda post: post.time_created, reverse=True)

    tickets_already_answer = [review.ticket_id for review in reviews] + \
                             [review_from_followed.ticket_id for review_from_followed in reviews_from_followed]

    return render(request, 'website/flux.html', context={'posts': posts,
                                                         'tickets_already_answer': tickets_already_answer})


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
            review.ticket = Ticket.objects.last()
            review.save()
            return redirect('flux')
    context = {"review_form": review_form, "ticket_form": ticket_form}
    return render(request, 'website/create_review.html', context=context)


@login_required
def create_review_from_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)

    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = Ticket.objects.get(pk=ticket_id)
            review.save()
            return redirect('flux')
    return render(request, 'website/create_review_from_ticket.html', context={"ticket": ticket,
                                                                              "review_form": review_form})


@login_required
def display_posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(reviews, tickets),
                   key=lambda post: post.time_created, reverse=True)
    return render(request, 'website/posts.html', context={"posts": posts})


@login_required
def follow_users(request):
    users_follow_you = [user_follow.user.username for user_follow in
                        UserFollows.objects.filter(followed_user=request.user.id)]

    users_followed = UserFollows.objects.filter(user_id=request.user)
    users_to_exclude = [user_followed.followed_user.username for user_followed in users_followed]
    users_to_exclude.append(request.user.username)
    users_to_follow = User.objects.exclude(username__in=users_to_exclude)
    if request.method == "POST":
        print(request.POST["to_delete"])
        """
        to_follow = User.objects.get(pk=request.POST["to_follow"])
        if to_follow in users_to_follow:
            UserFollows(user=request.user, followed_user=to_follow).save()
        """

    return render(request, 'website/follow_users.html', context={"users_followed": users_followed,
                                                                 "users_to_follow": users_to_follow,
                                                                 "users_follow_you": users_follow_you})



