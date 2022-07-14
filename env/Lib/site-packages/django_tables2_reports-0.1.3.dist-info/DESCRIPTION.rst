.. contents::

======================
django-tables2-reports
======================

.. image:: https://travis-ci.org/goinnn/django-tables2-reports.svg?branch=master
    :target: https://travis-ci.org/goinnn/django-tables2-reports

.. image:: https://badge.fury.io/py/django-tables2-reports.svg
    :target: https://pypi.python.org/pypi/django-tables2-reports

With django-tables2-reports you can get a report (CSV, XLS) of any `table <http://pypi.python.org/pypi/django-tables2/>`_  with **minimal changes** to your project

Requirements
============

* `Python <http://python.org>`_ (supports 2.7, 3.3, 3.4, 3.5, 3.6)
* `Django <http://pypi.python.org/pypi/django/>`_ (supports 1.3, 1.4, 1.5, 1.6, 1.7, 1.8. 1.9, 1.10, 1.11)
* `django-tables2 <http://pypi.python.org/pypi/django-tables2/>`_ 
* `xlwt <http://pypi.python.org/pypi/xlwt/>`_, `openpyxl <http://pythonhosted.org/openpyxl/>`_ or `pyExcelerator <http://pypi.python.org/pypi/pyExcelerator/>`_  (these are optionals, to export to xls; defaults to xlwt if available)


Installation
============

* In your settings:

::

    INSTALLED_APPS = (

        'django_tables2_reports',
    )


    TEMPLATE_CONTEXT_PROCESSORS = (

        'django.core.context_processors.static',

    )


    # This is optional

    EXCEL_SUPPORT = 'xlwt' # or 'openpyxl' or 'pyexcelerator'

Changes in your project
=======================

1.a Now your table should extend of 'TableReport'

::

    ############### Before ###################

    import django_tables2 as tables


    class MyTable(tables.Table):

        ...

    ############### Now ######################

    from django_tables2_reports.tables import TableReport


    class MyTable(TableReport):

        ...

1.b If you want to exclude some columns from report (e.g. if it is a column of buttons), you should set 'exclude_from_report' - the names of columns (as well as property 'exclude' in `table <http://pypi.python.org/pypi/django-tables2/>`_)

::

    class MyTable(TableReport):

        class Meta:
            exclude_from_report = ('column1', ...)
        ...

2.a. If you use a traditional views, now you should use other RequestConfig and change a little your view:

::

    ############### Before ###################

    from django_tables2 import RequestConfig


    def my_view(request):
        objs = ....
        table = MyTable(objs)
        RequestConfig(request).configure(table)
        return render_to_response('app1/my_view.html',
                                  {'table': table},
                                  context_instance=RequestContext(request))

    ############### Now ######################

    from django_tables2_reports.config import RequestConfigReport as RequestConfig
    from django_tables2_reports.utils import create_report_http_response

    def my_view(request):
        objs = ....
        table = MyTable(objs)
        table_to_report = RequestConfig(request).configure(table)
        if table_to_report:
            return create_report_http_response(table_to_report, request)
        return render_to_response('app1/my_view.html',
                                  {'table': table},
                                  context_instance=RequestContext(request))


If you have a lot of tables in your project, you can activate the middleware, and you do not have to change your views, only the RequestConfig import

::

    # In your settings 

    MIDDLEWARE_CLASSES = (

        'django_tables2_reports.middleware.TableReportMiddleware',
    )

    ############### Now (with middleware) ######################

    from django_tables2_reports.config import RequestConfigReport as RequestConfig

    def my_view(request):
        objs = ....
        table = MyTable(objs)
        RequestConfig(request).configure(table)
        return render_to_response('app1/my_view.html',
                                  {'table': table},
                                  context_instance=RequestContext(request))


2.b. If you use a `Class-based views <https://docs.djangoproject.com/en/dev/topics/class-based-views/>`_:

::

    ############### Before ###################

    from django_tables2.views import SingleTableView


    class PhaseChangeView(SingleTableView):
        table_class = MyTable
        model = MyModel


    ############### Now ######################

    from django_tables2_reports.views import ReportTableView


    class PhaseChangeView(ReportTableView):
        table_class = MyTable
        model = MyModel


