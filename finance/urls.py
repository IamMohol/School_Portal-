from django.urls import path
from . import apiviews

urlpatterns = [
    path('current/', apiviews.FinanceView.as_view(), name='finance'),
    path('history/', apiviews.FinanceHistoryView.as_view(), name='finance'),
]