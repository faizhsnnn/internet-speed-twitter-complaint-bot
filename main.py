from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "Gmail"
TWITTER_PASSWORD = "Gmail_Pass"

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # accept cookies if popup appears
        wait = WebDriverWait(self.driver, 20)

        # Wait for cookie button and click it using JavaScript
        try:
            accept_button = wait.until(
                EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
            )
            self.driver.execute_script("arguments[0].click();", accept_button)
        except:
            pass

        go_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.js-start-test"))
        )
        go_button.click()

        # wait for test to complete
        time.sleep(60)

        self.down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

        print(f"Download Speed: {self.down}")
        print(f"Upload Speed: {self.up}")

    def tweet(self):
        wait = WebDriverWait(self.driver, 30)

        self.driver.get("https://x.com/i/flow/login")

        # Click Google login
        google_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Google')]"))
        )
        google_button.click()

        # Switch to Google login window
        wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])

        # Enter Google email
        email = wait.until(EC.element_to_be_clickable((By.ID, "identifierId")))
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        # Wait for password field
        password = wait.until(EC.element_to_be_clickable((By.NAME, "Passwd")))
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        # Wait until login finishes and switch back
        wait.until(lambda d: len(d.window_handles) == 1)
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        tweet_box = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']"))
        )

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        tweet_box.send_keys(tweet)

        # Wait for tweet button
        tweet_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='button']//span[text()='Post']"))
        )

        tweet_button.click()
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet()