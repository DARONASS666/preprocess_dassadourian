# Preprocessing Text Python Package

#### Course Link: https://bit.ly/intro_nlp

This python package is prepared by Daron Assadourian.

Install

`pip install git+ssh://git@github.com/DARONASS666/preprocess_dassadourian.git`

Uninstall

`pip uninstall preprocess_dassadourian`

How to use it for preprocessing

You have to have installed spacy and python3 to make it work.

def get_clean(x):
    x = str(x).lower().replace('\\', '').replace('_', ' ')
    x = ps.cont_exp(x)
    x = ps.remove_emails(x)
    x = ps.remove_urls(x)
    x = ps.remove_html_tags(x)
    x = ps.remove_rt(x)
    x = ps.remove_accented_chars(x)
    x = ps.remove_special_chars(x)
    x = re.sub("(.)\\1{2,}", "\\1", x)
    return x
    
# Use this if you want to use one by one

import pandas as pd
import numpy as np
import preprocess_dassadourian as pp

df = pd.read_csv('imdb_reviews.txt', sep = '\t', header = None)
df.columns = ['reviews', 'sentiment']

### These are series of preprocessing
df['reviews'] = df['reviews'].apply(lambda x: pp.cont_exp(x)) #you're -> you are; i'm -> i am
df['reviews'] = df['reviews'].apply(lambda x: pp.remove_emails(x))
df['reviews'] = df['reviews'].apply(lambda x: pp.remove_html_tags(x))
df['reviews'] = df['reviews'].apply(lambda x: pp.remove_urls(x))

df['reviews'] = df['reviews'].apply(lambda x: pp.remove_special_chars(x))
df['reviews'] = df['reviews'].apply(lambda x: pp.remove_accented_chars(x))
df['reviews'] = df['reviews'].apply(lambda x: pp.make_base(x)) #ran -> run, 
df['reviews'] = df['reviews'].apply(lambda x: pp.spelling_correction(x).raw_sentences[0]) #seplling -> spelling

Note: Avoid to use make_base and spelling_correction for very large dataset otherwise it might take hours to process.

