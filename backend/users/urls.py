from django.urls import path

from .views import UserRegistration, UserActivity, UserSubscribe, UserUnSubscribe, GettingAllSubs

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('activity/', UserActivity.as_view(), name='activity'),
    path('subscribe/', UserSubscribe.as_view(), name='subscribe'),
    path('unsubscribe/', UserUnSubscribe.as_view(), name='unsubscribe'),
    path('all-subs/', GettingAllSubs.as_view(), name='all-subs')
]
