from playwright.async_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("//*[@id='user_email']")
        self.password_input = page.locator("//*[@id='user_password']")
        self.login_button = page.locator("//*[@id='login-form']/div[2]/div[2]/div[5]/div/input")
        self.forget_password = page.locator("//*[@id='login-form']/div[2]/div[2]/div[6]/div[1]/div/a")
        self.new_login = page.locator("//*[@id='login-form']/div[2]/div[2]/div[6]/div[2]/div/a")

    async def open(self):
        url = "https://demo.relbase.cl/ingresar"
        await self.page.goto(url)

    async def fill_email(self, email:str):
        await expect(self.email_input).to_be_visible()
        await self.email_input.fill(email)

    async def fill_password(self, password:str):
        await expect(self.password_input).to_be_visible()
        await self.password_input.fill(password)
    
    async def click_login_button(self):
        await expect(self.login_button).to_be_visible()
        await self.login_button.click()
    
    async def click_forget_password(self):
        await expect(self.forget_password).to_be_visible()
        await self.forget_password.click()

    async def click_new_login(self):
        await expect(self.new_login).to_be_visible()
        await self.new_login.click()