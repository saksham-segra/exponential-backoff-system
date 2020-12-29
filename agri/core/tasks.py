import random

import celery
from django.conf import settings


class ExponentialBackoffRetryTask(celery.Task):
    """Retry task class for all tasks that need to be auto retried."""
    autoretry_for = (Exception,)
    retry_kwargs = {'max_retries': settings.CELERY_MAX_RETRIES}
    retry_backoff_max = settings.CELERY_RETRY_BACKOFF_MAX
    retry_jitter = settings.CELERY_RETRY_JITTER

    def run(self, *args, **kwargs):
        super().run(*args, **kwargs)

    def retry(self, args=None, kwargs=None, exc=None, throw=True, eta=None, countdown=None,
              max_retries=None, **options):

        countdown = self._get_countdown(countdown)
        return super().retry(args, kwargs, exc, throw, eta, countdown, max_retries, **options)

    def _get_countdown(self, countdown):
        countdown = min(self.retry_backoff_max, countdown or 2 ** self.request.retries)

        if self.retry_jitter:
            countdown = int(random.randrange(countdown))
        return countdown
