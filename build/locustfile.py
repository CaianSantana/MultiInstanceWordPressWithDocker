from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_main_page(self):
        self.client.get("/")