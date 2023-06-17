from django.urls import path

from analyze_api import views



urlpatterns = [
    path('', views.SentimentAnalysisViewSet.as_view({
        'post': 'create',
    })),
]