from django.urls import path

from charities.views import CreateCharityView

urlpatterns = [
    path('create/', CreateCharityView.as_view())
]
