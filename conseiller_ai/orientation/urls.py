from django.urls import path
from .views import prompt, IndexView, BlogView, AboutView, VirtualAdvisorView, detect_intent

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Page principale
    path('blog/', BlogView.as_view(), name='blog'),  # Vue pour le blog
    path('about/', AboutView.as_view(), name='about'),  # Vue pour à propos
    path('virtual_advisor/', VirtualAdvisorView.as_view(), name='virtual_advisor'),  # Vue pour conseiller virtuel
    path('search/', prompt, name='prompt'),  # Vue pour les requêtes
]