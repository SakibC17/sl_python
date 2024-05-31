from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
import time
import booking.constants as const

class Booking(webdriver.Chrome):

    def __init__(self, teardown=False):
        self.teardown = teardown 
        super(Booking, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first(self):
        self.get(const.BASE_URL)

    def close_popup(self):
        try:
            x_button = self.find_element(By.CLASS_NAME, "f4552b6561")
            x_button.click()
        except:
            print("No pop-up to close.")

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, '[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        selected_currency = self.find_element(By.CLASS_NAME, "ac7953442b")
        selected_currency.click()

    def select_destination(self, place_going):
        WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.NAME, "ss"))
        )

        search_field = self.find_element(By.NAME, "ss" )
        search_field.send_keys(str(place_going))

    def select_dates(self, check_in, check_out):
        calendar_select = self.find_element(By.CSS_SELECTOR, "[data-testid='date-display-field-start']")
        calendar_select.click()
        # time.sleep(2)
        check_in_select = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_in}"]')
        check_in_select.click()
        check_out_select = self.find_element(By.CSS_SELECTOR, f'[data-date="{check_out}"]')
        check_out_select.click()

    def inc(self, adults, children, rooms):
        select_occupants = self.find_element(By.CSS_SELECTOR, '[data-testid="occupancy-config"]')
        select_occupants.click()

        inc_adults = self.find_element(locate_with(By.CLASS_NAME, "f4d78af12a").to_right_of({By.CSS_SELECTOR: '[for="group_adults"]'}))
        dec_adults = self.find_element(locate_with(By.CLASS_NAME, "e91c91fa93").to_right_of({By.CSS_SELECTOR: '[for="group_adults"]'}))
        if adults == 1:
            dec_adults.click()
        else:
            while adults > 2:
                inc_adults.click()
                adults -= 1

        inc_rooms = self.find_element(locate_with(By.CLASS_NAME, "f4d78af12a").to_right_of({By.CSS_SELECTOR: '[for="no_rooms"]'}))
        while rooms > 1:
            inc_rooms.click()
            rooms -= 1

        num_children = len(children)
        inc_children = self.find_element(locate_with(By.CLASS_NAME, "f4d78af12a").to_right_of({By.CSS_SELECTOR: '[for="group_children"]'}))
        while num_children > 0:
            inc_children.click()
            num_children -= 1
        
        child_ages = self.find_elements(By.CLASS_NAME, "c3390b1036")
        curr_child = 0
        for e in child_ages:
            e.click()
            age_select = e.find_element(By.CSS_SELECTOR, f'[data-key="{children[curr_child]}"]').click()
            curr_child += 1

        submit_button = self.find_element(By.CLASS_NAME, "c213355c26").click()
    
    def submit_query(self):
        launch_query = self.find_element(By.CLASS_NAME, "cceeb8986b").click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        # filtration.choose_sorting()
        filtration.apply_star_rating(2)


    def report_results(self):
        boxes = self.find_element(By.CLASS_NAME, "d4924c9e74")
        
        report = BookingReport(boxes, driver=self)
        report.pull_titles()

        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price"]
        )
        table.add_rows(report.pull_titles())
        print(table)



        
        