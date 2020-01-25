from django.urls import path

from . import views

app_name = 'schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('setting-schedule/', views.add, name="schedule_setting"),
    path('private-schedule/', views.ScheduleView.as_view(), name="schedule_index"),
]
