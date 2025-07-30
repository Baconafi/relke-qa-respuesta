from playwright.async_api import Page, expect

class NewNotasVentasPage:
    def __init__(self, page: Page):
        self.page = page
        self.sucursal = page.locator("#sales_note_branch_id")
        self.doc_tributario = page.locator("#sales_note_type_document_sii")
        self.bodega = page.locator("#sales_note_ware_house_id")
        self.cliente_dropdown = page.locator("#select2-sales_note_customer_id-container")
        self.cliente_input = page.locator("input[type=\"search\"]")
        self.cliente_opcion = page.get_by_role("treeitem", name="[79587210-8] Escondida")
        self.moneda = page.locator("#sales_note_currency")
        self.producto_dropdown = page.locator("#select2-sales_note_e_document_products_attributes_0_product_id-container")
        self.producto_input = page.locator("input[type=\"search\"]")
        self.producto_opcion = page.get_by_role("treeitem", name="[O-CM-827917] Cajon Manzanas")
        self.cantidad = page.locator("#sales_note_e_document_products_attributes_0_quantity")
        self.monto_neto = page.locator("div:nth-child(3) > .col-md-5")
        self.monto_iva = page.locator("div:nth-child(5) > .col-md-5")
        self.total = page.locator("#total")
        self.comment = page.locator("#sales_note_comment")
        self.enviar_button = page.get_by_role("button", name=" Enviar")

    async def open(self):
        url = "https://demo.relbase.cl/dtes/notas-venta/new"
        await self.page.goto(url)

    async def select_option_sucursal(self, label: str):
        await expect(self.sucursal).to_be_visible()
        await self.sucursal.select_option(label)

    async def select_doc_tributario(self, doc: str):
        await expect(self.doc_tributario).to_be_visible()
        await self.doc_tributario.select_option(doc)

    async def select_bodega(self, bodega_value: str):
        await expect(self.bodega).to_be_visible()
        await self.bodega.select_option(bodega_value)

    async def select_cliente(self, cliente_value: str):
        await expect(self.cliente_dropdown).to_be_visible()
        await self.cliente_dropdown.click() 
        await expect(self.cliente_input).to_be_visible()
        await self.cliente_input.fill(cliente_value)
        await expect(self.cliente_opcion).to_be_visible()
        await self.cliente_opcion.click()

    async def select_moneda(self, moneda_value: str):
        await expect(self.moneda).to_be_visible()
        await self.moneda.select_option(moneda_value)

    async def select_producto(self, producto_value: str):
        await expect(self.producto_dropdown).to_be_visible()
        await self.producto_dropdown.click()
        await expect(self.producto_input).to_be_visible()
        await self.producto_input.fill(producto_value)
        await expect(self.producto_opcion).to_be_visible()
        await self.producto_opcion.click()

    async def fill_cantidad(self, cantidad_value: str):
        await expect(self.cantidad).to_be_visible()
        await self.cantidad.fill(cantidad_value)

    async def click_comment(self):
        await expect(self.comment).to_be_visible()
        await self.comment.click()

    async def click_enviar_button(self):
        await expect(self.enviar_button).to_be_visible()
        await self.enviar_button.click()

    async def get_monto_neto(self):
        await expect(self.monto_neto).to_be_visible()
        return await self.monto_neto.inner_text()
    
    async def get_monto_iva(self):
        await expect(self.monto_iva).to_be_visible()
        return await self.monto_iva.inner_text()

    async def total_amount(self):
        await expect(self.total).to_be_visible()
        return await self.total.inner_text()
