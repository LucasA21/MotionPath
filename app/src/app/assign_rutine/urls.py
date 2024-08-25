from django.urls import path

import app.assign_rutine.views as view

urlpatterns = [
    path('', view.AssignRutineListView.as_view(), name='assign_rutine_list'),
    path('<int:pk>/', view.AssignRutineDetailView.as_view(), name='assign_rutine_detail'),
    path('create/', view.AssignRutineCreateView.as_view(), name='assign_rutine_create'),
    path('update/<int:pk>', view.AssignRutineUpdateView.as_view(), name='assign_rutine_update'),
    path('delete/<int:pk>', view.AssignRutineDeleteView.as_view(), name='assign_rutine_delete'),
]
