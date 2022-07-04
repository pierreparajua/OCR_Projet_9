from django import forms
from website import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mx-auto w-50 mb-3'})}



class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'body': forms.Textarea(attrs={'class': 'form-control mx-auto w-50 mb-3'})
        }


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = ['followed_user']


"""
class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fiels = ['headline']
"""
