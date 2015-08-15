# social-hashtag-map
Subscribe to twitter/instagram hashtags, verify users, put them on a map

## Based on

 - [Djangular](https://github.com/TrackMaven/Djangular.git)
 
 ## Checklist
 
 - [x] Add checklist to readme, remove old stuff
 - [x] Change requirements (Django 1.7.1, add celery, add python-oauth2, add python-instagram)
 - [x] pip install -r requirements.txt
 - [x] npm install
 - [ ] setup models (api keys, tweet model, instagram model, tag model, team models (team, van, user))
 - [ ] Integrate celery
 - [ ] Update readme with instructions for getting API keys
 - [ ] Add twitter and instagram tasks into celery
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