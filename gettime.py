import datetime


def get_now_time():
    now = datetime.datetime.now()
    result = (
        str(now.year)
        + "/"
        + str(now.month)
        + "/"
        + str(now.day)
        + "/"
        + str(now.hour)
        + "/"
        + str(now.minute)
    )
    return result
