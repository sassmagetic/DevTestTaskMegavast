import requests
from collections import Counter


class GamesApiException(Exception):
    pass


class GamesAPI:
    def __init__(self):
        self._url = 'https://www.magetic.com/c/test?api=1&name=Illia_Busov'
        self._games_set = set() # Use set to collect game names

    def request(self):
        '''
        Return response from http GET request 
        '''
        return requests.get(self._url)

    def _process_response(self, response):
        '''
        Raise exception if API returned error and set of game names if no error
        '''
        if 'Error 501' in response.text:
            raise GamesApiException('Error 501 from server')

        return set(response.text.split(';')[:-1])

    def add_to_games_set(self, items):
        '''
        Add new game names to the result set
        '''
        self._games_set |= items

    def get_request_result(self):
        '''
        Get set of game names from one api request
        '''
        response = self.request()
        return self._process_response(response)
    
    def check_new_item(self, items):
        '''
        Check if there are new game names in the given set of games
        '''
        return len(self._games_set.intersection(items)) != len(items)

    def get_game_names(self):
        '''
        Get all sorted game names
        '''
        return sorted(list(self._games_set))

    def get_json(self):
        '''
        Get game names in json format
        '''
        return {'total_number': len(self.get_game_names()),
        'games': [{
            'name': item,
            'number': int(i + 1)
        } for i, item in enumerate(self.get_game_names())]
        }

    def save_all_games(self):
        '''
        Retrive all game names from the api
        '''
        self._games_set = set()  # clear game names set
        consecutive_no_new_items = 0  # consecutive api requests that return already retrieved games 
        max_games_by_request = 6

        
        while True:
            try:
                games = self.get_request_result()
            except GamesApiException:
                continue

            new_items = self.check_new_item(games)
            if not new_items:
                consecutive_no_new_items += 1
            else:
                consecutive_no_new_items = 0 

            # Quit loop if no more new items are retrieved by multiple consecutive requests
            if 2 * len(self.get_game_names()) // max_games_by_request < consecutive_no_new_items:
                break
            self.add_to_games_set(games)
        


if __name__ == '__main__':
    api = GamesAPI()
    api.save_all_games()
    print(api.get_json())
