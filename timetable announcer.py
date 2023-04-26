import datetime
import time
import os
from gtts import gTTS

# Define the timetable dictionary
timetable = {
    "Wednesday": {
        "03:00-8:40": {
            "FORM 4 GEOGRAPHY": ["MR. Mulati in form 4", "MR. Muchiri in form 2"],
            "FORM 3 HISTORY": ["MRS. MUGAMBI in form 3"],
            "BREAK": [],
        # ... other classes and teachers
        },
        "9:00-9:40": {  # add new time slot
        "FORM 2 CHEMISTRY": ["MR. WEKESA"],
        "FORM 1 ENGLISH": ["MRS. OUMA"],
        # ... other classes and teachers
        },
    # ... other time slots for Wednesday
    },
    "Thursday": {
        "8:00-8:40": {
            "FORM 2 BIOLOGY": ["MR. DANIEL"],
            "FORM 1 PHYSICS": ["MRS. KIPTANUI"],
            "BREAK": [],
            # ... other classes and teachers
        },
        # ... other time slots for Thursday
    },
    # ... other weeks' timetable
}

current_day = datetime.datetime.now().strftime("%A")  # get the current day's name

# Check if the day name is valid
if current_day not in timetable:
    print("Invalid day name!")
else:
    while True:  # repeat forever
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        print("Current day:", current_day)
        print("Current time:", current_time)
        # Loop through the timetable to find the matching class
        is_class_scheduled = False
        for time_range, classes in timetable[current_day].items():
            start_time, end_time = time_range.split("-")
            if start_time <= current_time <= end_time:
                teachers = ", ".join([str(teacher) for teacher in classes.values()])
                message = f"On {current_day}, you have {', '.join(classes.keys())} with {teachers} from {time_range}."
                tts = gTTS(message)
                tts.save('message.mp3')
                os.system('mpg321 message.mp3')
                os.remove('message.mp3')
                is_class_scheduled = True
                break
        if not is_class_scheduled:
            print("No class currently scheduled.")
        time.sleep(30)  # wait for 30 seconds
