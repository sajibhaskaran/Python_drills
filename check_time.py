# Purpose: A program for finding out if given branches open or not.
#
# Author : Saji Bhaskaran


import datetime as dt


def check_branch(city, diff):
    # finding out the hour in the given city
    time_now = dt.datetime.now() + dt.timedelta(hours=diff)
    time_open = dt.datetime.replace(dt.datetime.now() + dt.timedelta(days = 1), hour = 9, minute=0, second=0)    
    time_till = dt.datetime.strptime(str(time_open - time_now), '%H:%M:%S')    
    state = ("closed", "open")[9 < time_now.hour < 21]
       
    print('{0} branch is {1} now. \nThis branch will be open in {2} hours and {3} minutes.\n'.format(
                                                    city, state, time_till.hour, time_till.minute))


    

def main():
    
    check_branch('London', 8)
    check_branch('New York City', 3)


if __name__ == "__main__":
    main()
