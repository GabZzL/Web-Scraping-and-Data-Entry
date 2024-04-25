from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class GoogleForms:
    # init the class with the Chrome options, driver and url
    def __init__(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = url

    # method to open the form page, then fill out the questions, it repeats the process till the end of the information
    def fill_out(self, rooms_list):
        self.driver.get(url=self.url)
        sleep(5)
        # loop in each room element
        for room in rooms_list:
            address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/'
                                                                     'div/div[2]/div/div[1]/div/div[1]/input')
            address_input.send_keys(room[1])

            price_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/'
                                                                   'div[2]/div/div[1]/div/div[1]/input')
            price_input.send_keys(room[2])

            url_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/'
                                                                 'div[2]/div/div[1]/div/div[1]/input')
            url_input.send_keys(room[0])
            sleep(1)
            send_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]'
                                                                   '/div[1]/div')
            send_button.click()
            sleep(5)
            another_answer_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]'
                                                                             '/div/div[4]/a')
            another_answer_button.click()
            sleep(5)
        # when the process is done, close the page
        self.driver.quit()
