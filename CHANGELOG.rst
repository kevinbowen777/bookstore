.. _`changelog`:

=========
Changelog
=========

``bookstore`` issues are filed on `GitHub <https://github.com/kevinbowen777/bookstore/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

bookstore 0.3.7 (2026-09-02)
============================

Contributor-facing changes
--------------------------

-  (`#642 <https://github.com/kevinbowen777/bookstore/642>`_): Initial zizmor remediation. Pin GitHub actions to hashes.

-  (`#645 <https://github.com/kevinbowen777/bookstore/645>`_): Update testing to Python 3.14.7, 3.13.15, and 3.12.14

-  (`#645 <https://github.com/kevinbowen777/bookstore/645>`_): Update django-allauth to 65.19.1

-  (`#645 <https://github.com/kevinbowen777/bookstore/645>`_): Update nox to 2026.8.10

-  (`#645 <https://github.com/kevinbowen777/bookstore/645>`_): Update django-debug-toolbar to 7.1.0

-  (`#649 <https://github.com/kevinbowen777/bookstore/649>`_): Update django-allauth to 65.19.2

-  (`#649 <https://github.com/kevinbowen777/bookstore/649>`_): Update Trove classifier

-  (`#649 <https://github.com/kevinbowen777/bookstore/649>`_): Update nox to 2026.8.17

-  (`#649 <https://github.com/kevinbowen777/bookstore/649>`_): Update psycopg to 3.3.5

-  (`#649 <https://github.com/kevinbowen777/bookstore/649>`_): Update django-debug-toolbar to 8.0.0


New features
------------

-  (`#649 <https://github.com/kevinbowen777/bookstore/649>`_): Upgrade to Django 6.1

bookstore 0.3.6 (2026-08-08)
============================

Improved documentation
----------------------

-  (`#642 <https://github.com/kevinbowen777/bookstore/642>`_): Add towncrier 25.8.0.

bookstore 0.3.5 (2026-07-22)
============================

Contributor-facing changes
--------------------------

-  (`#635 <https://github.com/kevinbowen777/bookstore/635>`_): Update with Python 3.14.6 & 3.13.14.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#631 <https://github.com/kevinbowen777/bookstore/631>`_): Drop support for Python 3.11.


New features
------------

-  (`#603 <https://github.com/kevinbowen777/bookstore/603>`_): Upgrade to Django 6.0.7

bookstore 0.3.4 (2025-11-28)
============================

Contributor-facing changes
--------------------------

-  (`#589 <https://github.com/kevinbowen777/bookstore/589>`_): Add Python 3.14 support.


New features
------------

-  (`#592 <https://github.com/kevinbowen777/bookstore/592>`_): Upgrade Django to 5.2.8.

bookstore 0.3.3 (2025-04-29)
============================

Contributor-facing changes
--------------------------

-  (`#533 <https://github.com/kevinbowen777/bookstore/533>`_): Upgrade PostgreSQL to 15.11.

-  (`#543 <https://github.com/kevinbowen777/bookstore/543>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#541 <https://github.com/kevinbowen777/bookstore/541>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#539 <https://github.com/kevinbowen777/bookstore/539>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#480 <https://github.com/kevinbowen777/bookstore/480>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#545 <https://github.com/kevinbowen777/bookstore/545>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#547 <https://github.com/kevinbowen777/bookstore/547>`_): Replace safety package with pip-audit.

bookstore 0.3.2 (2025-01-07)
============================

Contributor-facing changes
--------------------------

-  (`#470 <https://github.com/kevinbowen777/bookstore/470>`_): Upgrade to psycopg 3.

-  (`#476 <https://github.com/kevinbowen777/bookstore/476>`_): Add support for Python 3.13

-  (`#518 <https://github.com/kevinbowen777/bookstore/518>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#510 <https://github.com/kevinbowen777/bookstore/510>`_): Upgrade Django to 5.1.4

bookstore 0.3.0 (2023-12-21)
============================

Contributor-facing changes
--------------------------

-  (`#201 <https://github.com/kevinbowen777/bookstore/201>`_): Migrate to non-root Docker user & venv.

-  (`#341 <https://github.com/kevinbowen777/bookstore/341>`_): Bump Safety version to 2.4.0.

-  (`#379 <https://github.com/kevinbowen777/bookstore/379>`_): Upgrade Poetry to 1.7.0.

-  (`#388 <https://github.com/kevinbowen777/bookstore/388>`_): Update Python to 3.12.1.


New features
------------

-  (`#384 <https://github.com/kevinbowen777/bookstore/384>`_): Upgrade to Django 5.0.

bookstore 0.2.0 (2023-05-07)
============================

Contributor-facing changes
--------------------------

-  (`#213 <https://github.com/kevinbowen777/bookstore/213>`_): Install ruff. Drop flake8-* packages.

bookstore 0.1.0 (2023-05-05)
============================

Contributor-facing changes
--------------------------

- : Drop pipenv for project management. Add Poetry.

-  (`#108 <https://github.com/kevinbowen777/bookstore/108>`_): Mirror to GitLab.

-  (`#137 <https://github.com/kevinbowen777/bookstore/137>`_): Implement gunicorn for testing

-  (`#139 <https://github.com/kevinbowen777/bookstore/139>`_): Add support for Python 3.12.

-  (`#198 <https://github.com/kevinbowen777/bookstore/198>`_): Migrate test sqlite db to PostgreSQL

-  (`#216 <https://github.com/kevinbowen777/bookstore/216>`_): Update Poetry to 1.4.1.

-  (`#221 <https://github.com/kevinbowen777/bookstore/221>`_): Migrate PostgreSQL to 15.2


New features
------------

-  (`#218 <https://github.com/kevinbowen777/bookstore/218>`_): Upgrade to Django 4.2.

bookstore 0.0.1 (2022-02-23)
============================

New features
------------

- : Build Docker support for Heroku deployment.

- : Support Django 4.0.3, Python 3.9.12.


Miscellaneous internal changes
------------------------------

- : Initial commit
