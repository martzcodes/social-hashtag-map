(function() {
  var services;

  services = angular.module('pollApp.services', []);

  services.factory('Tweet', function($http, $log) {
    var Tweet;
    Tweet = (function() {
      function Tweet(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Tweet.prototype.init = function(data) {
        this.user_name = data.user_name;
        this.known_user = data.known_user;
        this.content = data.content;
        this.lat = data.lat;
        this.lon = data.lon;
        this.profile_pic = data.profile_pic;
        return this.content_date = data.content_date;
      };

      Tweet.prototype.get = function(tweetId) {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/tweet/' + tweetId + '/'
        }).success(function(data) {
          _this.init(data);
          return $log.info("Succesfully fetched tweet");
        }).error(function(data) {
          return $log.info("Failed to fetch tweet.");
        });
      };

      return Tweet;

    })();
    return Tweet;
  });

  services.factory('Tweets', function($log, $http, Tweet) {
    var tweets;
    $log.info("fetching tweets.");
    tweets = {
      all: []
    };
    return {
      fromServer: function(data) {
        var tweet, _i, _len, _results;
        tweets['all'].length = 0;
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          tweet = data[_i];
          _results.push(tweets['all'].push(new Tweet(tweet)));
        }
        return _results;
      },
      fetch: function() {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/tweets'
        }).success(function(data) {
          $log.info("Succesfully fetched tweets.", data);
          return _this.fromServer(data);
        }).error(function(data) {
          return $log.info("Failed to fetch tweets.");
        });
      },
      data: function() {
        return tweets;
      }
    };
  });

}).call(this);
