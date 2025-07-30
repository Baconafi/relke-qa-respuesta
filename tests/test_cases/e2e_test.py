from playwright.async_api import expect
import pytest
from pages import HomePage, LoginPage, VentasPage, NotasVentasPage, NewNotasVentasPage


@pytest.mark.asyncio
async def test_nota_venta_nueva(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    ventas_page = VentasPage(page)
    notas_ventas_page = NotasVentasPage(page)
    new_nota_venta_page = NewNotasVentasPage(page)

    await login_page.open()
    await login_page.fill_email("qa_junior@relke.cl") 
    await login_page.fill_password("Demo123456!")
    await login_page.click_login_button()

    await home_page.click_ventas()

    await ventas_page.click_nota_de_venta()

    await notas_ventas_page.click_new_nota_button()
    await notas_ventas_page.click_nota_venta()

    await new_nota_venta_page.select_option_sucursal(label="Casa matriz")
    await new_nota_venta_page.select_doc_tributario("39")
    await new_nota_venta_page.select_bodega("13")
    await new_nota_venta_page.select_cliente("es")
    await new_nota_venta_page.select_moneda("pesos")
    await new_nota_venta_page.select_producto("man")
    await new_nota_venta_page.fill_cantidad("1")
    await new_nota_venta_page.click_comment()
    
    # Validar que monto neto + monto iva = monto total
    monto_neto = await new_nota_venta_page.get_monto_neto()
    monto_iva = await new_nota_venta_page.get_monto_iva()
    monto_total = await new_nota_venta_page.total_amount()

    # Convertir a float (ajusta si hay símbolos de moneda o separadores)
    monto_neto = float(monto_neto.replace('$ ', ''))
    monto_iva = float(monto_iva.replace('$ ', ''))
    monto_total = float(monto_total.replace('$ ', ''))

    assert monto_total > 0, "El monto total debe ser mayor que cero"
    assert abs((monto_neto + monto_iva) - monto_total) < 0.01, "La suma de monto neto e IVA no es igual al monto total"

    await new_nota_venta_page.click_enviar_button()

    await expect(page).to_have_url("https://demo.relbase.cl/dtes/notas-venta/67959")

    await expect(notas_ventas_page.nota_exitosa).to_contain_text("Nota de venta creada correctamente")

    await notas_ventas_page.click_go_back_button()

    await expect(notas_ventas_page.first_row).to_contain_text("Escondida")
    await expect(notas_ventas_page.first_row).to_contain_text("595")

    await page.pause()

    await notas_ventas_page.click_profile_icon()
    await notas_ventas_page.click_profile_icon_logout()

    await expect(page).to_have_url("https://demo.relbase.cl/ingresar")



