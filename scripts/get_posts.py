import json
import urllib.request

def createRequestForPublishedPosts(ENDPOINT, X_API_KEY, offset, limit):
    req = urllib.request.Request(f'{ENDPOINT}?offset={offset}&limit={limit}')
    req.add_header('X-API-KEY', X_API_KEY)
    return req

def createRequestForDraftPost(ENDPOINT, X_API_KEY, contentId, draftKey):
    req = urllib.request.Request(f'{ENDPOINT}/{contentId}?draftKey={draftKey}')
    req.add_header('X-API-KEY', X_API_KEY)
    return req

def openRequest(request):
    with urllib.request.urlopen(request) as res:
        body = res.read().decode('utf-8')
    return body

def getPublishedPosts(ENDPOINT, X_API_KEY, offset, limit):
    req = createRequestForPublishedPosts(ENDPOINT, X_API_KEY, offset, limit)
    body = openRequest(req)
    return json.loads(body)

def getDraftPost(ENDPOINT, X_API_KEY, contentId, draftKey):
    req = createRequestForDraftPost(ENDPOINT, X_API_KEY, contentId, draftKey)
    body = openRequest(req)
    return json.loads(body)
