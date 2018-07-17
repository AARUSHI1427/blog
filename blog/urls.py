from django.contrib import admin
from django.urls import path
from blog import views
app_name="blog"

urlpatterns=[
    path('',views.post_list,name='list'),
    path('create/',views.post_create),
    path('<int:id>/',views.post_detail,name='detail'),
    path('<int:id>/edit/',views.post_update,name='update'),
    path('<int:id>/delete/',views.post_delete,name='delete'),

]
