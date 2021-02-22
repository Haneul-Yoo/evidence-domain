import csv
import random
import json
import os
import jsonlines

def load_jsonl(filename):
    data = []
    with jsonlines.open('./data/'+filename+'.jsonl') as reader:
        for row in reader:
            data.append(row)
    return data

def get_domain(data):
    cnt = 1
    for row in data:
        book = {
            'netloc': row['netloc'],
            'count': row['count'],
            'urls': row['urls']
        }
        with open('./data/contexts/%04d-%s-%s.json' % (cnt, book['netloc'], book['count']), 'w') as f:
            json.dump(book, f, sort_keys=True, indent=4)
        cnt += 1

def conv(filename):
    if not os.path.exists('./data/contexts'):
        os.makedirs('./data/contexts')
    get_domain(load_jsonl(filename))

def main():
    conv('evidence_domain-annot')

if __name__ == "__main__":
    main()