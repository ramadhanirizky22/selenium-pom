import os
from selenium import webdriver

def get_driver(browser="chrome", headless=False):
    is_headless = headless or os.getenv("HEADLESS", "false").lower() in ("true", "1")
    
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if is_headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument("--headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Browser tidak didukung: " + browser)
    
    if not is_headless:
        driver.maximize_window()
    return driver

