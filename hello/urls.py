from django.urls import path
from .views import IndexView
from hello.views import NameListView, NameDetailView

app_name = 'hello'

urlpatterns = [
    path('', IndexView.as_view()),
    path('list/', NameListView.as_view(), name = 'namelist'),
    path('detail/<int:pk>/', NameDetailView.as_view(), name = 'namedetail'),
]

