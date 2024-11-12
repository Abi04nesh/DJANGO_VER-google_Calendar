from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from .utils import generate_google_calendar_link
from django.shortcuts import render



def home(request):
    return render(request, 'home.html')

def send_interview_notification(request):
    # Sample data for testing
    candidate_name = "sivaprakash"
    candidate_email = "abinesh.p.csd.2021@snsce.ac.in"
    hr_manager_email = "abinesh.p.ihub@snsgroups.com"
    interview_date = "2024-11-15"
    interview_time = "14:00"
    location = "SNS College of Engineering"

    # Generate Google Calendar link
    calendar_link = generate_google_calendar_link(candidate_name, interview_date, interview_time,location)

    # Render email templates with context
    hr_email_content = render_to_string('emails/hr_notification.html', {
        'candidate_name': candidate_name,
        'interview_date': interview_date,
        'interview_time': interview_time,
        'calendar_link': calendar_link,
    })
    
    candidate_email_content = render_to_string('emails/candidate_confirmation.html', {
        'candidate_name': candidate_name,
        'interview_date': interview_date,
        'interview_time': interview_time,
        'calendar_link': calendar_link,
    })

    # Send email to HR
    send_mail(
        subject="Interview Scheduled with Candidate",
        message="",
        html_message=hr_email_content,
        from_email="abi04nesh@gmail.com",
        recipient_list=[hr_manager_email],
    )

    # Send email to Candidate
    send_mail(
        subject="Your Interview Confirmation",
        message="",
        html_message=candidate_email_content,
        from_email="abi04nesh@gmail.com",
        recipient_list=[candidate_email],
    )

    return HttpResponse("Interview notification emails sent.")

def home(request):
    return render(request, 'home.html')



