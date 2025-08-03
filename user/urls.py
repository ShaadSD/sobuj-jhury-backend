from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views





router = DefaultRouter()
router.register('list',views.UserListView,basename='list')
router.register('profile_list',views.UserProfileList,basename='profile_list')

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.UserRegistrationView.as_view(),name = 'register'),
    path('login/',views.UserLoginView.as_view(),name = 'login'),
    path('logout/',views.LogoutView.as_view(), name = 'logout'),
    path('pass_change/',views.PasswordChangeView.as_view(),name = 'pass_change'),
    path('profile_details/',views.UserProfileDetail.as_view(),name = 'profile_details')
]
