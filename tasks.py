__author__ = 'Rene'

from celery import Celery
import time

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y

def main():
    result=add.delay(33,4)
    time.sleep(2)
    print result.status
    # while result.ready() is False:
    #     print result.status
    # result= result.collect()

    # while result.ready() is False:
    #     print result.status

    print result
    # print result.backend
if __name__ == "__main__":
    main()