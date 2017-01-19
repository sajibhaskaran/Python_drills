import datetime


def check_branch(city, diff):
    today = datetime.datetime.now()
    time = today + datetime.timedelta(hours=diff)

    if 9 < time.hour < 21:
        print('{} branch is open now'.format(city))
    else:
        print('{} branch is closed now'.format(city))

    print('Current Time at {}: {}\n'.format(city, time.strftime("%a %b %d, %Y %H:%M:%S")))


def main():
    check_branch('London', 8)
    check_branch('New York City', 3)


if __name__ == "__main__":
    main()
