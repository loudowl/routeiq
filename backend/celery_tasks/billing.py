from celery import Celery

app = Celery('billing', broker='redis://localhost:6379/0')

@app.task
def generate_invoice():
    # Placeholder for billing task
    print("Generating invoice")
