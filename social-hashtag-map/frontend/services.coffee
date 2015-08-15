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

services.factory('Tweets', ($log, $http, Tweet) ->
    $log.info("fetching tweets.")
    tweets = {
        all : []
    }

    fromServer: (data) ->
        tweets['all'].length = 0
        for tweet in data
            tweets['all'].push(new Tweet(tweet))

    fetch: ->
        $http({method: 'GET', url: '/polls/tweets'})
            .success (data) =>
                $log.info("Succesfully fetched tweets.",data)
                @fromServer(data)
            .error (data) =>
                $log.info("Failed to fetch tweets.")

    data : ->
        return tweets
)


