from datetime import datetime


class timedata():

# change time to str
    def getCurrentTime():
        format = "%a %b %d %H:%M:%S %Y"
        return datetime.now().strftime(format)


# Get time diff
    def timeDiff(starttime, endtime):
        format = "%a %b %d %H:%M:%S %Y"
        return datetime.strptime(endtime, format) - datetime.strptime(starttime, format)