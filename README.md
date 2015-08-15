# social-hashtag-map
Subscribe to twitter/instagram hashtags, verify users, put them on a map

## Based on

 - [Djangular](https://github.com/TrackMaven/Djangular.git)
 
## API Keys

### Twitter

Go here: [https://apps.twitter.com/app/new](https://apps.twitter.com/app/new)

Sign up for an app, get the keys (client id and secret)

### Instagram

Go here: [https://instagram.com/developer/clients/register/](https://instagram.com/developer/clients/register/)

Register, clone [python-instagram](https://github.com/Instagram/python-instagram)

Run `python get_access_token.py`, follow the directions, copy the access_token.  You'll need the access_token and client_secret

## Checklist
 
 - [x] Add checklist to readme, remove old stuff
 - [x] Change requirements (Django 1.7.1, add celery, add oauth2, add python-instagram)
 - [x] pip install -r requirements.txt
 - [x] npm install
 - [x] setup models (api keys, tweet model, instagram model, tag model, team models (team, van, user))
 - [x] Install Redis `brew install redis` & `redis-server`
 - [x] Integrate celery
 - [x] Update readme with instructions for getting API keys
 - [x] Add twitter task into celery
 - [ ] Add instagram task into celery
 - [ ] Process twitter results
 - [ ] Process instagram results
 - [ ] Have celery check twitter/instagram at x-frequency
 - [ ] Check if tweets/instagrams are from known people
 - [ ] Store tweets/instagrams
 - [ ] Setup endpoint to retrieve tweets/instagrams (combined, separate, verified only, separate + verified)
 - [ ] Setup endpoint to retrieve stats
 - [ ] Setup master endpoint with all info
 - [ ] Move to front end
 - [ ] List Tweets (raw)
 - [ ] List Pics (raw)
 - [ ] List Stats (raw)
 - [ ] Highlight verified tweets/pics
 - [ ] Highlight most recent tweets/pics
 - [ ] “Style” tweets
 - [ ] “Style” pics
 - [ ] “Style” Stats
 - [ ] Process out locations, put them on a map (mapbox?)
 - [ ] Style map