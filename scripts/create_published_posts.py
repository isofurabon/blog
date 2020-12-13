#!/usr/bin/env python3

from get_posts import getPublishedPosts
from convert_posts import convertToMarkdown
import os
from pathlib import Path

OUTPUT_PARENT_DIR = Path(os.environ['OUTPUT'])
OUTPUT_PARENT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    offset = 0
    limit = 10
    while True:
        body = getPublishedPosts(os.environ['ENDPOINT'], os.environ['X_API_KEY'], offset, limit)

        # parameters about getd contetns
        totalCount = body['totalCount']
        offset = body['offset']
        limit = body['limit']
        contents = body['contents']
        contentsCount = len(contents)

        # parse contents and make json to md
        for content in contents:
            
            # create file
            filepath = OUTPUT_PARENT_DIR / f'{content["slug"]}.md'
            print(f'{filepath} ...\t', end="")
            with open(filepath, 'w') as file:
                file.write(convertToMarkdown(content))
            print('COMPLETE!!')
        
        # check rest of posts that are not getd in current session
        if offset + contentsCount >= totalCount:
            print(f'offset={offset} + contentsCount={contentsCount} >= totalCount={totalCount}')
            break

        offset += limit

if __name__ == "__main__":
    main()