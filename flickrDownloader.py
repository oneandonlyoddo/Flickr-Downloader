'''
To do:
timer to get around rate limiting
change variable names
write readme
make a requirements.txt
push to github
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flickrapi import FlickrAPI
import requests
import os
import sys
import time

def get_urls(image_tag,max_amount, key, secret):
    flickr = FlickrAPI(key, secret)
    images = flickr.walk(text=image_tag, tag_mode='all', tags=image_tag, extras='url_o', per_page=50, sort='relevance')
    count = 0
    urls = []
    for image in images:
        if count < max_amount:
            count = count + 1
            print("Fetching url for image number {}".format(count))
            try:
                url = image.get('url_o')
                if url is not None:
                    urls.append(url)
                else:
                    print("Url for image number {} returned None".format(count))
            except:
                print("Url for image number {} could not be fetched".format(count))
        else:
            print("Done fetching urls, fetched {} urls out of {}".format(len(urls), max_amount))
            break
    return urls

def download_images(urls, output_folder):
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    print("Starting download of {} files".format(len(urls)))
    for idx, url in enumerate(urls):
        try:
            path_to_write = os.path.join(output_folder, url.split("/")[-1])
            if not os.path.exists(path_to_write):
                response = requests.get(url, stream = True)
                outfile = open(path_to_write, 'wb')
                outfile.write(response.content)
                outfile.close()
                print("Done downloading {} of {}".format(idx, len(urls)))
                time.sleep(5.0) # waiting for 5 seconds to avoid being limited or temporarily blocked
            else:
                print("Skipped {} because it already exists".format(idx, len(urls)))
        except:
            print("Failed to download url number {}".format(idx))
    print("Done.") 

def get_keys_from_file(path):
    f = open(path, "r")
    lines = f.readlines()
    key = lines[0].strip()
    secret = lines[1].strip()
    return key, secret

def main():
    tag = sys.argv[1]
    max_amount = int(sys.argv[2])
    out = sys.argv[3]
    key, secret = get_keys_from_file("./keys.txt")
    urls = get_urls(tag,max_amount, key, secret)
    download_images(urls, out)

if __name__=='__main__':
    main()    