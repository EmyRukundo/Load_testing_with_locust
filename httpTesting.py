from locust import TaskSet, constant, task, HttpUser
import random


class myHTTPcast(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get status of 200")

    @task
    def get_random_status(self):
        status_codes = [100, 101, 102, 200, 201, 202, 203]
        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)

        print("random http status")


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    task = [myHTTPcast]
    wait_time = constant(1)
