from time import time
from datetime import datetime, timedelta


def set_time_range(days=1):
    """
    (오늘 날짜 00시 - days에 입력한 날) ~ 오늘 날짜 00시
    :param days: start date를 계산하기 위한 n days. default 1 days
    :return: start(datetime), end(datetime)
    """
    today = datetime.now()
    end = datetime(today.year, today.month, today.day, 0, 0, 0)
    start = end - timedelta(days=days)
    return start, end


def set_date_range_list(days=1):
    today = datetime.now()
    date_list = []
    for i in range(1, days + 1):
        start = today - timedelta(days=i)
        end = today - timedelta(days=i-1)
        date_list.append((start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")))
    return date_list


def now_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def time_format(start_time: time):
    """
    time 함수로 즉정한 실행 시간을 시분초 단위로 변환해주는 기능
    :param start: 시작시간
    :return:
    """
    end = time() - start_time
    e = int(end)

    if e // 86400 > 0:
        runtime = "{:d}day {:02d}:{:02d}:{:02d}.{:03d}".format(
            e // 86400, e % 86400 // 3600, e % 3600 // 60, e % 60, (e - int(end)) * 1000)
    else:
        runtime = "{:02d}:{:02d}:{:02d}.{:03d}".format(e // 3600, e % 3600 // 60, e % 60, int((end - e) * 1000))

    return runtime
