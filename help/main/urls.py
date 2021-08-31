from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('courses', views.courses, name="courses"),
    path('courses/<str:slug>/', views.course, name="course"),
    path('business', views.business, name="business")
]