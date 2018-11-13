import requests
import misc
import json
import os
import hashlib


token  = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
blockchain_dir = os.curdir + '/blockchain/'
global last_update_id
last_update_id = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_hash(filename):

    file = open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()



def check_integrity():
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']

        prev_file = str(file - 1)

        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'OK'
        else:
            res = 'Corrupted'
        print('block {} is: {}'.format(prev_file, res))




def write_block():
    hash = ''
    data = get_updates()

    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    last_files = files[-1]
    filename = str(last_files + 1)

    current_update_id = data['result'][-1]['update_id']

    global last_update_id
    if last_update_id != current_update_id:

        last_update_id = current_update_id

        hash = get_hash(str(last_files))
        message = data['result'][-1]['message']['text']
        block = {'message': message, 'hash': hash}


        with open(blockchain_dir + filename, 'w') as file:
            json.dump(block, file, indent = 4, ensure_ascii = False)

        check = check_integrity()
        return check
    return None






def main():

    while True:
        block = write_block()
        if block != None:
            write_block()
        else:
            continue





if __name__ == '__main__':
    main()
