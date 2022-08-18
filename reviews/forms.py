from django import forms
from django.core.exceptions import ValidationError
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


class FollowForm(forms.Form):
    user_input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'utilisateur'}),
                                 label="S'abonner à un utilisateur")

    def clean_userinput(self):
        input = self.cleaned_data['user_input']
        if input not in users:
            raise ValidationError("Erreur, l'utilisateur saisi n'existe pas.", code='user_unknown')
        return input


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']


class UnFollowUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['followers']

