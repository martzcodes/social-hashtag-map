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

## Notes

Ended up moving instagram to the bottom... didn't realize their api doesn't let you search for multiple tags at once, so I have to figure out how I want to do that...

Edit: delaying cron-like celery checking for now... would be annoying for development

For some reason the controller wouldn't resolve tweets when in the stateProvider, so I bypassed it.  Will go back and fix later

## Checklist
 
 - [x] Add checklist to readme, remove old stuff
 - [x] Change requirements (Django 1.7.1, add celery, add oauth2, add python-instagram)
 - [x] pip install -r requirements.txt
 - [x] npm install
 - [x] setup models (api keys, tweet model, instagram model, tag model, team models (team, van, user))
 - [x] Install Redis (for celery) `brew install redis` & `redis-server`
 - [x] Integrate celery
 - [x] Update readme with instructions for getting API keys
 - [x] Add twitter task into celery
 - [X] Process twitter results
 - [x] Check if tweets are from known people
 - [x] Store tweets
 - [x] Setup endpoint to retrieve tweets (all)
 - [x] Setup endpoint to retrieve tweets (unverified, verified, combined, has location)
 - [x] Calculate Stats
 - [x] Setup endpoint to retrieve stats
 - [x] Move to front end...
 - [x] List Tweets (raw)
 - [x] List Stats (raw)
 - [ ] General Layout
 - [ ] Highlight verified (team member) tweets
 - [ ] Highlight most recent tweets
 - [ ] “Style” tweets
 - [ ] “Style” pics
 - [ ] “Style” Stats
 - [ ] Process out locations, put them on a map (mapbox?)
 - [ ] Style map
 - [ ] Add instagram task into celery
 - [ ] Process instagram results
 - [ ] Have celery check instagram at x-frequency
 - [ ] Check if instas are from known people
 - [ ] Store instas
 - [ ] Setup endpoint to retrieve instas (separate, verified only, separate + verified)
 - [ ] Setup endpoint to retrieve combined tweets and instas
 - [ ] List Pics (raw)
 - [ ] Highlight verified (team member) instas
 - [ ] Setup master endpoint with all info
 - [ ] Have celery check twitter at x-frequency
 - [ ] Fix resolve issue in stateProvider