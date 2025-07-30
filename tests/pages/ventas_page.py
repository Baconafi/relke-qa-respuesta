from playwright.async_api import Page, expect

class VentasPage:
    def __init__(self, page: Page):
        self.page = page
        self.nota_de_venta = page.locator("//*[@id='sidebar']/li[4]/a")

    async def open(self):
        url = "https://demo.relbase.cl/ventas"
        await self.page.goto(url)

    async def click_nota_de_venta(self):
        await expect(self.nota_de_venta).to_be_visible()
        await self.nota_de_venta.click()