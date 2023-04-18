import datetime

current_date_time = datetime.datetime.now()
game_current_time = current_date_time.time()
print(str(game_current_time)[0:7])