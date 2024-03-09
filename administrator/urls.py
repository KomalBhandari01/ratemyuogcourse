from django.urls import path
from administrator import views
from administrator.view import lecturer_view

app_name = 'administrator'

urlpatterns = [
    path ('', views.mainPage, name='mainPage'),
    path ('base/', views.base, name='base'),
    path ('report_review_management/', views.reported_reviews_management, name='report_review_management'),
    path ('report_review_detail/', views.reported_review_detail, name='report_review_detail'),
    path ('report_review_delete/', views.reported_review_delete, name='report_review_delete'),
    path ('website_feedback_management/', views.website_feedback_management, name='website_feedback_management'),
    path ('website_feedback_detail/', views.website_feedback_detail, name='website_feedback_detail'),
    path ('website_feedback_delete/', views.website_feedback_delete, name='website_feedback_delete'),
    path ('course_management/', views.course_management, name='course_management'),
    path ('course_detail/', views.course_detail, name='course_detail'),
    path ('course_edit_post/', views.course_edit_post, name='course_edit_post'),
    path ('course_delete/', views.course_delete, name='course_delete'),
    path ('course_edit/', views.course_edit, name='course_edit'),
    path ('create_course_management/', views.create_course_management, name='create_course_management'),
    path ('feedback_detail/', views.feedback_detail, name='feedback_detail'),
    path ('lecturer_management/', lecturer_view.lecturer_management, name='lecturer_management'),
    path ('lecturer_edit/', lecturer_view.lecturer_edit, name='lecturer_edit'),
    path ('lecturer_save_post/', lecturer_view.lecturer_save_post, name='lecturer_save_post'),
    path ('lecturer_delete/', lecturer_view.lecturer_delete, name='lecturer_delete'),
    path ('lecturer_add/', lecturer_view.lecturer_add, name='lecturer_add'),
    path ('create_lecturer_account/', views.create_lecturer_account, name='create_lecturer_account'),
    path ('admin_report_review_detail/', views.admin_report_review_detail, name='admin_report_review_detail'),
]
