#!/usr/bin/env python

import os
import yaml
import tablib

ORIGINAL_URL = "http://blog.copyninja.info"
NEW_URL = "http://copyninja.info"

URL_MAPPING_FILE = "Permalinks.csv"
CONFIG_FILE = "_config.yml"

PERMALINK_MAPPING = []

def parse_yaml_front_matter(filename):
    lines = open(filename).read().split('\n')
    
    yaml_content = '\n'.join(lines[1:lines[1:].index('---')])
    parsed_yaml = yaml.load(yaml_content)
    
    if parsed_yaml.has_key('meta'):
        if parsed_yaml['meta'].has_key('blogger_permalink'):
            return parsed_yaml['meta']['blogger_permalink']

def generate_map(blogger_permalink,filename):
    splits = filename.split('-')
    new_permalink = '/'.join(splits[0:2])+'/'+'-'.join(splits[3:])
    blog_url = ORIGINAL_URL + '/' + blogger_permalink
    new_url = os.path.join(NEW_URL,new_permalink)
    PERMALINK_MAPPING.append((blog_url,new_url))

def parse_directory(directory):
    print directory
    for dirpath,dirnames, filenames in os.walk(directory):
        for filename in filenames:
            blogger_permalink = parse_yaml_front_matter(os.path.join(dirpath,filename))
            if blogger_permalink:
                generate_map(blogger_permalink,filename)
            


def main():
    parse_directory("_posts")
    data = tablib.Dataset()
    for i in PERMALINK_MAPPING:
        data.append(i)

    open(URL_MAPPING_FILE,'w').write(data.csv)

if __name__ == "__main__":
    main()
            
