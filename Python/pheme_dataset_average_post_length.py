import pandas as pd

path = "phemrumour.csv"

df = pd.read_csv(path)

# print(df.head())
text_list = list(df["text"])

message_count = 0
total_text_length = 0

for text in text_list:
    text_word_list = text.split()
    total_text_length = total_text_length + len(text_word_list)
    message_count = message_count + 1

average_text_length =  round(total_text_length / message_count)
print("The average text length is:", average_text_length)

print("The longest text is:", len(max(text_list, key = len).split()))
