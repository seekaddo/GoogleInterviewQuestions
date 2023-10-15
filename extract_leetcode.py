"""
Copyright (c) Dennis Kwame Addo

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

import argparse
import json
import csv
from datetime import datetime
import os
import os.path
import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}


class LeetcodeScan:
    # Constants
    INTERV_QUESTIONS_URL = "https://leetcode.com/discuss/interview-question/?currentPage={}&orderBy=newest_to_oldest&query="
    INTERV_EXPERIENCE_URL = "https://leetcode.com/discuss/interview-experience?currentPage={}&orderBy=newest_to_oldest&query="

    SCAN_FILTER = ["google"]

    page_counter = 0

    def __init__(self):
        self.start_page = 1

    def display_urls(self):
        print(f"current scan list: {LeetcodeScan.INTERV_QUESTIONS_URL.format(self.start_page)}")

    def send_request(self, url):

        with requests.Session() as session:
            # response = session.get(url, headers=headers, timeout=50)
            logging.info(f"sending request to: {url}")
            response = session.get(url, headers=headers)

            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
                exit(11)

    def getnext_page(self):
        LeetcodeScan.page_counter += self.start_page
        pnr = LeetcodeScan.page_counter
        url = LeetcodeScan.INTERV_QUESTIONS_URL.format(pnr)

        soup = BeautifulSoup(self.send_request(url), "html.parser")
        print(soup)
        exit(11)
        page_content = soup.find_all("div", {"class": "topic-item-wrap__2FSZ"})
        return page_content


if __name__ == "__main__":
    scan = LeetcodeScan()
    print(len(scan.getnext_page()))
