#import datetime module
import datetime

#variable to hold current time
current_time = datetime.datetime.now()

#month, day, year numeric 
print(current_time.strftime("%m/%d/%y"))


#month, day year alpha month, day, year
print(current_time.strftime("%B %d, %Y"))


#current time 
print(current_time.strftime("%I:%M"))
