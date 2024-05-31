from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingFiltration():
    def __init__(self, driver: WebDriver ):
        self.driver = driver
    
    def apply_star_rating(self, star):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, '[data-filters-group="class"]')
        star_child_elems = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        for e in star_child_elems:
            try:
                # if e.get_attribute("data-filters-item") == f'class:class={2}':
                #     e.click()
                e.find_element(By.NAME, "class=3").click()
                print("YES IT WORKS")
            except:
                print("no")







    def choose_sorting(self):
        open_sorts = self.driver.find_element(By.CLASS_NAME, "b94d37c0c4")
        # open_sorts.click()
        # sorts_lists = self.driver.find_elements(By.CLASS_NAME, "ac7953442b")
        # match sort_style:
        #     case 0:
        #         popularity = self.driver.find_element(By.CSS_SELECTOR, '[data-id="popularity"]').click()
        #     case 1:
        #         home_apartment = self.driver.find_element(By.CSS_SELECTOR, '[data-id="upsort_bh"]').click()
        #     case 2:
        #         home_apartment = self.driver.find_element(By.CSS_SELECTOR, '[data-id="class"]').click()
        #     case 3:
        #         home_apartment = self.driver.find_element(By.CSS_SELECTOR, '[data-id="class_asc"]').click()
        #     case 4:
        #         home_apartment = self.driver.find_element(By.CSS_SELECTOR, '[data-id="distance_from_search"]').click()
        #     case 5:
        #         home_apartment = self.driver.find_element(By.CSS_SELECTOR, '[data-id="bayesian_review_score"]').click()
        #     case _:
        #         home_apartment = self.driver.find_element(By.CSS_SELECTOR, '[data-id="popularity"]').click()
            
