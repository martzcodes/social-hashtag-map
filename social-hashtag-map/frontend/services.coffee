services = angular.module('pollApp.services', [])

services.factory('Tweet', ($http, $log) ->
    class Tweet
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @user_name = data.user_name
            @known_user = data.known_user
            @content = data.content
            @lat = data.lat
            @lon = data.lon
            @profile_pic = data.profile_pic
            @content_date = data.content_date

        get : (tweetId) ->
            $http({method: 'GET', url: '/polls/tweet/' + tweetId + '/'})
            .success (data) =>
                @init(data)
                $log.info("Succesfully fetched tweet")
            .error (data) =>
                $log.info("Failed to fetch tweet.")
    return Tweet
)

services.factory('Hashtag', ($http, $log) ->
    class Tweet
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @hashtag = data.hashtag
            @tweet_count = data.tweet_count
            @insta_count = data.insta_count
            @verified_count = data.verified_count
            @unverified_count = data.unverified_count

        get : (tweetId) ->
            $http({method: 'GET', url: '/polls/tweet/' + tweetId + '/'})
            .success (data) =>
                @init(data)
                $log.info("Succesfully fetched tweet")
            .error (data) =>
                $log.info("Failed to fetch tweet.")
    return Tweet
)
services.factory('Member', ($http, $log) ->
    class Tweet
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @display_name = data.display_name
            @tweet_count = data.tweet_count
            @insta_count = data.content

        get : (tweetId) ->
            $http({method: 'GET', url: '/polls/tweet/' + tweetId + '/'})
            .success (data) =>
                @init(data)
                $log.info("Succesfully fetched tweet")
            .error (data) =>
                $log.info("Failed to fetch tweet.")
    return Tweet
)
services.factory('Team', ($http, $log) ->
    class Tweet
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @team_name = data.team_name
            @van_name = data.van_name
            @tweet_count = data.tweet_count
            @insta_count = data.insta_count

        get : (tweetId) ->
            $http({method: 'GET', url: '/polls/tweet/' + tweetId + '/'})
            .success (data) =>
                @init(data)
                $log.info("Succesfully fetched tweet")
            .error (data) =>
                $log.info("Failed to fetch tweet.")
    return Tweet
)

services.factory('Tweets', ($log, $http, Tweet) ->
    tweets = {
        all : [],
        location: []
    }

    fromServer: (data) ->
        tweets['all'].length = 0
        for tweet in data
            new_tweet = new Tweet(tweet)
            tweets['all'].push(new_tweet)
            if new_tweet.lat and new_tweet.lon
                tweets['location'].push(new_tweet)

    fetch: ->
        $http({method: 'GET', url: '/polls/tweets'})
            .success (data) =>
                $log.info("Succesfully fetched tweets.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch tweets.")

    data : ->
        return tweets
)

services.factory('VerifiedTweets', ($log, $http, Tweet) ->
    tweets = {
        all : [],
        location: []
    }

    fromServer: (data) ->
        tweets['all'].length = 0
        for tweet in data
            new_tweet = new Tweet(tweet)
            tweets['all'].push(new_tweet)
            if new_tweet.lat and new_tweet.lon
                tweets['location'].push(new_tweet)

    fetch: ->
        $http({method: 'GET', url: '/polls/tweets/verified'})
            .success (data) =>
                $log.info("Succesfully fetched tweets.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch tweets.")

    data : ->
        return tweets
)

services.factory('UnVerifiedTweets', ($log, $http, Tweet) ->
    tweets = {
        all : []
    }

    fromServer: (data) ->
        tweets['all'].length = 0
        for tweet in data
            tweets['all'].push(new Tweet(tweet))

    fetch: ->
        $http({method: 'GET', url: '/polls/tweets/unverified'})
            .success (data) =>
                $log.info("Succesfully fetched tweets.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch tweets.")

    data : ->
        return tweets
)

services.factory('LocationTweets', ($log, $http, Tweet) ->
    tweets = {
        all : []
    }

    fromServer: (data) ->
        tweets['all'].length = 0
        for tweet in data
            tweets['all'].push(new Tweet(tweet))

    fetch: ->
        $http({method: 'GET', url: '/polls/tweets/location'})
            .success (data) =>
                $log.info("Succesfully fetched tweets.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch tweets.")

    data : ->
        return tweets
)

services.factory('TeamStats', ($log, $http, Team) ->
    teams = {
        all : []
    }

    fromServer: (data) ->
        teams['all'].length = 0
        for team in data
            teams['all'].push(new Team(team))

    fetch: ->
        $http({method: 'GET', url: '/polls/team/stats'})
            .success (data) =>
                $log.info("Succesfully fetched teams.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch teams.")

    data : ->
        return teams
)

services.factory('MemberStats', ($log, $http, Member) ->
    members = {
        all : []
    }

    fromServer: (data) ->
        members['all'].length = 0
        for member in data
            members['all'].push(new Member(member))

    fetch: ->
        $http({method: 'GET', url: '/polls/member/stats'})
            .success (data) =>
                $log.info("Succesfully fetched members.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch members.")

    data : ->
        return members
)

services.factory('HashtagStats', ($log, $http, Hashtag) ->
    hashtags = {
        all : []
    }

    fromServer: (data) ->
        hashtags['all'].length = 0
        for hashtag in data
            hashtags['all'].push(new Hashtag(hashtag))

    fetch: ->
        $http({method: 'GET', url: '/polls/hashtag/stats'})
            .success (data) =>
                $log.info("Succesfully fetched hashtags.")
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch hashtags.")

    data : ->
        return hashtags
)