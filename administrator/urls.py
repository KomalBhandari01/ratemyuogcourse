from django.urls import path
from administrator import views


app_name = 'administrator'

urlpatterns = [
    path ('', views.mainPage, name='mainPage'),
    path('base/', views.base, name='base'),
    path ('report_review_management/', views.report_review_management, name='report_review_management'),
    path ('report_review_detail/', views.reported_review_detail, name='report_review_detail'),
    path ('report_review_delete/', views.reported_review_delete, name='report_review_delete'),
    path ('website_feedback_management/', views.website_feedback_management, name='website_feedback_management'),
    path ('website_feedback_detail/', views.website_feedback_detail, name='website_feedback_detail'),
    path ('website_feedback_delete/', views.website_feedback_delete, name='website_feedback_delete'),
    path('course_management/', views.course_management, name='course_management'),
    path ('course_detail/', views.course_detail, name='course_detail'),
    path ('course_edit_post/', views.course_edit_post, name='course_edit_post'),
    path ('course_delete/', views.course_delete, name='course_delete'),
    path('lecturer_management/', views.lecturer_management, name='lecturer_management'),
]
