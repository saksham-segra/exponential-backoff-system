from celery import shared_task

from core.tasks import ExponentialBackoffRetryTask


@shared_task(base=ExponentialBackoffRetryTask, name='payments.tasks.update_payment_status')
def update_payment_status(payment_id):
    # simulating a failing task
    raise ValueError
