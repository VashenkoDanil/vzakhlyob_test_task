from vzakhlyob_test_task.celery import app
from .send_email import send_activate_account_email as send


@app.task
def send_activate_account_email(user_id, site_domain):
    send(user_id, site_domain)
