import csv
import datetime
import tempfile

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
# pdf stuff
from weasyprint import HTML

from support.form import UserForm
from support.models import Support


def search_task(request):
    if request.method == "POST":
        searched = request.POST['searched']
        supports = Support.objects.filter(name__contains=searched)

        return render(request,
                      'search_task.html',
                      {'searched': searched,
                       'supports': supports})
    else:
        return render(request,
                      'search_task.html',
                      {})


# Generate a PDF File Venue List
def task_pdf(request):
    """Generate pdf."""
    # Model data
    supports = Support.objects.filter(pk__lte=200).order_by('-id')

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

    # # Create Bytestream buffer
    # buf = io.BytesIO()
    # # Create a canvas
    # c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # # Create a text object
    # textob = c.beginText()
    # textob.setTextOrigin(inch, inch)
    # textob.setFont("Helvetica", 14)
    #
    # # Add some lines of text
    # # lines = [
    # #	"This is line 1",
    # #	"This is line 2",
    # #	"This is line 3",
    # # ]
    #
    # # Designate The Model
    # tasks = Support.objects.all()
    #
    # # Create blank list
    # lines = []
    #
    # for task in tasks:
    #     lines.append(task.id)
    #     lines.append(task.name)
    #     lines.append(" ")
    #
    # # Loop
    # for line in lines:
    #     textob.textLine(line)
    #
    # # Finish Up
    # c.drawText(textob)
    # c.showPage()
    # c.save()
    # buf.seek(0)
    #
    # # Return something
    # return FileResponse(buf, as_attachment=True, filename='task.pdf')


# Generate CSV File Venue List
def task_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'inline; attachment; filename=tasks' + str(datetime.datetime.now()) + '.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate The Model

    tasks = Support.objects.all().order_by('-id')

    # Add column headings to the csv file
    writer.writerow(
        ['Name', 'NO', 'Date', 'Extension', 'Department', 'Summary', 'category', 'assigned', 'solution', 'status'])

    # Loop Thu and output
    for task in tasks:
        writer.writerow(
            [task.name, task.id, task.date_created, task.extension, task.department, task.summary, task.category,
             task.assigned,
             task.solution, task.status])

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
    if request.user.is_staff:
        context = {}
        return render(request, 'workshop.html', context)
    else:
        messages.error(request, "You Aren't Authorized To View This Page")
        return redirect('/')


def index(request):
    supports = Support.objects.all().order_by('-id')

    # pagination set up
    # p = Paginator(Support.objects.all().order_by('-id'), 10)
    # page = request.GET.get('page')
    # mytask = p.get_page(page)

    return render(request, 'crud/index.html', {'supports': supports})
    # include -- 'mytask': mytask -- to use in pagination. now have used data tables instead


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
    messages.success(request, "Task added successfully")
    return redirect('index')


def Edit(request):
    supports = Support.objects.all()
    context = {
        supports: supports,
    }
    return redirect(request, 'crud/index.html', context)


def Update(request, id):
    if request.user.is_staff:
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
    else:
        messages.warning(request, "You are not authorized to make changes")
        return redirect('/')


def Delete(request, id):
    if request.user.is_superuser:
        supports = Support.objects.filter(id=id)
        supports.delete()
        messages.warning(request, "Task deleted successfully")
        return redirect('index')
    else:
        messages.warning(request, "You are not authorized for such operations")
        return redirect('/')


def handle_not_found(request, exception):
    return render(request, 'not_found.html')