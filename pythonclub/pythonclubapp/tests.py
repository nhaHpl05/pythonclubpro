from django.test import TestCase
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getResource, getMeeting, getMeetingDetails
from .forms import MeetingForm, ResourceForm

# Create your tests here.

class MeetingTest(TestCase):
    def setUp(self):
        self.meetingName = Meeting(meeting_title = 'python model reviews',meeting_date = '2020-05-12',)
        self.assertEqual(str(self.meetingName), self.meetingName.meeting_title, self.meetingName.meeting_date,)
    
    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinuteTest(TestCase):
    def setUp(self):
        self.meetingName = Meeting(meeting_title ='python model reviews')
        self.meetingMinutes = MeetingMinutes(meetTitle = self.meetingName, attendance = 8, minutes_text = '30 minutes')

    def string_test(self):
        minute = self.setUp()
        self.assertEqual(str(self.minute), minute.attendance, 8, minute.minutes_text, '30 minutes', minute.meetTitle, 'python model reviews')
        self.assertEqual(str(table._meta.db_table), 'MeetingMinute')

class TestResource(TestCase):
    def test_string(self):
        res = Resource(resource_name = 'python turtorials')
        self.assertEqual(str(res), res.resource_name)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'Resource')
        
class TestEvent(TestCase):
    def test_string(self):
        eve = Event(event_title = 'Meeting on Thursday')
        self.assertEqual(str(eve), eve.event_title)


#Test for views

class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        self.response = self.client.get(reverse('index'))
        self.assertEqual(self.response.status_code, 200)

class TestGetResource(TestCase):
    def test_view_url_accessible_by_name(self):
        self.response = self.client.get(reverse('resource'))
        self.assertEqual(self.response.status_code, 200)

class TestgetMeeting(TestCase):
    def test_view_url_accessible_by_name(self):
        self.response = self.client.get(reverse('meeting'))
        self.assertEqual(self.response.status_code, 200)

class TestMeetingDetail(TestCase):
    def setUp(self):
        self.u = User.objects.create(username='MyName')
        self.meet = Meeting.objects.create( meeting_title = 'django tutorials', meeting_date='2020-05-12', meeting_time='10:30 a.m', location='room100')
      


    def test_meeting_details_sucesss(self):
        response = self.client.get(reverse('meetingdetails', args=(self.meet.id,)))
        # Assert that self-post is actually return by the post-detail view
        self.assertEqual(response.status_code, 200)
class Form_Meeting_Test(TestCase):
    def test_typeform_is_valid(self):
        form = MeetingForm(data = {'meeting_title' : "meeting test", 'meeting_date': "2020-06-03", 'meeting_time': "2:30 p.m"})
        self.assertTrue(form.is_valid())

    def test_typeform_title(self):
        form = MeetingForm(data = {'meeting_title' : "meeting test"})
        self.assertTrue(form.is_valid())

class Form_Resource_Test(TestCase):
    def test_typeform_is_valid(self):
        form = ResourceForm(data = {'resource_name': "resource1", 'resource_type': "resourcetype", 'date_entered': "2020-05-12", 'user_id': "me", 'description': "one description"})
        self.assertTrue(form.is_valid())

#Test authentication

class Create_Meeting_with_Resource_authentication():
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser1', password='Password1')
        self.meeting = Meeting.objects.create(meeting_title='python disscuss')
        self.resource = Resource.objects.create(resource_name='django turtorial', resource_type='tutorial', URL='django.turtorial.com' )
    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('resourceform'))
        self.assertRedirects(response, '/accounts/login/?next=/pythonclubapp/FormResource/')

    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='Password1')
        response = self.client.get(reverse('resourceform'))
        self.assertEqual(str(response.context['user'],'testuser1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pythonclubapp/resourceform.html')

    
    

  




        