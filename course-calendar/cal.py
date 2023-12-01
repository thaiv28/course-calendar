import api

# returns calendar, cal_id
def get_calendar(service):
    cal_dict = api.get_calendars(service)
    key_list = list(cal_dict.keys())
    
    print("Please select which calendar you would like to use:(1-"+
          str(len(key_list) + 1)+"):")
    
    for i in range(len(key_list)):
        print(str(i + 1) + ". " + key_list[i].upper())
    print("-------------------")
    print(str(len(key_list)+1) + ". Create a new calendar")
    print(str(len(key_list)+2) + ". Quit")
    
    cal_num = int(input(""))
    while(True):
        if 0 < cal_num < len(key_list) + 3:
            break
        cal_num = input("Invalid input. Please select which calendar you would like to use (1-"+
          str(len(key_list) + 1)+"):")
        
    if(cal_num == len(key_list) + 1):
        name = input("Enter calendar name:")
        calendar = {
            'summary': name,
            'timeZone': service.calendars().get(calendarId='primary').execute()['timeZone']
        }

        calendar = service.calendars().insert(body=calendar).execute()
        cal_id = calendar['id']
        
        print("Created calendar '" + calendar['summary'] + "'")
    elif(cal_num == len(key_list) + 2):
        exit()
    else:   
        cal_id = cal_dict[key_list[cal_num - 1]]
        calendar = service.calendarList().get(calendarId=cal_id).execute()
    
    return calendar, cal_id