import os.path
import shlex
import time
from contextlib import contextmanager
from subprocess import Popen

import pytest
import requests


@contextmanager
def tservice(port=None, prefix=None):
    args = 'tserve {}'.format(os.path.dirname(__file__))

    if port:
        args += ' --port {}'.format(port)
    if prefix:
        args += ' --prefix {}'.format(prefix)

    p = Popen(shlex.split(args))
    # give time for the tornado server to get up and running
    time.sleep(0.5)
    yield
    p.terminate()


@pytest.fixture(params=[None, 9999])
def port(request):
    return request.param


@pytest.fixture(params=[None, 'prefix'])
def prefix(request):
    return request.param


def test_tservice(port, prefix):
    port = port or 8000  # default port in tservice
    prefix = prefix or ''

    url = 'http://localhost:{}/{}/test_tservice.py'.format(
        port, prefix).replace('//test_tservice', '/test_tservice')

    with tservice(port=port, prefix=prefix):
        result = requests.get(url)

    result.raise_for_status()
    assert 'tservice' in result.text