Usage
=====

Under the table appear a CSV icon (and XLS icon if you have `xlwt <http://pypi.python.org/pypi/xlwt/>`_, `openpyxl <http://pythonhosted.org/openpyxl/>`_ or `pyExcelerator <http://pypi.python.org/pypi/pyExcelerator/>`_ in your python path), if you click in this icon, you get a CSV report (or xls report) with every item of the table (without pagination). The ordering works!


Development
===========

You can get the last bleeding edge version of django-tables2-reports by doing a clone
of its git repository::

  git clone https://github.com/goinnn/django-tables2-reports


Test project
============

In the source tree, you will find a directory called 'test_project'. It contains
a readily setup project that uses django-tables2-reports. You can run it as usual:

::

    cd test_project
    export PYTHONPATH=..
    python manage.py syncdb --noinput
    python manage.py runserver


Releases
========

0.1.0 (2017-06-19)
------------------
* maintenance release, 
* Django 1.8, 1.9, 1.10, 1.11 support,
* openpyxl > 2.0.0 support,
* recent django-tables2 support,
* new maintainer `Michał Pasternak <https://github.com/mpasternak>`_

0.0.10 (2014-10-13)
-------------------
* Fixes for xlsx Content-Type:
    * django-tables2-reports throws 500 Sever Error when report format is not recognized. 404 is more appropriate in this case.
    * django-tables2-reports sets Content-Type to application/vnd.ms-excel for xlsx files which causes warnings in Firefox. application/vnd.openxmlformats-officedocument.spreadsheetml.sheet is the correct Content-Type for xlsx
* Support to Django 1.7 (I'm sorry to the delay)
* Adding new feature: exclude_from_report
* And a little details
* Thanks to:
    * `Ramana Varanasi <https://github.com/sramana>`_
    * `Mihas <https://github.com/mihasK>`_
    * `Paulgueltekin <https://github.com/paulgueltekin>`_
    * `David Ray <https://github.com/daaray>`_

0.0.9 (2013-11-30)
------------------
* Compatible with the future version  of Django (>=1.7)
* Update the tests
* Refactor the code
* Fix a bug when the title of the sheet is longer than 31
* Thanks to:
    * `Pavel Zaytsev <https://github.com/stelzzz>`_


0.0.8 (2013-11-14)
------------------
* `Refactor the csv_to_excel module <https://github.com/goinnn/django-tables2-reports/commit/51c8cee2500f73ba8b823a81fc5ad9b3f2a62d83>`_. In the next release this package will be a pypi egg.
* Support for `openpyxl <http://pythonhosted.org/openpyxl/>`_
* Integration with travis and coveralls
* Fix an error if you use the theme paleblue
* Fix test with python 3
* Fix some details
* Test project
* Thanks to:
    * `Michał Pasternak <https://github.com/mpasternak>`_
    * `Mark Jones <https://github.com/mark0978>`_

0.0.7 (2013-08-29)
------------------

* Russian translations
* Thanks to:
    * `Armicron <https://github.com/armicron>`_


0.0.6  (2013-08-22)
-------------------

* Python3 support
* Polish translation
* Thanks to:
    * `Michał Pasternak <https://github.com/mpasternak>`_

0.0.5  (2013-07-03)
-------------------

* Improvements in the README
* Exportable to XLS with `xlwt <http://pypi.python.org/pypi/xlwt/>`_
* Thanks to:
    * `Crashy23 <https://github.com/Crashy23>`_
    * `Gamesbook <https://github.com/gamesbook>`_
    * And spatially to `Austin Phillips <https://github.com/austinphillips2>`_


0.0.4  (2013-05-17)
-------------------

* Escape csv data correctly during output
* The fields with commas now are not split into multiple columns
* Thanks to:
    * `Austin Phillips <https://github.com/austinphillips2>`_

0.0.3  (2012-07-19)
-------------------

* Fix a little error, when a column has line breaks. Now these are changed to espaces
* Details

0.0.2  (2012-07-18)
-------------------

* Add a default view (https://docs.djangoproject.com/en/dev/topics/class-based-views/)
* Exportable to XLS
* Update the README

0.0.1  (2012-07-17)
-------------------

* Initial release


