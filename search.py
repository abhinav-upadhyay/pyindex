#import json
import pickle
import sys

def main():
    with open('iindex.pickle', 'rb') as f:
        index = pickle.load(f)

    query = sys.argv[1]
    if query in index:
        doclist = index[query]
        print(doclist.keys())


if __name__ == '__main__':
    main()
