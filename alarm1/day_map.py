from datetime import date, timedelta

def allsundays(year):
    d = date(year, 1, 1)
    d += timedelta(days=6-d.weekday())
    while d.year == year:
        yield d
        d += timedelta(days=7)
