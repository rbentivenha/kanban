from django.test import TestCase


from .models import Activity


class TestActivity(TestCase):
    def setUp(self):
        Activity.objects.create(
            name="Reunião de Negócios", description="Uma reunião muito importante", due_date="2020-08-08")
    
    def test_activities_is_delayed(self):
        activity = Activity.objects.get(name="Reunião de Negócios")
        self.assertEqual(activity.is_delayed(), True)