import time 
from booking.booking import Booking

with Booking() as bot:
    bot.land_first()
    bot.close_popup()
    # bot.change_currency()
    # time.sleep(5)
    bot.select_destination('New York')
    bot.select_dates('2024-05-30', '2024-06-15')
    bot.inc(8, [2, 3, 4], 4)
    bot.submit_query()
    time.sleep(3)
    bot.close_popup()
    # bot.apply_filtrations()
    
    bot.report_results()
    time.sleep(3)




