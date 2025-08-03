from .views import ConfirmOrderAPIView,OrderCalculationAPIView,OrderList,CountryListAPIView,CountryListAPIView,DistrictListAPIView,UpazilaListAPIView
from django.urls import path,include

urlpatterns =[

    path('buy_now/<int:id>/',ConfirmOrderAPIView.as_view(),name = 'buy_now'),
    path('calculate/<int:id>/',OrderCalculationAPIView.as_view(),name = 'calculate'),
    path('orderlist/',OrderList.as_view(),name = 'orderlist'),
    path('countries/', CountryListAPIView.as_view()),
    path('countries/<int:country_id>/districts/', DistrictListAPIView.as_view()),
    path('districts/<int:district_id>/upazilas/', UpazilaListAPIView.as_view()),
]