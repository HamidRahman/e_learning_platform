from rest_framework import generics
from rest_framework import viewsets
from courses.api.serializers import SubjectSerializer, CourseSerializer
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from courses.api.pagination import StandardPagination
from courses.models import Subject, Course

# class SubjectListView(generics.ListAPIView):
#     queryset = Subject.objects.annotate(
#         total_courses=Count('courses')
#     )
#     serializer_class = SubjectSerializer
#     pagination_class = StandardPagination
    
# class SubjectDetailView(generics.RetrieveAPIView):
#     queryset = Subject.objects.annotate(
#         total_courses=Count('courses')
#     )
#     serializer_class = SubjectSerializer
    
class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.annotate(
        total_courses=Count('courses')
    )
    serializer_class = SubjectSerializer
    pagination_class = StandardPagination

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer
    pagination_class = StandardPagination
    @action(
        detail=True,
        methods=['post'],
        authentication_classes=[SessionAuthentication],
        permission_classes=[IsAuthenticated]
    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled':True})
    
# class CourseEnrollView(APIView):
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         course.students.add(request.user)
#         return Response({'enrolled':True})