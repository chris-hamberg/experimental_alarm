import shelve, os

class Alarm:

    def __init__(self, hour='*', minute='*', day='*', id=None):
        self._alarm_number = id
        self._hour = hour
        self._min  = minute
        self._day  = day
        self.callback_function = 'birds_loop.py'
        self.function_path = os.environ['HOME']+ \
                '/alarm/{self.callback_function}'
        self.callback_function = self.function_path.format_map(vars())
        self.save()

    def __repr__(self):
        mapping = {0: 'Sun',
                   1: 'Mon',
                   2: 'Tue',
                   3: 'Wen',
                   4: 'Thur',
                   5: 'Fri',
                   6: 'Sat',
                   7: 'Sun',
                   }
        day = mapping[self.day]
        if len(str(self.minute)) == 1:
            minute = '0' + str(self.minute)
        else:
            minute = str(self.minute)
        if self.hour > 12:
            hour = self.hour%12
        else:
            hour = self.hour
        suffix = 'am' if self.hour <= hour else 'pm'
        if hour == 0:
            hour = '00'; suffix = 'am'
        elif hour == 12:
            suffix = 'pm'
        return '{day} {hour}:{minute} {suffix}'.format_map(vars())

    @property
    def hour(self):
        return self._hour
    @hour.setter
    def hour(self, hour):
        self._hour = hour

    @property
    def minute(self):
        return self._min

    @minute.setter
    def minute(self, minute):
        self._minute = minute

    @property
    def day(self):
        return self._day
    
    @day.setter
    def day(self, day):
        self._day = day

    @property
    def id(self):
        return self._alarm_number

    def save(self):
        job = '{self._min} {self._hour} * * {self._day}'.format_map(
                vars()) + ' {self.callback_function}'.format_map(
                vars())
        job += ' #alarm{self._alarm_number}\n'.format_map(
                vars())

        index, cur_cron = self._parse()

        try:
            cur_cron[index] = job
        except TypeError:
            cur_cron.append(job)
        finally:
            self._write(cur_cron)
            #DAT[str(self._alarm_number)] = self

    def delete(self):
        index, cur_cron = self._parse()
        try:
            del cur_cron[index]
        except TypeError:
            pass
        finally:
            self._write(cur_cron)
            #del DAT[str(self._alarm_number)]
            del self

    def _parse(self):
        cur_cron = list(os.popen('crontab -l'))
        for index, line in enumerate(cur_cron):
            if '#alarm{self._alarm_number}'.format_map(vars()) in line:
                return index, cur_cron
        return 'False', cur_cron

    def _write(self, cur_cron):
        with open('temp', 'w') as fhand:
            fhand.write(''.join(cur_cron))
        os.system('crontab temp')
        os.system('rm temp')

def test():
    a1, a2, a3 = Alarm(), Alarm(), Alarm()
    a1.min = 11 
    a1.day = 1
    a1.hour = 15
    a2.min = 22
    a2.day = 2
    a2.hour = 15
    a3.min = 3
    a3.day = 3
    a3.hour = 15
    a1.update()
    a2.update()
    a3.update()
    os.system('crontab -e')
    a1.delete()
    os.system('crontab -e')
    a2.delete()
    a3.delete()
    os.system('crontab -e')

if __name__ == '__main__':
    test()
