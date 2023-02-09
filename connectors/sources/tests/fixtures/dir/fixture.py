#
# Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
# or more contributor license agreements. Licensed under the Elastic License 2.0;
# you may not use this file except in compliance with the Elastic License 2.0.
#
import os
import random
import shutil
import string
import urllib.request
import zipfile

SYSTEM_DIR = os.path.join(os.path.dirname(__file__), "data")


def load():
    if os.path.exists(SYSTEM_DIR):
        teardown()
    print(f"Working in {SYSTEM_DIR}")
    os.makedirs(SYSTEM_DIR)
    repo_zip = os.path.join(SYSTEM_DIR, "repo.zip")

    # lazy tree generator: we download the elasticsearch repo and unzip it
    print(f"Downloading some source this may take a while...")
    urllib.request.urlretrieve(
        "https://github.com/elastic/elasticsearch/zipball/main", repo_zip
    )

    print(f"Unzipping the tree")
    with zipfile.ZipFile(repo_zip) as zip_ref:
        zip_ref.extractall(SYSTEM_DIR)

    os.unlink(repo_zip)


def remove():
    # removing 10 files
    files = []
    for root, dirnames, filenames in os.walk(SYSTEM_DIR):
        for filename in filenames:
            files.append(os.path.join(root, filename))

    random.shuffle(files)
    for i in range(10):
        print(f"deleting {files[i]}")
        os.unlink(files[i])


def teardown():
    shutil.rmtree(SYSTEM_DIR)
