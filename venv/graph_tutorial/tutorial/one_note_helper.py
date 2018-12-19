from requests_oauthlib import OAuth2Session

onenote_url = "https://graph.microsoft.com/v1.0/me/onenote"

def get_user(token):
    graph_client = OAuth2Session(token=token)
    # Send GET to /me
    user = graph_client.get('{0}/me'.format(onenote_url))
    # Return the JSON result
    return user.json()

def get_onenote_pages(token):
    client = OAuth2Session(token=token)

    pages = client.get('{0}/pages?select=title,self'.format(onenote_url))
    return pages.json()

"""
  query_params = {
    '$select': 'subject,organizer,start,end',
    '$orderby': 'createdDateTime DESC'
  }

  # Send GET to /me/events
  events = graph_client.get('{0}/me/events'.format(graph_url), params=query_params)
  # Return the JSON result"""