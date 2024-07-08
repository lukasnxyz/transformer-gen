import os
import requests

data_dir = 'data'

# make data dir
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# get shakespeare data
input_file_path = os.path.join(data_dir, 'input.txt')
if not os.path.exists(input_file_path):
    data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
    with open(input_file_path, 'w', encoding='utf-8') as f:
        f.write(requests.get(data_url).text)