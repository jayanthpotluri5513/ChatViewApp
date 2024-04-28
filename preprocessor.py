import re
import pandas as pd


def preprocess(data):
    df = re.sub(r'(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2})\s[apmAPM]+', r'\1', data)
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages = re.split(pattern, df)[1:]
    dates = re.findall(pattern, df)
    chat = pd.DataFrame({'user_message': messages, 'message_date': dates})
    chat['message_date'] = pd.to_datetime(chat['message_date'], format='%d/%m/%y, %H:%M - ')
    chat.rename(columns={'message_date': 'date'}, inplace=True)
    users = []
    messages = []
    for message in chat['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    chat['user'] = users
    chat['message'] = messages
    chat.drop(columns=['user_message'], inplace=True)
    chat['only_date']=chat['date'].dt.date
    chat['year'] = chat['date'].dt.year
    chat['month_num']=chat['date'].dt.month
    chat['month'] = chat['date'].dt.month_name()
    chat['day'] = chat['date'].dt.day
    chat['day_name']= chat['date'].dt.day_name()
    chat['hour'] = chat['date'].dt.hour
    chat['minute'] = chat['date'].dt.minute

    period= []
    for hour in chat[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour== 0:
            period.append(str('00') + "-" + str(hour+1))
        else:
            period.append(str(hour) + "-" + str(hour+1))
    chat['period'] = period

    return chat
