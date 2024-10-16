from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_profile.controller.views import UserProfileView

router = DefaultRouter()
router.register(r'user_profile', UserProfileView, basename='user_profile')

urlpatterns = [
    path('', include(router.urls)),
    path('email-duplication-check',
         UserProfileView.as_view({'post': 'checkEmailDuplication'}),
         name='profile-email-duplication-check'),
    path('nickname-duplication-check',
         UserProfileView.as_view({'post': 'checkNicknameDuplication'}),
         name='profile-nickname-duplication-check'),
    path('register',
         UserProfileView.as_view({'post': 'registerProfile'}),
         name='register-profile'),
]