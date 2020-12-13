#!/usr/bin/env python3

import html
import urllib.request
import json
import re
import os
from pathlib import Path

# regex for retrive code tags
ONE_LINE_CODE_START_TAG = "<code>"
ONE_LINE_CODE_END_TAG = "</code>"
CODE_START_TAG = "<pre><code>"
CODE_END_TAG = "</code></pre>"
CODE_TAG_EXP = re.compile(CODE_START_TAG+'.*?'+CODE_END_TAG+'|'+ONE_LINE_CODE_START_TAG+'.*?'+ONE_LINE_CODE_END_TAG, re.DOTALL)

def createRequest(ENDPOINT, X_API_KEY, offset, limit):
    req = urllib.request.Request(f'{ENDPOINT}?offset={offset}&limit={limit}')
    req.add_header('X-API-KEY', X_API_KEY)
    return req

def callAPI(request):
    with urllib.request.urlopen(request) as res:
        body = res.read().decode('utf-8')
    return body

def getJSONData(ENDPOINT, X_API_KEY, offset, limit):
    req = createRequest(ENDPOINT, X_API_KEY, offset, limit)
    body = callAPI(req)
    return json.loads(body)

def main():
    offset = 0
    limit = 10
    while True:
        jsonFile = getJSONData(os.environ['ENDPOINT'], os.environ['X_API_KEY'], offset, limit)

        # parameters about retrived contetns
        totalCount = jsonFile['totalCount']
        offset = jsonFile['offset']
        limit = jsonFile['limit']
        contents = jsonFile['contents']
        contentsCount = len(contents)

        # parse contents and make json to md
        for content in contents:
            postTitle = content['title']
            postSlug = content['slug']
            postDate = content['date']
            postTags = list(map(lambda x:x['tag'], content['tags']))
            postBody = content['body']

            # get codes from body 
            codes = CODE_TAG_EXP.findall(postBody)
            for code in codes:
                # remove all character reference & <code> tags
                if CODE_START_TAG in code and CODE_END_TAG in code:
                    postBody = postBody.replace(code, '\n\n' + \
                        html.unescape(code[len(CODE_START_TAG):-len(CODE_END_TAG)]) + \
                            '\n\n')
                elif ONE_LINE_CODE_END_TAG in code and ONE_LINE_CODE_START_TAG in code:
                    postBody = postBody.replace(code, '\n\n' + \
                        html.unescape(code[len(ONE_LINE_CODE_START_TAG):-len(ONE_LINE_CODE_END_TAG)]) + \
                            '\n\n')

            
            # create file
            filepath = Path(os.environ['OUTPUT']+f'/{postSlug}.md')
            print(f'{filepath} ...\t', end="")

            with open(filepath, 'w') as file:
                file.write('---\n'\
                        'author: "isofurabon"\n' \
                        f'title: "{postTitle}"\n' \
                        f'date: {postDate}\n' \
                        f'tags: {postTags}\n' \
                        '---\n' \
                        f'{postBody}')
            print('COMPLETE!!')
        
        # check rest of posts that are not retrived in current session
        if offset + contentsCount >= totalCount:
            print(f'offset={offset} + contentsCount={contentsCount} >= totalCount={totalCount}')
            break

        offset += limit

if __name__ == "__main__":
    main()