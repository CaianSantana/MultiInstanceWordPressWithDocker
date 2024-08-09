from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task(3)
    def view_post(self):
        self.client.get("/?p=12")


        
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)