from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_feedbacks, name='main'),
    path('feedback/<str:id>/', views.feedback_by_id, name='feedback_by_id'),
    path('create/feedback', views.create_feedback, name='create_feedback'),
    path('delete/feedback/<str:id>', views.delete_feedback, name='delete_feedback'),
    path('update/feedback/<str:id>', views.update_feedback, name="update_feedback"),
    path('feedback/<uuid:feedback_id>/comment/<uuid:comment_id>/delete/', views.delete_comment, name='delete_comment')
]
