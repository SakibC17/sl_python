from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class BookingReport:
    def __init__(self, boxes_section_element:WebElement, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
        # self.titles = self.pull_titles()


    def pull_deal_boxes(self):
        list_boxes = self.driver.find_elements(By.CLASS_NAME, "c6710787a4")
        # print(list_boxes, len(list_boxes))
        return list_boxes
            
    def pull_titles(self):  
        collection =[]
        for deal_box in self.deal_boxes: 
            elem = deal_box.find_element(By.CSS_SELECTOR, "[data-testid='title']")
            title = elem.get_attribute("innerHTML")
            # print(elem, title)
            elem_2 = deal_box.find_element(By.CSS_SELECTOR, "[data-testid='price-and-discounted-price']")
            title_2 = elem_2.get_attribute("innerHTML")
            title_2 = title_2.replace('&nbsp;', ' ')
            # print(elem_2, title_2)

            
            collection.append([title, title_2])
        
        # print(collection)
        return collection