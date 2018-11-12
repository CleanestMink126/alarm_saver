import datetime
import time

def parse_times(times):
    '''
    times --> list of (Day of Week, Hour, Minute)
    We convert everthing to weekly system composed of minutes
    '''
    total_minutes=  7 * 24 * 60
    current = datetime.datetime.now()
    day = current.weekday()
    current_time = day * 24 * 60 + current.hour * 60 + current.minute
    list_times = []

    for day,hour,minute in times:
        list_times.append(day * 24 * 60 + hour * 60 + minute)
    index = 1
    num_times = len(list_times)

    while index < num_times:
        if current_time > list_times[index-1] and current_time < list_times[index]:
            break
        index += 1
    if index == num_times:
        index = 0

    while True:
        wait_alarm(current_time[index])
        index = (index + 1)%num_times


def wait_alarm(time):
    while True:
        current = datetime.datetime.now()
        day = current.weekday()
        current_time = day * 24 * 60 + current.hour * 60 + current.minute
        if current_time == time:
            start_noise()
            break
        time.sleep(5)

def start_noise():
    pass

def check_switch():
    return True
