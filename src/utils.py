#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
import unidecode


def get_html_content(url, headers):
    """Gets HTML content from URL"""
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        raise requests.ConnectionError("Expected status code 200, but got {}".format(r.status_code))

    return r.content


def flatten_list(l):
    """Converts list of lists to 1D list"""
    return [item for sublist in l for item in sublist]


def clean_string(s):
    """Basic string cleaning"""

    s = re.sub('(\n){3,}', '[sep]', s)  # Marker for separation between alternative names
    s = re.sub(r"[\n\t\r]*", "", s)  # Remove \n \t \r
    s = re.sub(' +', ' ', s)  # Remove more than two consecutive whitespaces
    s = s.strip()  # Remove trailing whitespaces
    s = s.rstrip('.')  # Remove ending period
    s = re.sub(r'[\x92]', "'", s)  # Correct bad utf-8 characters

    return s


def normalize_key(k):
    """Cleans key values"""
    k = clean_string(k)  # clean string
    k = k.lower()  # lowercase
    k = k.replace(' ', '_')  # no whitespaces
    k = unidecode.unidecode(k)  # remove accents

    return k
