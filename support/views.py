import csv
import io

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.db.models.query_utils import Q
from django.http import FileResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
# pdf stuff
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

import support
from support.form import UserForm
from support.forms import NewUserForm
from support.models import Support


# Generate a PDF File Venue List
def task_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text
    # lines = [
    #	"This is line 1",
    #	"This is line 2",
    #	"This is line 3",
    # ]

    # Designate The Model
    tasks = Support.objects.all()

    # Create blank list
    lines = []

    for task in tasks:
        lines.append(task.name)
        lines.append(task.date_created)
        lines.append(task.extension)
        lines.append(task.department)
        lines.append(task.summary)
        lines.append(task.category)
        lines.append(task.assigned)
        lines.append(task.solution)
        lines.append(task.status)
        lines.append(" ")

    # Loop
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something
    return FileResponse(buf, as_attachment=True, filename='task.pdf')


# Generate CSV File Venue List
def task_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=tasks.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model
    tasks = Support.objects.all()

    # Add column headings to the csv file
    writer.writerow(['Name', 'Date', 'Extension', 'Department', 'Summary', 'category', 'assigned', 'solution', 'status'])

    # Loop Thu and output
    for task in tasks:
        writer.writerow([task.name, task.date_created, task.extension, task.department, task.summary, task.category, task.assigned, task.solution, task.status])

        return response


# Generate Text File Venue List
def task_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=task.txt'
    # Designate The Model
    tasks = Support.objects.all()

    # Create blank list
    lines = []
    # Loop Thu and output
    for task in tasks:
        lines.append(
            f'{task.id}\n{task.name}\n{task.date_created}\n{task.extension}\n{task.department}\n{task.summary}\n{task.category}\n{task.assigned}\n{task.solution}\n{task.status}\n\n\n')

    # lines = ["This is line 1\n",
    # "This is line 2\n",
    # "This is line 3\n\n",
    # "John Elder Is Awesome!\n"]

    # Write To TextFile
    response.writelines(lines)
    return response


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def Homepage(request):
    supports = Support.objects.all().order_by('-id')
    # pagination set up
    p = Paginator(Support.objects.all(), 10)
    page = request.GET.get('page')
    mytask = p.get_page(page)

    return render(request, 'main.html',
                  {'supports': supports,
                   'mytask': mytask}
                  )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("/")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def networking(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User form request submitted successfully.')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = UserForm()
    return render(request, 'networking.html', {'form': form})


def workshop(request):
    context = {}
    return render(request, 'workshop.html', context)


def index(request):
    supports = Support.objects.all()
    # pagination set up
    p = Paginator(Support.objects.all(), 10)
    page = request.GET.get('page')
    mytask = p.get_page(page)

    return render(request, 'crud/index.html',
                  {'supports': supports,
                   'mytask': mytask}
                  )


def add_task(request):
    if request.method == "POST":
        name = request.POST.get('name')
        extension = request.POST.get('extension')
        department = request.POST.get('department')
        summary = request.POST.get('summary')
        category = request.POST.get('category')
        assigned = request.POST.get('assigned')
        solution = request.POST.get('solution')
        status = request.POST.get('status')

        supports = Support(
            name=name,
            extension=extension,
            department=department,
            summary=summary,
            category=category,
            assigned=assigned,
            solution=solution,
            status=status,
        )
        supports.save()
    return redirect('index')


def Edit(request):
    supports = support.objects.all()
    context = {
        supports: supports,
    }
    return redirect(request, 'crud/index.html', context)


def Update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        extension = request.POST.get('extension')
        department = request.POST.get('department')
        summary = request.POST.get('summary')
        category = request.POST.get('category')
        assigned = request.POST.get('assigned')
        solution = request.POST.get('solution')
        status = request.POST.get('status')

        supports = Support(

            id=id,
            name=name,
            extension=extension,
            department=department,
            summary=summary,
            category=category,
            assigned=assigned,
            solution=solution,
            status=status,
        )
        supports.save()
        messages.success(request, "Task updated successfully")
        return redirect('index')


def Delete(request, id):
    supports = Support.objects.filter(id=id)
    supports.delete()
    messages.warning(request, "Task deleted successfully")
    return redirect('index')
