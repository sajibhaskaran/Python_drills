# Purpose: A program for finding out if given branches open or not.
#
# Author : Saji Bhaskaran


import datetime


def check_branch(city, diff):
    # finding out the hour in the given city
    time = datetime.datetime.now() + datetime.timedelta(hours=diff)
    print(datetime.time(9,0,0)-time)
    state = ("closed", "open")[9 < time.hour < 21]
       
    print('{0} branch is {1} now \nCurrent Time at {0}: {2}\n'.format(city, state,
                                            time.strftime("%a %b %d, %Y %H:%M:%S")))


    

def main():
    
    check_branch('London', 8)
    check_branch('New York City', 3)


if __name__ == "__main__":
    main()
