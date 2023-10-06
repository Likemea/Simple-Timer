import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Timer is up!")

if __name__ == "__main__":
    minutes = int(input("Enter the number of minutes: "))
    seconds = minutes * 60
    countdown(seconds)