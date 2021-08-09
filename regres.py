from locust import HttpUser, constant, task

class MyRegRes(HttpUser):

    host = "https://regres.in"
    wait_time = constant(1)


    @task
    def get_users(self):
       res = self.client.get("/api/users?page=2")
       print(res.text)
       print(res.status_code)
       print(res.headers)


    @task
    def create_user(Self):
        res = Self.client.post("/api/users", data='''{"name": "morpheus", "job": "leader"} ''')
        print(res.text)
        print(res.status_code)
        print(res.headers)