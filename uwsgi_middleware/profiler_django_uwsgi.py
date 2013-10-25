import os
import sys
import datetime

from repoze.profile.profiler import AccumulatingProfileMiddleware, MiniRequest

sys.path.append('/usr/share/pyshared/django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hhcareerfair.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()


class CacheGrinderWsgiLog(AccumulatingProfileMiddleware):
    def __init__(self, *args, **kwargs):
        self.base_cachegrind_filename = kwargs['cachegrind_filename']
        super(CacheGrinderWsgiLog, self).__init__(*args, **kwargs)

    def __call__(self, environ, start_response):
        def time_stamped(fname, fmt='{fname}-%H-%M-%S-%f'):
            return datetime.datetime.now().strftime(fmt).format(fname=fname)

        tmp_request = MiniRequest(environ)
        path_name = tmp_request.path_info.strip("/").replace('/', '.') or "root"
        filename = '-'.join([self.base_cachegrind_filename, path_name])

        self.cachegrind_filename = time_stamped(filename)

        return super(CacheGrinderWsgiLog, self).__call__(environ, start_response)

application = CacheGrinderWsgiLog(
    application,
    log_filename='/tmp/djangoprofile.log',
    cachegrind_filename='/tmp/cachegrind',
    discard_first_request=True,
    flush_at_shutdown=True,
    path='/__profile__')
