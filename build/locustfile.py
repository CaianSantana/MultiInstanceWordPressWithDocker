from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    
    @task
    def index(self):
        self.client.get("/?p=1")
    '''
    @task
    def view_post(self):
        self.client.get("/?p=5")
    '''

        
class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
