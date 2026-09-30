from django.urls import path
from standards import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('families/', views.families_view, name='families'),
    path('examples/', views.examples_view, name='examples'),
    path('analyze/', views.analyze_view, name='analyze'),
    path('feedback/', views.feedback_view, name='feedback'),
]
