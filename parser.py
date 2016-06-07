import argparse
import codecs
import os
import json
from escapewords import escape_words
from stopwords import stopwords
from stemming.porter2 import stem

inverted_index = {}

def parse_file(input_file):
    section = input_file.split('/')[-1].split('.')[-1]
    try:
        with codecs.open(input_file, 'r', 'latin-1') as ip:
            key = ip.name
            for line in ip:
                for word in line.split():
                    if word in stopwords:
                        continue
                    if word not in escape_words:
                        word = stem(word)
                    if word in inverted_index:
                        doclist = inverted_index[word]
                        if ip.name in doclist:
                            doclist[ip.name] += 1
                        else:
                            doclist[ip.name] = 1
                    else:
                        inverted_index[word] = {}
                        inverted_index[word][ip.name] = 1
    except Exception as e:
        print('Failed to open: %s due to %s' % (input_file, str(e)))


def parse_dir_tree(rootdir):
    for root, dirs, files in os.walk(rootdir):
        for f in files:
            parse_file(os.path.join(rootdir, f))
        for d in dirs:
            parse_dir_tree(os.path.join(rootdir, d))


def save_index():
    with open('iindex', 'w') as output:
        json.dump(inverted_index, output)

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-s', '--source')
    args = argparser.parse_args()
    parse_dir_tree(args.source)
    save_index()

if __name__ == '__main__':
    main()

