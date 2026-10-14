
from django.urls import path

from fitwise_app.views import RegisterView,GetMeView,FoodLogListCreateView,FoodLogRetrieveUpdateDeleteView,FoodLogSummaryView,DietPlanView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # route for register view
    path("register/",RegisterView.as_view()),

    # route for getme view
    path("me/",GetMeView.as_view()),

    # route for foodlog list,create view
    path("foodlog/",FoodLogListCreateView.as_view()),

    # route for foodlog retrieve,update,delete view
    path("foodlog/<int:pk>/",FoodLogRetrieveUpdateDeleteView.as_view()),

    # route for token authentication
    path("token/",ObtainAuthToken.as_view()),

    # route for summary view
    path("foodlog/summary/",FoodLogSummaryView.as_view()),

    # route for dietplan view
    path("foodlog/diet/",DietPlanView.as_view()),
]