from worker import app, generate_random_number # This are the Celery and the Function 
from time import sleep
from celery.result import AsyncResult


sleep(5)
result_future = generate_random_number.delay(100) # Using .delay() to call the task asynchronously and in background
result_future2= generate_random_number.delay(250)
result_future3= generate_random_number.delay(98)

result_futures = [result_future, result_future2, result_future3]
result = [AsyncResult(rf.id, app=app) for rf in result_futures ]  # Getting the result using the task id and the Celery app

print('Submitted task')
print(result.state) # Result stages : ready, pending, started, etc.

while True:
    if not result:
        break

    for r in result:
        if r.ready():
            print(r.get())  # Getting the result when it's ready
            result.remove(r)

    sleep(1)