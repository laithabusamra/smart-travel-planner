from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('NewTrips/', views.add_trip, name='add_trip'),
    path('public-trips/', views.public_trips, name='public_trips'),
    path('my-trips/', views.mytrips_view, name='my_trips'),
    path('trip/<int:pk>/update/', views.TripUdateView.as_view(), name='trip_update'),
    path('trip/<int:pk>/delete/', views.TripDeleteView.as_view(),name='trip_delete'),
    path('review/<int:review_id>/update/', views.update_review, name='update_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
