import csv
import datetime
import tempfile

from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


# pdf stuff
from weasyprint import HTML

from .forms import UserForm
from .models import Support


# Generate a PDF File Venue List
def task_pdf(request):
    """Generate pdf."""
    # Model data
    supports = Support.objects.filter(pk__lte=200, owner=request.user).order_by('-id')

    # Rendered
    html_string = render_to_string('task/pdf_output.html', {'supports': supports})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output.seek(0)
        response.write(output.read())

    return response


# Generate CSV File Venue List
def task_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'inline; attachment; filename=tasks' + str(datetime.datetime.now()) + '.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model

    tasks = Support.objects.filter(owner=request.user).order_by('-id')

    # Add column headings to the csv file
    writer.writerow(
        ['Name', 'NO', 'Date', 'Extension', 'Department', 'Summary', 'category', 'priority', 'solution', 'status'])

    # Loop Thu and output
    for task in tasks:
        writer.writerow(
            [task.name, task.id, task.date_created, task.extension, task.department, task.summary, task.category,
             task.priority,
             task.solution, task.status])

    return response


# Generate Text File Venue List
def task_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=task.txt'
    # Designate The Model
    tasks = Support.objects.filter(owner=request.user).order_by('-id')

    # Create blank list
    lines = []
    # Loop Thu and output
    for task in tasks:
        lines.append(
            f'{task.id}\n{task.name}\n{task.date_created}\n{task.extension}\n{task.department}\n{task.summary}\n{task.category}\n{task.priority}\n{task.solution}\n{task.status}\n\n\n')

    # lines = ["This is line 1\n",
    # "This is line 2\n",
    # "This is line 3\n\n",
    # "John Elder Is Awesome!\n"]

    # Write To TextFile
    response.writelines(lines)
    return response


def new_task(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'User form request submitted successfully.')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = UserForm()
    return render(request, 'new_task.html', {'form': form})


def workshop(request):
    context = {}
    return render(request, 'workshop.html', context)


def assigned_tasks(request):
    assigned_tasks = Support.objects.filter(assigned_to=request.user)
    context = {'assigned_tasks': assigned_tasks}
    return render(request, 'crud/assigned_tasks.html', context)


def index(request):
    # get Counts
    task_count = Support.objects.all().count
    user_count = User.objects.all().count

    high_count = Support.objects.filter(priority='High').count()
    medium_count = Support.objects.filter(priority='Medium').count()
    low_count = Support.objects.filter(priority='Low').count()    

    new_count = Support.objects.filter(status='New').count()
    completed_count = Support.objects.filter(status='Completed').count()
    review_count = Support.objects.filter(status='Review').count()    

    status_list = ['New', 'Completed', 'Review']
    status_number = [new_count, completed_count, review_count]

    priority_list =['High', 'Medium', 'Low']
    priority_number = [high_count, medium_count, low_count]


    supports = Support.objects.filter(owner=request.user).order_by('-id')

    # supports = Support.objects.order_by('-id')


    # pagination set up
    # p = Paginator(Support.objects.all().order_by('-id'), 10)
    # page = request.GET.get('page')
    # mytask = p.get_page(page)




    context = {
        'supports': supports,
        'task_count': task_count,
        'user_count': user_count,
        'new_count': new_count,
        'completed_count': completed_count,
        'review_count': review_count,
        'status_list': status_list,
        'status_number': status_number,
        'priority_list': priority_list,
        'priority_number': priority_number,

    }

    return render(request, 'crud/index.html', context)


def add_task(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.instance.owner = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'User form request submitted successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = UserForm()
    return render(request, 'crud/index.html', {'form': form})


def Update(request, pk):
    supports = Support.objects.get(id=pk)
    if request.user == supports.owner:
        if request.method == 'POST':
            form = UserForm(request.POST, instance=supports)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ticket updated successfully.')
                return redirect('index')
        else:
            form = UserForm(instance=supports)
        context = {
            'form': form,
        }
        return render(request, 'crud/update_task.html', context)

    else:
        messages.warning(request, "You are not authorized to make such operations")
        return redirect('/')


def Delete(request, id):
    supports = Support.objects.filter(id=id)
    if request.user.is_superuser:
        supports.delete()
        messages.warning(request, "Task deleted successfully")
        return redirect('index')

    else:
        messages.warning(request, "You are not authorized for such operations")
        return redirect('/')


def error_404(request, exception):
    data = {}
    return render(request, 'support/404.html', data)


def error_500(request, exception):
    data = {}
    return render(request, 'support/500.html', data)
