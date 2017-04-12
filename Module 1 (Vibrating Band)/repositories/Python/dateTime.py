from time import gmtime, strftime
def dateFormat():
    #getting time and date and storing in current_time
    current_time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    #converting time into lists
    lists = current_time.split()
    date = lists[:-2]
    getDate = ' '.join(date)
    return getDate

def timeFormat():
    #getting time and date and storing in current_time
    current_time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    #converting time into lists
    lists = current_time.split()
    time = lists[-1]
    getTime = ''.join(time)
    return getTime



 