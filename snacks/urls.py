from django.urls import path, include
from .views import HomeView,AboutView # we imported this because we defined a class that we used here 'HomeView'

urlpatterns = [
    path('',HomeView.as_view(), name = 'home'),  # path('root we want',NameView.as_view(), name='VARIABLE ex:home we will use it later') ## NameView we make from this one a class inside views.py
    path('about/',AboutView.as_view(), name = 'about'),
    
]