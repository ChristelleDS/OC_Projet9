from django import forms
from . import models
from django.contrib.auth import get_user_model

User = get_user_model()
users = User.objects.all()


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        # fields = '__all__'
        exclude = ('user', 'time_created', 'last_edited', )


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        # fields = '__all__'
        exclude = ('user', 'ticket')


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']


class UnFollowUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['followers']


def check_userinput(user_input):
    if user_input not in users:
        raise forms.ValidationError("Erreur, l'utilisateur saisi n'existe pas.", code='user_unknown')
    else:
        return user_input


class FollowForm(forms.Form):
    user_input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'utilisateur'}),
                                 label="S'abonner à un utilisateur ")
