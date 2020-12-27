from django.forms.fields import NullBooleanField
from django.test import TestCase
from .models import SafetyReport
from django.contrib.auth.models import User

# Create your tests here.


class SafetyReportTest(TestCase):

    def setUp(self) -> None:
        SafetyReport.objects.create(
            date='2020-12-27', description='Test', reporter=User.objects.create())

    def test_report_conforms(self):
        report = SafetyReport.objects.get(description='Test')
        self.assertEqual(report.description, 'Test')
