from get_posts import getPublishedPosts, getDraftPost
import html
import re
import os

ONE_LINE_CODE_START_TAG = "<code>"
ONE_LINE_CODE_END_TAG = "</code>"
CODE_START_TAG = "<pre><code>"
CODE_END_TAG = "</code></pre>"
CODE_TAG_EXP = re.compile(CODE_START_TAG+'.*?'+CODE_END_TAG+'|'+ONE_LINE_CODE_START_TAG+'.*?'+ONE_LINE_CODE_END_TAG, re.DOTALL)

def getTags(content):
    tags = list(map(lambda x:x['tag'], content['tags']))
    return tags


def convertCodeTags(content):
    codes = CODE_TAG_EXP.findall(content['body'])
    # remove all character reference & <code> tags
    for code in codes:
        if CODE_START_TAG in code and CODE_END_TAG in code:
            content['body'] = content['body'].replace(code, '\n\n' + \
                html.unescape(code[len(CODE_START_TAG):-len(CODE_END_TAG)]) + \
                    '\n\n')
        elif ONE_LINE_CODE_END_TAG in code and ONE_LINE_CODE_START_TAG in code:
            content['body'] = content['body'].replace(code, '\n\n' + \
                html.unescape(code[len(ONE_LINE_CODE_START_TAG):-len(ONE_LINE_CODE_END_TAG)]) + \
                    '\n\n')
    
    return content


def convertToMarkdown(content):
    markdown =  '---\n'\
        'author: "isofurabon"\n' \
        f'title: "{content["title"]}"\n' \
        f'slug: "{content["slug"]}"\n' \
        f'date: {content["date"]}\n' \
        f'tags: {getTags(content)}\n' \
        '---\n' \
        f'{convertCodeTags(content)["body"]}'
    return markdown
