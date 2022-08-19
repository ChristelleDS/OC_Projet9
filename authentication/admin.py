from django.contrib import admin
from authentication.models import User
from reviews.models import Ticket, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Review)
