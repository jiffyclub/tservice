import os

import tornado.ioloop
import tornado.web


class Handler(tornado.web.StaticFileHandler):
    def parse_url_path(self, url_path):
        if not url_path or url_path.endswith('/'):
            url_path = url_path + 'index.html'
        return url_path


def mkapp(prefix=None):
    if prefix:
        path = '/' + prefix + '/(.*)'
    else:
        path = '/(.*)'

    application = tornado.web.Application(
        [(path, Handler, {'path': os.getcwd()})],
        debug=True)

    return application


def start_server(prefix=None, port=8000):
    app = mkapp(prefix)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
