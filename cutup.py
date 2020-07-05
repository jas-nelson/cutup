import nltk.tokenize as nt
import requests
import bs4
import argparse
import sys
import re
import random


def extract_text_from_webaddress(link: str):
    request = requests.get(link)
    soup = bs4.BeautifulSoup(request.content, "html.parser")
    ss = nt.sent_tokenize(soup.text)
    return ss


def clean_text(text):
    lol = [re.findall(r'\w+', tok) for tok in text]
    return [item for sublist in lol for item in sublist]


def select_words_for_cutup(text: list, selection_count=5):
    return random.choices(text, k=selection_count)

def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="Link to website to extract text.", required=True)
    parser.add_argument("-c", help="Count of words to return", required=True)
    parser.add_argument("-o", help="(Optional) File path to save cutup.")
    return parser.parse_args(args)


def write_to_file(array: list, filename: str):
    with open(filename, mode="w+", encoding='utf-8', newline='') as file:
        file.writelines(' '.join(array))


if __name__ == "__main__":
    arguments = parse_arguments(sys.argv[1:])
    text = extract_text_from_webaddress(arguments.l)
    cleanText = clean_text(text)
    cutup = select_words_for_cutup(cleanText, int(arguments.c))
    if arguments.o is not None:
        write_to_file(cutup, arguments.o)
    else:
        print(cutup)
