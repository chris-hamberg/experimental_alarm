import shelve, sys, os
import alarm

DAT = shelve.open('alarm')
DAT.setdefault('ALARM_ID', 0)

class View:

    def __init__(self):
        self.controller = Controller()
        self.jump_table = {
                1: self.controller.create,
                2: self.controller.modify, 
                3: self.controller.view,
                4: self.controller.delete,
                5: self.controller.exit,
                    }

    def display(self):
        print('''Select Option:
1. Create a New Alarm
2. Modify an Alarm
3. View Alarms
4. Delete an Alarm
5. exit
''')

    def run(self):
        while True:
            os.system('clear')
            self.display()
            selection = int(input('>>> '))
            try:
                assert selection in {1, 2, 3, 4, 5}
            except AssertionError: 
                print('Invalid selection.')
                input('Press enter to continue.')
                pass
            else:
                self.jump_table[selection]()

class Controller:
    
    def create(self, new=True, key=None):
        while True:
            try:
                hour   = int(input('Enter the hour: '))
                minute = int(input('Enter the minute: '))
            except ValueError: pass
            else: break
        while True:
            print('Will the alarm repeat daily? [y/n]')
            try:
                opt = input('>>> ').lower()
                assert opt != 'y' and opt != 'n'
            except AssertionError:
                day = '*'
                if opt == 'n':
                    try:
                        day = int(input('Enter the day: '))
                        break
                    except ValueError: pass
        if new:
            DAT['ALARM_ID'] += 1
            key = str(DAT['ALARM_ID'])
            DAT[key] = alarm.Alarm(hour, minute, day, key)
        else:
            DAT[key].hour = hour
            DAT[key].minute = minute
            DAT[key].day = day
            DAT[key].save()

    def modify(self):
        while True:
            try:
                key = int(input('Enter the alarm id# '))
                DAT[str(key)]
            except ValueError:
                print('That is an invalid id number.')
            except KeyError:
                print('No alarm exists with that id number.')
            else:
                self.create(new=False, key=str(key))
                print('Alarm id {key} has been updated'.format_map(vars()))
            finally:
                input('Press enter to continue.')
                break

    def view(self):
        os.system('clear')
        if len(list(DAT.keys())) <= 1:
            print('There are no alarms')
        else:
            for key in list(DAT.keys()):
                if key != 'ALARM_ID':
                    print('id: {key},'.format_map(vars()), DAT[key])
        input('Press Enter to Continue... ')

    def delete(self):
        while True:
            try:
                key = input('Enter the alarm id# ')
                int(key)
                a = DAT[key]
                info = repr(a)
                a.delete()
                del DAT[key]
            except ValueError:
                print('That is not a valid id number.')
            except KeyError:
                print('No alarm exists for that id number.')
            else:
                print('Deleted alarm id {key}, {info}.'.format_map(vars()))
            finally:
                input('Press Enter to continue.')
                break

    def exit(self):
        DAT.close()
        os.system('clear')
        sys.exit(0)

if __name__ == '__main__':
    View().run()
