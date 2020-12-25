from django.urls import path
from .views import addReportView, index, myReportsView, processReportView, singleReportView

urlpatterns = [
    path('', index, name='index'),
    path('<int:userid>/report/', addReportView, name='add-report'),
    path('<int:userid>/reports/', myReportsView, name='my-reports'),
    path('reports/<int:report_id>/', singleReportView, name='comment-receipt'),
    path('reports/<int:report_id>/process',
         processReportView, name='process-report')
]
