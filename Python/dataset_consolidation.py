import os
import json
import pandas as pd

# A script to consolidate the dataset found here: https://figshare.com/articles/dataset/PHEME_rumour_scheme_dataset_journalism_use_case/2068650/2?file=4988998
# into one .csv file for use in mango-tango-cli - https://github.com/civictechdc/mango-tango-cli

dataset_tweets_parent_path = "phemerumourschemedataset/pheme-rumour-scheme-dataset/threads/en"

#print(os.listdir(dataset_tweets_parent_path))

undesireable_folder_names = ["images", "urls-content"]
undesireable_file_names = ["annotation.json", "images.dat", "retweets.json", "structure.json", "urls.dat", "who-follows-whom.dat"]

def scandir_and_get_tweet_json_files(dir):
    dirpath, filepath = [], []
    for file_or_directory in os.scandir(dir):
        if file_or_directory.is_dir() and file_or_directory.name not in undesireable_folder_names:
            dirpath.append(file_or_directory.path)
        if file_or_directory.is_file() and file_or_directory.name not in undesireable_file_names:
            filepath.append(file_or_directory.path)

    for directory in list(dirpath):
        dp, fp = scandir_and_get_tweet_json_files(directory)
        dirpath.extend(dp)
        filepath.extend(fp)
    return dirpath, filepath


subdir, subfiles = scandir_and_get_tweet_json_files(dataset_tweets_parent_path)

#print(subfiles)
relevant_json_data_list_of_dicts = []
for file in subfiles:
    

    with open(file, 'r') as tweet:
        #relevant_json_data_dict = {}
        contents = json.load(tweet)
        #print("text:", contents["text"], "ID:", contents["id"], "Retweet Count:", contents["retweet_count"], "Created at:", contents["created_at"])

        #print("\n \n \n")
        #print("User info:", contents["user"])

        user_info_from_tweet = dict(contents["user"])

        #print(user_info_from_tweet["followers_count"])
        relevant_json_data_dict = {"text" : contents["text"], "tweet_id" : contents["id"], "retweet_count" : contents["retweet_count"], "timestamp" : contents["created_at"],
                                "follower_count" : user_info_from_tweet["followers_count"], "verified" : user_info_from_tweet["verified"], "screen_name" : user_info_from_tweet["screen_name"],
                                    "account_created_date" : user_info_from_tweet["created_at"]}
        
        #print(relevant_json_data_dict)
        relevant_json_data_list_of_dicts.append(relevant_json_data_dict)

#print(relevant_json_data_list_of_dicts)
relevant_data_dataframe = pd.DataFrame(relevant_json_data_list_of_dicts)

relevant_data_dataframe.to_csv("phemrumour.csv")