from rest_framework.serializers import ModelSerializer, UniqueTogetherValidator
from . import models


class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = models.Department
        fields = '__all__'


class PositionSerializer(ModelSerializer):

    class Meta:
        model = models.Position
        fields = '__all__'


class EmployeeSerializerGetData(ModelSerializer):
    department = DepartmentSerializer()
    position = PositionSerializer()
    class Meta:
        model = models.Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'department', 'position', 'status']


class EmployeeSerializer(ModelSerializer):
    department = DepartmentSerializer
    position = PositionSerializer
    class Meta:
        model = models.Employee
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Employee.objects.all(),
                fields = ['first_name', 'last_name'],
                message = "employee with this name already exists."
            )
        ]



class EmployeeName(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ['id', 'first_name', 'last_name']


class ReviewSerializerGetData(ModelSerializer):
    employee = EmployeeName()
    class Meta:
        model = models.Review
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    employee = EmployeeName
    class Meta:
        model = models.Review
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Review.objects.all(),
                fields = ['reviewer_name', 'employee'],
                message = "A reviewer cannot make more than one review for the same employee."
            )
        ]