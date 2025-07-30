from playwright.async_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.ventas_button = page.locator("//*[@id='bs-example-navbar-collapse-1']/ul[1]/li[2]/a")

    async def open(self):
        url = "https://demo.relbase.cl/"
        await self.page.goto(url)

    async def click_ventas(self):
        await expect(self.ventas_button).to_be_visible()
        await self.ventas_button.click()