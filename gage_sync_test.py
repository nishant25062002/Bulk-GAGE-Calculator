from playwright.sync_api import sync_playwright

def get_gage_motion(lat, lon, model="ITRF2020"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True to hide browser
        page = browser.new_page()
        page.goto("https://www.unavco.org/software/geodetic-utilities/plate-motion-calculator/plate-motion-calculator.html", timeout=60000)

        page.fill('input[name="latitude"]', str(lat))
        page.fill('input[name="longitude"]', str(lon))
        page.select_option('select[name="model"]', label=model)
        page.click('input[value="Calculate"]')

        page.wait_for_selector('table.tableOutput', timeout=10000)
        result = page.inner_text('table.tableOutput')
        browser.close()
        return result

# Example usage
if __name__ == "__main__":
    lat = 26.963219
    lon = 80.340050
    print("📍 Querying GAGE...")
    output = get_gage_motion(lat, lon)
    print("✅ GAGE Result:\n", output)
