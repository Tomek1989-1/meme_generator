"""This file creates meme based on user input."""
import sys
sys.path.insert(0, './QuoteEngine/')
import argparse
import os
from quote_engine import Ingestor
from meme_generator import memeGenerator
import random

parser = argparse.ArgumentParser()

parser.add_argument("-body", default=False)
parser.add_argument("-author", default=False)
parser.add_argument("-path", default=False)
args = parser.parse_args()


def main():
    """Make meme."""
    if not args.body:
        """Random input."""
        random_file = random.choice(os.listdir('./_data/DogQuotes'))
        random_quote = random.choice(Ingestor.parse(f'./_data/DogQuotes/'
                                                    + random_file))
        quote_body = random_quote.body
        quote_author = random_quote.author
    else:
        """User provided input."""
        quote_body = args.body
        quote_author = args.author

    if not args.path:
        meme_image = random.choice(os.listdir('./_data/photos/dog'))
    else:
        meme_image = args.path
    
    in_path = f'./_data/photos/dog/' + meme_image
    out_path = f'{random.randint(1,100000)}.jpg'
    memeGenerator(out_path).make_meme(in_path, quote_body, quote_author)

    return print(out_path)

if __name__ == "__main__":
    main()