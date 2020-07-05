import nltk.tokenize as nt
import nltk
from beautifulscraper import BeautifulScraper
import argparse, sys, re, random

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


# text = "Being more Pythonic is good for health."
# ss = nt.sent_tokenize(text)
# tokenized_sent = [nt.word_tokenize(sent) for sent in ss]
# pos_sentence = [nltk.pos_tag(sent) for sent in tokenized_sent]
# pos_sentence




def extract_text_from_webaddress(link: str):
    scraper = BeautifulScraper()
    body = scraper.go(link)
    ss = nt.sent_tokenize(body.text)
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
    # arguments = {}
    # arguments["l"] = "https://stackoverflow.com/questions/23380171/using-beautifulsoup-to-extract-text-without-tags"
    # arguments["c"] = 10
    # arguments["o"] = "ouput_cutup.txt"
    text = extract_text_from_webaddress(arguments.l)
    # text = extract_text_from_webaddress(arguments["l"])
    cleanText = clean_text(text)
    cutup = select_words_for_cutup(cleanText, int(arguments.c))
    # cutup = select_words_for_cutup(cleanText, int(arguments["c"]))
    if arguments.o is not None:
        write_to_file(cutup, arguments.o)
    else:
        print(cutup)

    # if arguments["o"] is not None:
    #     write_to_file(cutup, arguments["o"])
    # else:
    #     print(cutup)
