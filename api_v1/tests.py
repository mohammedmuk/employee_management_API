# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status


# class EmployeeSytemTest(APITestCase):
#     def test_departments(self):
#         departments_path = reverse('departments')
#         department = {"department_name" : "Management"}
#         response = self.client.post(departments_path, department, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
#         response2 = self.client.post( departments_path, department, format='json')
#         self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

#         response3 = self.client.get(departments_path)
#         self.assertEqual(response3.status_code, status.HTTP_200_OK)
    

#     def test_department(self):
#         departments_path = reverse('departments')
#         department = {"department_name" : "Management"}
#         response = self.client.post(departments_path, department, format='json')
#         id = response.json()['id']

#         department_path = reverse('departments')+f'/{id}'
#         response2 = self.client.get(department_path)
#         self.assertEqual(response2.status_code, status.HTTP_200_OK)

#         department2 = {"department_name" : "Sales"}
#         response3 = self.client.put(department_path, department2)
#         self.assertEqual(response3.status_code, status.HTTP_200_OK)

#         department3 = {"Department" : "IT"}
#         response4 = self.client.put(department_path, department3)
#         self.assertEqual(response4.status_code, status.HTTP_400_BAD_REQUEST)

#         response5 = self.client.delete(department_path)
#         self.assertEqual(response5.status_code, status.HTTP_204_NO_CONTENT)
