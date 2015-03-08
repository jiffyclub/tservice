T-Service
=========

.. image:: https://pypip.in/version/tservice/badge.svg
    :target: https://pypi.python.org/pypi/tservice/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/tservice/badge.svg
    :target: https://pypi.python.org/pypi/tservice/
    :alt: Supported Python versions

.. image:: https://pypip.in/wheel/tservice/badge.svg
    :target: https://pypi.python.org/pypi/tservice/
    :alt: Wheel Status

T-Service is a tiny Python tool for starting a local static file server
using `Tornado <http://www.tornadoweb.org/en/stable/>`__.
I use it for previewing sites before pushing them to
`GitHub Pages <https://pages.github.com/>`__.

Installation
------------

T-Service is on PyPI, install it with: ``pip install tservice``.

Usage
-----

T-Service installs a command line utility called ``tserve``.
``tserve`` has one required parameter:
the directory from which to serve files.
For example, to start the server from a directory called ``build``
that's in your current directory, use this command::

    tserve build

The server starts on port 8000 by default, so you can look for your
site at ``http://localhost:8000``.

Specifying a Port
~~~~~~~~~~~~~~~~~

If port 8000 is in use, or you want to use a different port, use the
``-p``/``--port`` flag::

    tserve --port 7654 build

Specifying a Prefix
~~~~~~~~~~~~~~~~~~~

If you need to run the server so that it serves the files from some prefix
use the ``-f``/``--prefix`` flag::

    tserve --prefix myusername build

That will cause the files to be served from
``http://localhost:8000/myusername/``.
(You may need to do this so that the local site matches where your
site will be deployed, e.g. GitHub Pages or a university server.)

Stopping the Server
~~~~~~~~~~~~~~~~~~~

Type ``control-C`` at the command line to stop the server.

Why Not Use Python's Server?
----------------------------

I've found I sometimes need to serve files with a prefix on the URL,
and I don't know how to do that with Python's
`builtin server <https://docs.python.org/3/library/http.server.html#module-http.server>`__.
