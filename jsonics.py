from ics import Calendar, Event
import json
import os, sys



def cleanDate(datetext):
    return datetext[:-6]


if __name__ == "__main__":

    general_cal = Calendar()

    jsonevents = json.load(open('sth.json','r'))

    count = 0

    for match in jsonevents:
        try:
            cal_event = Event()
            cal_event.begin = str(cleanDate(match['start']))
            cal_event.end = cleanDate(match['end'])
            cal_event.name = str(match['title'])
        except ValueError:
            count += 1
            continue

        if 'Under' in match['title']:
            count += 1
            continue

        general_cal.events.add(cal_event)

    cal_event = Event()
    cal_event.begin = '2014-01-01T10:00:00'
    cal_event.end = '2014--0101T18:00:00'
    print(cal_event)

    print("Calendar created")
    print("Skipped %i events" % count)
    with open(os.path.expanduser('adult_shcc.cal'), 'w') as f:
        f.writelines(general_cal)

    sys.exit(0)