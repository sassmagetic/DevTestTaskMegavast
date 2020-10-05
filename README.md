# Mission 1

To get all game names run ```python api.py```
To retrieve all game name I use some assumption because of random api response result.
I assume that if I have already got all games then I can make another 'total number of games' / 'number of games per requests' requests
and no new games would be retrieved. If name of the game always is returned with equal probability, with more requests I will get duplicates. But when I tested this approach sometimes I got less number of games, so for more confident result I make 2 * 'total number of games' / 'number of games per request' requests

# Mission 2
I use Flask for this task
Run ```pip install -r requirements.txt``` to intall it
Get result by following URL http://localhost:12345/TEST
To run server
```python server.py```

# Mission 3
Use the same server as in Mission 2
Get result by following URL http://localhost:12345/?search=[word]
