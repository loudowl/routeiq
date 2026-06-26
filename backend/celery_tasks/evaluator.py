from celery import Celery

app = Celery('evaluator', broker='redis://localhost:6379/0')

@app.task
def evaluate():
    # Placeholder for evaluation task
    print("Running evaluation task")
