from playwright.async_api import Page, expect

class NotasVentasPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_nota_button = page.locator("//*[@id='btn-new-invoice']")
        self.nota_venta = page.locator("//*[@id='form-filter']/div[1]/div[1]/div/ul/li[1]/a")
        self.go_back_button = page.locator("//*[@id='content']/div[2]/ol/li[2]/a")
        self.nota_exitosa = page.get_by_role("alert")
        self.first_row = page.locator('tr').nth(1)
        self.profile_icon = page.locator("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[2]/a")
        self.profile_icon_logout = page.locator("//*[@id='bs-example-navbar-collapse-1']/ul[2]/li[2]/ul/li[5]/a")

    async def open(self):
        url = "https://demo.relbase.cl/dtes/notas-venta"
        await self.page.goto(url)

    async def click_new_nota_button(self):
        await expect(self.new_nota_button).to_be_visible()
        await self.new_nota_button.click()

    async def click_nota_venta(self):
        await expect(self.nota_venta).to_be_visible()
        await self.nota_venta.click()

    async def click_go_back_button(self):
        await expect(self.go_back_button).to_be_visible()
        await self.go_back_button.click()

    async def get_first_row_text(self):
        await expect(self.first_row).to_be_visible()
        return await self.first_row.inner_text()
    
    async def click_profile_icon(self):
        await expect(self.profile_icon).to_be_visible()
        await self.profile_icon.click()

    async def click_profile_icon_logout(self):
        await expect(self.profile_icon_logout).to_be_visible()
        await self.profile_icon_logout.click()