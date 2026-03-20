class CreateLeadPage:
    def __init__(self, page):
        self.page = page
        self.name_input = "#name"
        self.email_input = "#leadEmail"
        self.phone_input = "#phone"
        self.save_button = "#saveLead"

    def create_lead(self, name, email, phone):
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.fill(self.phone_input, phone)
        self.page.click(self.save_button)
