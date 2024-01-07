from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# View for accepting user input and creating a new profile
def accept(request):
    if request.method == "POST":
        # Retrieve user input from the form
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")

        # Create a new Profile object and save it to the database
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)
        profile.save()

    # Render the accept.html template
    return render(request, 'pdf/accept.html')

# View for generating a PDF resume for a specific user profile
def resume(request, id):
    # Retrieve the user profile from the database using the provided id
    user_profile = Profile.objects.get(pk=id)

    # Render the resume.html template with the user profile data
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})

    # Convert the HTML to a PDF using pdfkit
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)

    # Create and return a PDF response for download
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response

# View for listing all user profiles
def list(request):
    # Retrieve all profiles from the database
    profiles = Profile.objects.all()

    # Render the list.html template with the profile data
    return render(request, 'pdf/list.html', {'profiles': profiles})
