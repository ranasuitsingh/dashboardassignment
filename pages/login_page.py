class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = "#email"
        self.password_input = "#password"
        self.login_button = "#loginBtn"

    def goto(self):
        self.page.goto("https://example.com/login")

    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
