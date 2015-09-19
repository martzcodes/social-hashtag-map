services = angular.module('pollApp.services', [])

services.factory('Post', ($log) ->
    class Post
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @name = data.display_name
            @user_name = data.user_name
            @known_user = data.known_user
            @content = data.content
            if data.has_location
                @lat = data.lat
                @lon = data.lon
            @thumbnail = data.thumbnail_link
            @image = data.image_link
            @profile_pic = data.profile_pic
            @content_date = data.content_date
            @source = data.source_type
    return Post
)
services.factory('Hashtag', ($log) ->
    class Hashtag
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @hashtag = data.hashtag
            @verified = data.verified_count
            @unverified = data.unverified_count
    return Hashtag
)
services.factory('Member', ($log) ->
    class Member
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            @display_name = data.display_name
            @tweet_count = data.tweet_count
            @insta_count = data.insta_count
            @team = data.team_choice
            @van = data.van_choice
            @runner = data.runner_number
    return Member
)
services.factory('Van', ($log) ->
    class Van
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            if data.van == 'V1'
                @name = 'Van 1'
            if data.van == 'V2'
                @name = 'Van 2'
            @tweet_count = data.tweet_count
            @insta_count = data.insta_count
            @runners = [data]
    return Van
)
services.factory('Team', ($log, Van) ->
    class Team
        constructor : (data) ->
            if data != null
                @init(data)
        init : (data) ->
            if data.team == 'T1'
                @name = 'Team 1'
            else if data.team == 'T2'
                @name = 'Team 2'
            else
                @name = 'Boundary Stone Supporters'
            @tweet_count = data.tweet_count
            @insta_count = data.insta_count
            if data.team == 'T1' or data.team == 'T2'
                @vans = []
                @runners = [data]
                @processVan(data)
        processVan : (data) ->
            van_index = @vans.map((van) ->
                van.name
            ).indexOf(data.van)
            if van_index != -1
                @vans[van_index]['tweet_count'] += data.tweet_count
                @vans[van_index]['insta_count'] += data.insta_count
                @vans[van_index]['runners'].push(data)
            else
                new_van = new Van(data)
                @vans.push(new_van)

    return Team
)

services.factory('Posts', ($log, $http, Post) ->
    posts = {
        all : [],
        verified: [],
        unverified: [],
        tweets: [],
        instas: [],
        location: []
    }
    postsReset: (callback) ->
        posts = {
            all : [],
            verified: [],
            unverified: [],
            tweets: [],
            instas: [],
            location: []
        }
        callback()

    fromServer: (data,callback) ->
        @postsReset ->
            for post in data
                new_post = new Post(post)
                posts['all'].push(new_post)
                if new_post.source == 'TW'
                    posts['tweets'].push(new_post)
                if new_post.source == 'IN'
                    posts['instas'].push(new_post)
                if new_post.known_user
                    posts['verified'].push(new_post)
                    if new_post.lat and new_post.lon
                        posts['location'].push(new_post)
                else
                    posts['unverified'].push(new_post)
            callback()

    fetch: (callback) ->
        $http({method: 'GET', url: '/polls/posts'})
            .success (data) =>
                $log.info("Succesfully fetched posts.")
                @fromServer(data,callback)
            .error (data) =>
                $log.info("Failed to fetch posts.")

    data : ->
        return posts

    all : ->
        return posts.all

    tweets : ->
        return posts.tweets

    instas : ->
        return posts.instas

    location : ->
        return posts.location

    verified : ->
        return posts.verified

    unverified : ->
        return posts.unverified
)

services.factory('MemberStats', ($log, $http, Member, Team) ->
    members = {
        all : [],
        teams : []
    }

    membersReset: (callback) ->
        members = {
            all : [],
            teams : []
        }
        callback()

    fromServer: (data,callback) ->
        @membersReset ->
            for member in data
                new_member = new Member(member)
                members['all'].push(new_member)
                team_index = members['teams'].map((team) ->
                    team.name
                ).indexOf(new_member.team)
                if team_index != -1
                    members['teams'][team_index]['tweet_count'] += new_member.tweet_count
                    members['teams'][team_index]['insta_count'] += new_member.insta_count
                    members['teams'][team_index].processVan(new_member)
                    members['teams'][team_index]['runners'].push(new_member)
                else
                    new_team = new Team(new_member)
                    members['teams'].push(new_team)
            callback()

    fetch: (callback) ->
        $http({method: 'GET', url: '/polls/member/stats'})
            .success (data) =>
                $log.info("Succesfully fetched members.")
                @fromServer(data,callback)
            .error (data) =>
                $log.info("Failed to fetch members.")

    data : ->
        return members

    all : ->
        return members.all

    teams : ->
        return members.teams
)

services.factory('HashtagStats', ($log, $http, Hashtag) ->
    hashtags = {
        all : [],
        verified : 0,
        unverified : 0,
        total: 0
    }

    hashtagsReset: (callback) ->
        hashtags = {
            all : [],
            verified : 0,
            unverified : 0,
            total: 0
        }
        callback()

    fromServer: (data,callback) ->
        @hashtagsReset ->
            for hashtag in data
                new_hashtag = new Hashtag(hashtag)
                hashtags['all'].push(new_hashtag)
                hashtags['verified'] += new_hashtag.verified
                hashtags['unverified'] += new_hashtag.unverified
                hashtags['total'] += new_hashtag.verified + new_hashtag.unverified
            callback()

    fetch: (callback) ->
        $http({method: 'GET', url: '/polls/hashtag/stats'})
            .success (data) =>
                $log.info("Succesfully fetched hashtags.")
                @fromServer(data,callback)
            .error (data) =>
                $log.info("Failed to fetch hashtags.")

    data : ->
        return hashtags

    all : ->
        return hashtags.all

    verified : ->
        return hashtags.verified

    unverified : ->
        return hashtags.unverified

    counts : ->
        return {verified: hashtags.verified, unverified: hashtags.unverified, total: hashtags.total}
)