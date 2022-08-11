from django import forms
from . import models
from django.contrib.auth import get_user_model


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        # fields = '__all__'
        exclude = ('user',)

class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Review
        # fields = '__all__'
        exclude = ('user','ticket')

class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


User = get_user_model()

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']

class UnFollowUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['followers']
