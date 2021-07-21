
def nextDay(day, k):

    daysOfWeek = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    print(len(daysOfWeek))

    nextIndex = (daysOfWeek.index(day) + k) % len(daysOfWeek)

    print(daysOfWeek[nextIndex])


nextDay('sat', 23)
