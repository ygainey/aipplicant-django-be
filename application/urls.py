from django.urls import path
from .views import ApplicationListCreateView, ApplicationRetrieveUpdateDestroyView

urlpatterns = [
    path('', ApplicationListCreateView.as_view()),
    path('<int:id>/', ApplicationRetrieveUpdateDestroyView.as_view())
]