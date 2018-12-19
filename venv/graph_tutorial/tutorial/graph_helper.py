from requests_oauthlib import OAuth2Session
from pprint import pprint
import json

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format(graph_url))
  # Return the JSON result
  return user.json()

def get_calendar_events(token):
  graph_client = OAuth2Session(token=token)

  # Configure query parameters to
  # modify the results
  query_params = {
    '$select': 'subject,organizer,start,end',
    '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events
  events = graph_client.get('{0}/me/events'.format(graph_url), params=query_params)
  # Return the JSON result
  return events.json()

def get_onenote_pages(token):
    client = OAuth2Session(token=token)
    # pages = client.get('{0}/me/onenote/pages'.format(graph_url))
    ids = client.get('{0}/me/onenote/pages?$select=id,lastModifiedDateTime,title'.format(graph_url))
#    pprint(ids.json())
    return ids.json()

def get_page_content(token, ids):
    client = OAuth2Session(token=token)

    with open('C:/Temp/notes.txt', 'w') as file:
        for id in ids:
            content = client.get('{0}/me/onenote/pages/{1}/content'.format(graph_url, id))
            file.write(json.dumps(content.text))
            file.write('\n')