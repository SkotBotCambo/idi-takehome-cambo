import pandas as pd
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure
import os
import time

def get_client():
    client = MongoClient('mongodb',
                     username=os.environ['MONGO_INITDB_ROOT_USERNAME'],
                     password=os.environ['MONGO_INITDB_ROOT_PASSWORD'],
                     authMechanism='SCRAM-SHA-256')

    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        print("MongoDB server Connection Test successful")
    except ConnectionFailure:
        print("MongoDB server not available")
    
    return client

def get_tweets(term: str, tweets_col: Collection) -> pd.DataFrame:
    """queries the database for records containg a string matching `term`

    Parameters
    ----------
    term: str, required
        The term to query the database with
        
    """
    q = {"$text":
         {"$search": term},
    }

    print("retreiving...")
    start_t = time.time()
    results = list(tweets_col.find(q, {"text":1, "ts1":1, "place_id": 1, "author_id":1, "author_handle":1, "like_count":1}))
    print(f"Query took {time.time()-start_t} seconds.")

    print("counting...")
    results_df = pd.DataFrame(results).set_index('_id')
    results_df['datetime'] = pd.to_datetime(results_df['ts1'])
    results_df['like_count'] = pd.to_numeric(results_df['like_count'], downcast='integer', errors='coerce')

    return results_df

def tweet_count_per_day(term_df: pd.DataFrame) -> list:
    """
        Takes a DataFrame from get_tweets() and returns a list where each element represents
        a day in which the term was used in a tweet. Each day is represented as a dictionary
        with the following schema:
            {date: the date the term was used,
            count: the number of times it was used that day}
    """
    counts_df = term_df.groupby([term_df['datetime'].dt.date]).count()

    print("serializing...")
    data = []
    
    for ind, row in counts_df.iterrows():
        record = {'date':ind.strftime("%Y-%m-%d"),
                  'count':int(row['text'])}
        data.append(record)

    return data

def query_term(term: str, tweets_col: Collection) -> dict:
    """
        This function wraps together the previous functions to create a 
        json serializable result that can be sent back to the user.
    """
    start_t = time.time()
    term_df = get_tweets(term, tweets_col)
    time_to_query = time.time() - start_t
    # How many tweets were posted containing the term on each day?
    daily_counts = tweet_count_per_day(term_df)

    # How many unique users posted a tweet containing the term?
    author_vc = term_df['author_id'].value_counts()
    unique_users = len(author_vc)

    # How many likes did tweets containing the term get, on average?
    avg_likes_per_tweet = term_df['like_count'].mean()

    # Where (in terms of place IDs) did the tweets come from?
    place_ids = []
    if 'place_id' in term_df.columns:
        place_ids = list(term_df['place_id'].unique())

    # What times of day were the tweets posted at?
    term_df = term_df.set_index('datetime')
    morning_df = term_df.between_time('05:00:00', '12:00:00')
    afternoon_df = term_df.between_time('12:00:00','17:00:00')
    evening_df = term_df.between_time('17:00:00','23:59:59')
    overnight_df = term_df.between_time('00:00:00','05:00:00')

    times_of_day = {'morning':len(morning_df),
                    'afternoon':len(afternoon_df),
                    'evening':len(evening_df),
                    'overnight':len(overnight_df)}
    
    most_used_by = term_df['author_handle'].value_counts().index[0]

    results = {'term':term,
               'time_to_complete_query':time_to_query,
               'counts_by_day':daily_counts,
               'users':unique_users,
               'avg_likes_per_tweet':int(avg_likes_per_tweet),
               'place_ids':place_ids,
               'times_of_day':times_of_day,
               'most_used_by':most_used_by}
    return results