from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# Tarayıcıyı başlat 
driver = webdriver.Chrome(service=Service())

# Login sayfasına git
driver.get("https://the-internet.herokuapp.com/login")

# Yanlış kullanıcı adı ve şifre girişi
driver.find_element(By.ID, "username").send_keys("yanlis")
driver.find_element(By.ID, "password").send_keys("yanlis")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Hata mesajı görünüyor mu kontrol eder
error_element = driver.find_element(By.ID, "flash")
if "Your username is invalid!" in error_element.text:
    print("Hata mesajı göründü: Test başarılı.")
else:
    print("Hata mesajı görünmedi: Test başarısız.")

# Ekran görüntüsü al
screenshot_path = os.path.join(os.path.dirname(__file__), "..", "test-sonucu.png")
driver.save_screenshot(screenshot_path)

