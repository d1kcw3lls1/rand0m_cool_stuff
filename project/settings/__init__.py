import os

HOST_ENV = os.environ.get('HOST_ENV')

if HOST_ENV == 'prod':
    from .prod import *  # noqa

elif HOST_ENV == 'heroku':
    from .heroku import *  # noqa

else:
    from .dev import *  # noqa

if True:
    try:
        from .dev_secrets import *  # noqa
    except ModuleNotFoundError:
        pass
