from urlextract import URLExtract

extract = URLExtract()
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import nltk
nltk.download('punkt')
import string
import emoji
import re
def fetch_stats(selected_user, df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))
    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x = df['user'].value_counts()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x, df


def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc


def most_common_words(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        tokens = nltk.word_tokenize(message.lower())
        for word in tokens:
            word = word.strip()
            word = re.sub(r"'", "", word)
            if word not in stop_words and word not in string.punctuation:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    most_common_df = most_common_df.rename(columns={0: "common words", 1: "frequency"})
    return most_common_df


def emoji_helper(selected_user, df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    new_list= []
    emoji_symbols = []
    for message in df['message']:
        emojis = emoji.distinct_emoji_list(message)
        emoji_symbols.extend([emoji.emojize(is_emoji) for is_emoji in emojis])

    emoji_df = pd.DataFrame(Counter(emoji_symbols).most_common(len(Counter(emoji_symbols))))

    return emoji_df
def monthly_timeline(selected_user,df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]
    timeline =df.groupby(['year','month_num','month']).count()['message'].reset_index()

    time= []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time']=time

    return timeline

def daily_timeline(selected_user,df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline


def week_activity(selected_user,df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'group':
        df = df[df['user'] == selected_user]

    activity_heatmap_df= df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return activity_heatmap_df




