django-profilers
================

Небольшой набор профайлеров для django
--------------------------------------

**UWSGI middleware**

Зависимости:

 - https://github.com/repoze/repoze.profile

Для использования в dev-окружении необходимо скопировать содержимое папки к файлу manage.py в вашем проекте
и выполнить команду:

    ```
    $ python rundebugserver.py profiler_django_uwsgi.py
    ```

Для использования в production-среде необходимо использовать profiler_django_uwsgi.py вместо django_uwsgi.py.
В файле profiler_django_uwsgi.py можно задать папку и исходное имя файла для логов, при каждом запросе будет создаваться отчет профайлера, который можно просмотреть с помощью утилит qcachegrind или kcachegrind.

**Debug Toolbar**

Зависимости:

 - https://github.com/django-debug-toolbar/django-debug-toolbar
 - hotshot
 - profile

DTB подключается как обычный django app, далее в настройках к стандартному списку панелей необходимо подключить:

   ```
   DEBUG_TOOLBAR_PANELS = (
       ...
       'debug_toolbar.panels.debug_profiling.ProfilingPanel',
       'debug_toolbar.panels.profiling.ProfilingDebugPanel',
       ...
   )
   ```

ProfilingDebugPanel доступна по умолчанию, для подключения ProfilingPanel необходимо скопировать соответсвующий файл из этого репозитория в удобное для вас место.
Теперь на каждой странице вашего приложения в DTB будут сформированы два отчета.