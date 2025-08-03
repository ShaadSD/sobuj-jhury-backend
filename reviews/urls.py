from django.urls import path,include

from .views import RevView






urlpatterns = [
   path('re-view/<int:id>/',RevView.as_view(),name = 're-view'),
]
