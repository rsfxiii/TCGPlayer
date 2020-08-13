from configparser import ConfigParser

import requests


class Client:
    def __init__(self):
        """ Establish default class properties """
        self._config = {
            'data': None,
            'parser': None
        }
        self._session = {
            'obj': None,
            'access': None
        }

    def read_config(self, config='config.ini', section='Default'):
        """ Load config data into bound dictionary """
        self._config['parser'] = ConfigParser()
        file = open(config, 'r')
        self._config['parser'].read_file(file)
        file.close()

        if section in self._config['parser'].sections():
            self._config['data'] = dict(self._config['parser'].items(section))

    def refresh_access(self, refresh_url):
        """ Update access attribute with fresh access object """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': str(self._config['data']['pubkey']),
            'client_secret': str(self._config['data']['privkey'])
        }

        response = requests.post(refresh_url, data=data, headers=headers)
        if response.status_code == 200:
            self._session['access'] = response.json()

    def authorize_session(self):
        """ Update bound session object with bound access data """
        token = self._session['access']['access_token']

        self._session['obj'] = requests.Session()
        self._session['obj'].headers.update({'Authorization': f'Bearer {token}'})

    def _handle_request(self, method, url, data=None):
        print(url)
        res = self._session['obj'].request(method.upper(), url, data=data)
        if res.status_code == 200:
            return res.json()
        else:
            print(res.text)




if __name__ == '__main__':
    # Bootstrap the client
    client = Client()
    client.read_config()

    # Init an API instance w/ Client    
    categories = Categories(client=client)

    client.refresh_access(refresh_url=categories.refresh_url)
    client.authorize_session()

    groups = Groups(client)
    print(groups.base_url)
    # print(groups.list(1))

    import urllib.parse as urlparse
    from urllib.parse import urlencode

    parts = list(urlparse.urlparse(groups.base_url))
    params = {'categoryId': 1}

    query = dict(urlparse.parse_qs(parts[4]))
    query.update(params)

    assert query == params

    parts[4] = urlencode(query)
    print(parts)

    print(urlparse.urlunparse(parts))

    # TODO: Write tests for these
    # print(categories.list())
    # print(categories.get_details('1'))
    # print(categories.get_search_manifest('1'))
    # print(categories.list_groups('1'))
    # print(categories.get_rarities('1'))
    # print(categories.get_printings('1'))
    # print(categories.list_languages('1'))
    # print(categories.list_media('1'))

    # import pdb; pdb.set_trace()
