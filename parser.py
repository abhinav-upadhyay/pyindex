import argparse
import codecs
import pickle
import os
import sys
from escapewords import escape_words
from stopwords import stopwords
import stems
#from stemming.porter2 import stem

inverted_index = {}

def remove_special_chars(word):
    if '%' in word:
        return None
    if '^' in word:
        return None
    if '&' in word:
        return None
    if '*' in word:
        return None
    if '[' in word or ']' in word:
        return None
    if '\\' in word:
        return None
    if '/' in word:
        return None
    if '|' in word:
        return None
    if '<' in word or '>' in word:
        return None
    if '~' in word:
        return None
    if '@' in word:
        return None
    if '=' in word:
        return None
    if '+' in word:
        return None
    if ':' in word:
        return None
    if '$' in word:
        return None


    w = word.replace('-', ' ')
    w = w.replace('!', '')
    w = w.replace('.', '')
    w = w.replace('#', '')
    w = w.replace('(', '')
    w = w.replace(')', '')
    w = w.replace(',', ' ')
    w = w.replace(';', ' ')
    w = w.replace('"', '')
    w = w.replace("'", "")
    w = w.replace('`', '')
    return w

def parse_file(input_file, output=False):
    try:
        with codecs.open(input_file, 'r', 'latin-1') as ip:
            file_name_parts = ip.name.split('/')[-1].split('.')
            file_name = file_name_parts[0] + '(' + file_name_parts[1] + ')'
            for line in ip:
                sys.stdout.write('\n')
                for word in line.split():
                    word = word.lower()
                    replacements = remove_special_chars(word)
                    if replacements is None:
                        continue
                    for w in replacements.split():
                        if word in stopwords:
                            continue
                        if w in stems.stems:
                            w = stems.stems.get(w)
                        if output:
                            sys.stdout.write('%s ' % w)
                        if w in inverted_index:
                            doclist = inverted_index[w]
                            if file_name in doclist:
                                doclist[file_name] += 1
                            else:
                                doclist[file_name] = 1
                        else:
                            inverted_index[w] = {}
                        inverted_index[w][file_name] = 1
    except Exception as e:
        sys.stderr.write('Failed to open: %s due to %s\n' % (input_file, str(e)))


def parse_dir_tree(rootdir, output=False):
    for root, dirs, files in os.walk(rootdir):
        for f in files:
            parse_file(os.path.join(rootdir, f), output=output)
        for d in dirs:
            parse_dir_tree(os.path.join(rootdir, d))


def save_index():
    with open('iindex', 'wb') as output:
        pickle.dump(inverted_index, output)

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-s', '--source')
    argparser.add_argument('-o', '--output', type=bool, default=False)
    argparser.add_argument('-f', '--file')
    args = argparser.parse_args()
    if args.file:
        parse_file(args.file, output=args.output)
    else:
        parse_dir_tree(args.source, output=args.output)
    save_index()

if __name__ == '__main__':
    main()

