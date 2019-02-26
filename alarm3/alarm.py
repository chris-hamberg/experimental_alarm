from datetime import datetime
import bird_loop, pygame, time, os

def alarm():

    user_alarm_time = (8, 10, 0)

    while True:
    
        info = datetime.ctime(datetime.utcnow()).split()
        hour, minute = int(info[3].split(':')[0])-4, int(info[3].split(':')[1])
        seconds = int(info[3].split(':')[2])
    
        if (hour, minute, seconds) > user_alarm_time and info[0] == 'Sun':
            bird_loop.main()
            time.sleep(1)
            break
        else:
            os.system('clear')
            print('Alarm scheduled for: {}:{}'.format(
                user_alarm_time[0], user_alarm_time[1]))
            hdif = (user_alarm_time[0]-hour)%12
            mdif = (user_alarm_time[1]-minute-1)%60
            sdif = (user_alarm_time[2]-seconds)%60
            print(
                'In {hdif} hours, {mdif} minutes, and {sdif} seconds.'.format_map(
                vars()))
        time.sleep(1)

if __name__ == '__main__':
    alarm()
