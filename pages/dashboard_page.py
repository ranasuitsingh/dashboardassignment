class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.create_lead_btn = "#createLead"
        self.lead_items = ".lead-item"

    def click_create_lead(self):
        self.page.click(self.create_lead_btn)

    def is_lead_visible(self, name):
        return self.page.locator(self.lead_items, has_text=name).is_visible()
