import os
if 'TRAVIS' in os.environ:
    from wanderit.production_settings import *
else:
    from wanderit.local_settings import *