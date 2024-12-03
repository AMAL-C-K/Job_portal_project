from django.urls import path
from . import views




urlpatterns = [
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('profile', views.profile, name='profile'),
    path('update/<int:profile_id>', views.update_profile, name='update'),
    path('delete/<int:profile_id>', views.delete_profile, name='delete'),
    
]