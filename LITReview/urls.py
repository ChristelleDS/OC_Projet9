"""critiques URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeView, PasswordChangeDoneView)
import authentication.views
import reviews.views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', authentication.views.login_page, name='login'),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
        name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('home/', reviews.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('ticket/create/', reviews.views.createTicket, name='ticket'),
    path('ticket/<int:ticket_id>', reviews.views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/edit', reviews.views.edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete', reviews.views.deleteTicket, name='delete_ticket'),
    path('ticket/review/create/', reviews.views.createReview_Ticket, name='review_ticket'),
    path('ticket/<int:ticket_id>/review/create/', reviews.views.createReview, name='review'),
    path('review/<int:review_id>', reviews.views.view_review, name='view_review'),
    path('review/<int:review_id>/edit', reviews.views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete', reviews.views.deleteReview, name='delete_review'),
    path('follow-users/', reviews.views.follow_users, name='follow_users'),
    path('follow-users/<str:user_input>/follow', reviews.views.follow, name='follow'),
    path('follow-users/<str:user_unfollow>/unfollow', reviews.views.unfollow, name='unfollow'),
    path('feed/', reviews.views.feed, name='feed'),
    path('posts/', reviews.views.posts, name='posts')
    ]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
