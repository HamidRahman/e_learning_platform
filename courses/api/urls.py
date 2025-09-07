from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'courses'

router = routers.DefaultRouter()
router.register('coureses', views.CourseViewSet)
router.register('subjects', views.SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('subjects/', views.SubjectListView.as_view(), name='subject_list'),
    # path('subjects/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    #path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll')
]