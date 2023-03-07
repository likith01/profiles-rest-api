from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views




router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name= 'hello-viewset')
#from video 45
router.register('profile', views.UserProfileViewSet)

#from video 59
router.register('feed', views.UserProfileFeedViewSet)




urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),#from video 55
    path('',include(router.urls))
]
