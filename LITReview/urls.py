"""LITReview URL Configuration

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
import authentication.views
import website.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('flux/', website.views.flux, name='flux'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('create_ticket', website.views.create_ticket, name='create_ticket'),
    path('create_review', website.views.create_review, name='create_review'),
    path('create_review_from_ticket/<int:ticket_id>', website.views.create_review_from_ticket,
         name='create_review_from_ticket'),
    path('posts', website.views.display_posts, name='posts'),
    path('follow_users/>', website.views.follow_users, name='follow_users'),
    path('delete_user/<int:user_id>', website.views.delete_follow_user, name='delete_user'),
    path('delete_review/<int:review_id>', website.views.delete_review, name='delete_review'),
    path('update_review/<int:review_id>', website.views.update_review, name='update_review'),
    path('delete_ticket/<int:ticket_id>', website.views.delete_ticket, name='delete_ticket'),
    path('update_ticket/<int:ticket_id>', website.views.update_ticket, name='update_ticket')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
