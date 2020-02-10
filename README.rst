======
djoser
======

Requirements
============

To be able to run **djoser** you have to meet following requirements:

- Python (3.5, 3.6, 3.7, 3.8)
- Django (1.11, 2.2)
- Django REST Framework (3.9, 3.10)

If you need to support other versions, please use djoser<2.

Installation
============

Simply install using ``pip``:

.. code-block:: bash

    $ pip install djoser

And continue with the steps described at
`configuration <https://djoser.readthedocs.io/en/latest/getting_started.html#configuration>`_
guide.

Documentation
=============

Documentation is available to study at
`https://djoser.readthedocs.io <https://djoser.readthedocs.io>`_
and in ``docs`` directory.

Contributing and development
============================

To start developing on **djoser**, clone the repository:

.. code-block:: bash

    $ git clone git@github.com:sunscrapers/djoser.git

If you are a **pipenv** user you can quickly setup testing environment by
using Make commands:

.. code-block:: bash

    $ make init
    $ make test

Otherwise, if you cannot use Make commands, please create virtualenv and install
requirements manually:

.. code-block:: bash

    $ pip install django djangorestframework
    $ pip install -r requirements.txt

.. code-block:: bash

    $ cd testproject
    $ ./manage.py test

If you need to run tests against all supported Python and Django versions then invoke:

.. code-block:: bash

    $ pip install tox
    $ tox -p all

You can also play with test project by running following commands:

.. code-block:: bash

    $ ./manage.py migrate
    $ ./manage.py runserver

Similar projects
================

List of projects related to Django, REST and authentication:

- `django-rest-framework-simplejwt <https://github.com/davesque/django-rest-framework-simplejwt>`_
- `django-oauth-toolkit <https://github.com/evonove/django-oauth-toolkit>`_
- `django-rest-auth <https://github.com/Tivix/django-rest-auth>`_
- `django-rest-framework-digestauth <https://github.com/juanriaza/django-rest-framework-digestauth>`_ (not maintained)
