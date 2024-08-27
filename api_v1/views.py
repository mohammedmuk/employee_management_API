from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from . import serializers
from . import models


class EmployeeView(ModelViewSet):
    queryset  = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializerGetData
    renderer_classes = [JSONRenderer]


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.EmployeeSerializerGetData
        return serializers.EmployeeSerializer


class DepartmentView(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    renderer_classes = [JSONRenderer]


class PositionView(ModelViewSet):
    queryset = models.Position.objects.all()
    serializer_class = serializers.PositionSerializer
    renderer_classes = [JSONRenderer]


class ReviewView(ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializerGetData
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        user_id = self.kwargs.get('id')
        return self.queryset.filter(employee__id=user_id)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.ReviewSerializerGetData
        return serializers.ReviewSerializer