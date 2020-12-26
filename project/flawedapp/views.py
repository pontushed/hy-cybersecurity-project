from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import SafetyReport


@login_required
def index(request):
    return render(request, 'pages/main.html', {"user": request.user})


# Flaws:
# Sensitive Data Exposure
# Broken Authentication
# Broken Access Control
# If a logged in user changes the start of the URL <userid>/reports to another user id, then the reports of that user can be seen
# Fix:
# Change line user = User.objects.get(id=userid) to user = request.id

@login_required
def myReportsView(request, userid):
    user = User.objects.get(id=userid)
    if request.GET.get("search"):
        searchTerm = request.GET.get("search")
        reports = SafetyReport.objects.filter(
            reporter=user, description__contains=searchTerm) | SafetyReport.objects.filter(reviewer=user, description__contains=searchTerm)
        return render(request, 'pages/my-reports.html', {"reports": reports})

    reports = SafetyReport.objects.filter(
        reporter=user) | SafetyReport.objects.filter(reviewer=user)
    return render(request, 'pages/my-reports.html', {"reports": reports})


# Flaws:
# Cross-Site Scripting XSS
# Injection
#
# Explanation: This function is forcefully disabling Django's built-in CSRF protection and this will allow anyone to
# post a new report on behalf of another user, if the ID is known. The description field allows SQL injection.
# Fix:
# Remove the @csrf_exempt decorator
# Comment lines 60-62
# Uncomment lines 63-65


@csrf_exempt
def addReportView(request, userid):
    reporter = User.objects.get(id=userid)
    if not request.POST:
        users = User.objects.exclude(username=request.user.username)
        return render(request, 'pages/report.html', {'users': users})
    else:
        reviewer = request.user
        date = request.POST.get("date")
        description = request.POST.get("description")
        # report = SafetyReport.objects.create(
        #    date=date, description=description, reporter=reporter)
        # report.save()
        with connection.cursor() as cursor:
            cursor.executescript("INSERT INTO flawedapp_safetyreport (date, description, reporter_id, processed) VALUES ('" +
                                 date + "','" + description + "'," + str(reporter.id) + ", FALSE)")
        return redirect('/' + str(reporter.id) + '/reports')

# Flaws:
# Broken Authentication
# Broken Access Control
# Explanation: A logged in user can change the status of any report by using the ID in the URL
# Fix:
# Add a check for reviewer, and change the status only if reviewer.id matches request.user.id.


@login_required
def processReportView(request, report_id):
    report = SafetyReport.objects.get(id=report_id)
    # if report.reviewer.id == request.user.id:
    report.processed = True
    report.save()
    return redirect('/reports')
