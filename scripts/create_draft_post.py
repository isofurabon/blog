#!/usr/bin/env python3

from get_posts import getDraftPost
from convert_posts import convertToMarkdown
import os
from pathlib import Path

OUTPUT_PARENT_DIR = Path(os.environ['OUTPUT'])
OUTPUT_PARENT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    content = getDraftPost(os.environ['ENDPOINT'], os.environ['X_API_KEY'], os.environ['CONTENTID'], os.environ['DRAFTKEY'])
        
    # create file
    filepath = OUTPUT_PARENT_DIR / f'{content["slug"]}.md'
    print(f'{filepath} ...\t', end="")
    with open(filepath, 'w') as file:
        file.write(convertToMarkdown(content))
    print('COMPLETE!!')

if __name__ == "__main__":
    main()