from django.urls import path
from . import views
urlpatterns = [
    path('departments', views.DepartmentView.as_view({'get' : 'list', 'post' : 'create'}), name="departments"),
    path('departments/<int:pk>', views.DepartmentView.as_view({'get' : 'retrieve', 'put' : 'update','delete' : 'destroy'}), name="department"),
    path('positions', views.PositionView.as_view({'get' : 'list', 'post' : 'create'}), name="positions"),
    path('positions/<int:pk>', views.PositionView.as_view({'get' : 'retrieve', 'put' : 'update', 'delete' : 'destroy'}), name="positions"),
    path('employees', views.EmployeeView.as_view({'get' : 'list', 'post' : 'create'}), name="employees"),
    path('employees/<int:pk>', views.EmployeeView.as_view({'get' : 'retrieve', 'put' : 'update', 'patch' : 'partial_update', 'delete' : 'destroy'}), name="employee"),
    path('employees/<int:id>/reviews', views.ReviewView.as_view({'get' : 'list', 'post' : 'create'}), name="reviews"),
    path('employees/<int:id>/reviews/<int:pk>', views.ReviewView.as_view({'get' : 'retrieve', 'put' : 'update', 'patch' : 'partial_update', 'delete' : 'destroy'}), name="review"),
]
