import gzip
import json
import os
import pandas as pd
import re
import sqlite3

# NewsEdits db files have been released here: https://drive.google.com/drive/folders/14Y8NM-A21lXEdD1Fn0JKFUnzcFoSzhe5
# Download newssniffer-bbc-db.gz, newssniffer-nytimes-db.gz, newssniffer-guardian-db.gz, newssniffer-independent-db.gz, newssniffer-washpo-db.gz
# Unzip these 5 files and save them to a new directory "newsedits_databases"

# Download the HREN data from here: https://zenodo.org/record/6578378#.YuwILHbMK3A
hren_file = 'dataset/hren/hren_valid.json.gz'
with gzip.open(hren_file, 'rb') as zipfile:
    hren_data = json.load(zipfile)

for hren_ex in hren_data:
    (db_source, article_id, old_headline_version, new_headline_version, old_body_version, new_body_version, _) = re.findall('(\S+)_(\d+):(\d+)-(\d+)-(\d+)-(\d+):(\d+)', hren_ex['id'])[0]
    newsedits_db_file = os.path.join('newsedits_databases', db_source.replace('-db', '.db'))
    conn = sqlite3.connect(newsedits_db_file)
    
    version_cache = dict()
    version_cache[old_headline_version] = None
    version_cache[new_headline_version] = None
    version_cache[old_body_version] = None
    version_cache[new_body_version] = None
    
    for version_number in version_cache.keys():
        res = pd.read_sql_query("SELECT * from entryversion WHERE entry_id={} AND version={}".format(article_id, version_number), conn)
        for row in res.iterrows():
            version_cache[version_number] = row[-1]

    element_version_rows = {
        'old_headline': version_cache[old_headline_version],
        'new_headline': version_cache[new_headline_version],
        'old_body': version_cache[old_body_version],
        'new_body': version_cache[new_body_version]
    }

    for element, element_row in element_version_rows.items():
        print('Version: {}'.format(element_row.version))
        print('Headline:\n{}\n'.format(element_row.title))
        print('Body:\n{}\n'.format(element_row.summary))
        print('URL: {}'.format(element_row.archive_url))
        print('----------------------------')