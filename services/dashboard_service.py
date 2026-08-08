from framework.pages.dashboardpage import DashboardPage
from playwright.sync_api import expect
class DashboardService:

    def __init__(self, page):
            self.dashboardpage=DashboardPage(page)

    