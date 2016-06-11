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
ignore_list = set(['c++', 'md5', 'sha1', 'sha2', 'sha256', 'sha512'])

def remove_special_chars(word):
    if word in ignore_list:
        return word

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
    w = w.replace('#', '')
    w = w.replace('(', '')
    w = w.replace(')', '')
    w = w.replace(',', ' ')
    w = w.replace(';', ' ')
    w = w.replace('"', '')
    w = w.replace('`', '')
    w = w.replace('1', '')
    w = w.replace('2', '')
    w = w.replace('3', '')
    w = w.replace('4', '')
    w = w.replace('5', '')
    w = w.replace('6', '')
    w = w.replace('7', '')
    w = w.replace('8', '')
    w = w.replace('9', '')
    w = w.replace('0', '')
    w = w.replace('?', '')
    if '.' in w:
        if w[-1] == '.':
            w = w.replace('.', '')
        else:
            w = w.replace('.', ' ')

    if "'" in w:
        if w[-2] == "'" and w[-1] == 's':
            w = w[:-2]
        w = w.replace("'", '')
    return w

def parse_file(input_file, output=False, stem=True, filter_stopwords=False):
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
                        if filter_stopwords and word in stopwords:
                            continue
                        if stem and w in stems.stems:
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


def parse_dir_tree(rootdir, output=False, stem=True, filter_stopwords=False):
    for root, dirs, files in os.walk(rootdir):
        for f in files:
            parse_file(os.path.join(rootdir, f), output=output,
                    stem=stem, filter_stopwords=filter_stopwords)
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
    argparser.add_argument('--no-stem', dest="no_stem", default=False)
    argparser.add_argument('--filter-stopwords', dest='stop_words', default=False)
    args = argparser.parse_args()
    if args.file:
        parse_file(args.file, output=args.output, filter_stopwords=args.stop_words, stem=not(args.no_stem))
    else:
        parse_dir_tree(args.source, output=args.output, filter_stopwords=args.stop_words, stem=not(args.no_stem))
    save_index()

if __name__ == '__main__':
    main()

