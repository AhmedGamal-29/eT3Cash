
#!/bin/sh
celery -A smart_wallet worker --loglevel=INFO --concurrency=1 -Q et3cash -n et3cash@%h

