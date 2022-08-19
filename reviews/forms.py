from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
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
        exclude = ('user', 'ticket', 'time_created', 'last_edited',)


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


def clean_user_input(user_input):
    try:
        input = User.objects.get(username=user_input)
    except ObjectDoesNotExist:
        raise ValidationError("Erreur, l'utilisateur saisi n'existe pas.")


class FollowForm(forms.Form):
    user_input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'utilisateur'}),
                                 label="S'abonner à un utilisateur", validators=[clean_user_input])
