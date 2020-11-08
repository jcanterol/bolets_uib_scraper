#!/usr/bin/env python
# -*- coding: utf-8 -*-

# External imports
import os
import re
import pandas as pd
from bs4 import BeautifulSoup

# Internal imports
import utils
import process

_BASEPATH = 'http://bolets.uib.es/cas/'
_SUBPATH_FAMILY = 'familia'
_SUBPATH_GENRE = 'genere'
_SUBPATH_MUSHROOM = 'bolet'

_HEADERS = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}


def get_group_ids(url):
    """General function to get all group identifiers"""
    # Get url content
    page = utils.get_html_content(url, _HEADERS) 
    soup = BeautifulSoup(page, 'html.parser')

    # Find categories section
    div = soup.find('div', id='contenido_2')
    ul = div.find('ul')

    # Find all a tags
    a_s = ul.find_all('a', href=True)
    
    # List all identifiers
    ids = [re.findall(r'[^\/]+(?=\.[^\/.]*$)', a['href'])[0] for a in a_s]

    return ids


def get_families():
    """Gets all families identifiers"""
    url = os.path.join(_BASEPATH, _SUBPATH_FAMILY, 'index.html')
    families_ids = get_group_ids(url)
    
    return families_ids


def get_genres_per_family(family_id):
    """Gets all genres identifiers per family"""
    url = os.path.join(_BASEPATH, _SUBPATH_FAMILY,'{}.html'.format(family_id))
    genres_ids = get_group_ids(url)

    return genres_ids


def get_mushrooms_per_genre(genre_id):
    """Get all mushrooms identifiers per genre"""
    url = os.path.join(_BASEPATH, _SUBPATH_GENRE,'{}.html'.format(genre_id))
    genres_ids = get_group_ids(url)

    return genres_ids


def get_all_mushrooms_ids():
    """Gets all mushrooms identifiers"""
    mushrooms_ids = []

    for f in get_families():
        for g in get_genres_per_family(f):
            mushrooms_ids.append(get_mushrooms_per_genre(g))
    
    mushrooms_ids = utils.flatten_list(mushrooms_ids)

    return mushrooms_ids


def get_mushroom_info(mushroom_id):
    """Retrieves the details for a mushroom"""

    dict_mushroom = {}
    url = os.path.join(_BASEPATH, _SUBPATH_MUSHROOM, '{}.html'.format(mushroom_id))

    # Get url content
    page = utils.get_html_content(url, _HEADERS)
    soup = BeautifulSoup(page, 'html.parser')

    # Find details section
    div = soup.find('div', id='contenido_2')

    # Find scientific name
    scientific_name = div.find('h3').get_text()
    dict_mushroom['scientific_name'] = utils.clean_string(scientific_name)
    
    # Find family and genre
    h4s = div.find_all('h4')
    family = h4s[0].get_text().split(':')[1]
    genre = h4s[1].get_text().split(':')[1]

    dict_mushroom['family'] = utils.clean_string(family)
    dict_mushroom['genre'] = utils.clean_string(genre)

    # Find other details
    ul = div.find('ul', class_='ficha')
    ps = ul.find_all('p')

    for idx_p, p in enumerate(ps):
        
        key, value = p.get_text().split(':', 1)
        key = utils.normalize_key(key)
        value = utils.clean_string(value)

        if key == '':
            if idx_p == 0:
                key = "alternative_scientific_names"
            else:
                continue

        dict_mushroom[key] = value

    return dict_mushroom


def main():
    """Main function"""

    print('Scrapping website {}...'.format(_BASEPATH))

    print('Getting all mushrooms ids...')
    mushrooms_ids = get_all_mushrooms_ids()
    mushrooms_info = []

    print('Getting all mushrooms info...')
    for m in mushrooms_ids:
        try:
            mushroom_info = get_mushroom_info(m)
            mushrooms_info.append(mushroom_info)
        except:
            continue

    print('Extracting data to CSV...')
    df_mushrooms = pd.DataFrame(mushrooms_info)
    df_mushrooms = process.process_mushroom_df(df_mushrooms)
    df_mushrooms.to_csv('mushrooms.csv', index=False)
    print('Done!')


main()
