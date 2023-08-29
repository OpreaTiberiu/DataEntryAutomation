from time import sleep
from listing_info import get_listing_info
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv()


class FormFill:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, data):
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfuSwZSSVya4hqCqviixfpny-PAzb29LWF11RjMObBhEKiSfQ/viewform")
        sleep(2)
        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
        ).send_keys(data["address"])
        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
        ).send_keys(data["price"])
        self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
        ).send_keys(data["link"])
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//span[text()='Trimite']").click()
        sleep(3)


ic = FormFill()

for data in get_listing_info():
    ic.fill_form(data)

sleep(20)
