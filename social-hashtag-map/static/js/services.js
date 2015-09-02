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

  services.factory('Hashtag', function($http, $log) {
    var Tweet;
    Tweet = (function() {
      function Tweet(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Tweet.prototype.init = function(data) {
        this.hashtag = data.hashtag;
        this.tweet_count = data.tweet_count;
        this.insta_count = data.insta_count;
        this.verified_count = data.verified_count;
        return this.unverified_count = data.unverified_count;
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

  services.factory('Member', function($http, $log) {
    var Tweet;
    Tweet = (function() {
      function Tweet(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Tweet.prototype.init = function(data) {
        this.display_name = data.display_name;
        this.tweet_count = data.tweet_count;
        return this.insta_count = data.content;
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

  services.factory('Team', function($http, $log) {
    var Tweet;
    Tweet = (function() {
      function Tweet(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Tweet.prototype.init = function(data) {
        this.team_name = data.team_name;
        this.van_name = data.van_name;
        this.tweet_count = data.tweet_count;
        return this.insta_count = data.insta_count;
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
    tweets = {
      all: [],
      location: []
    };
    return {
      fromServer: function(data) {
        var new_tweet, tweet, _i, _len, _results;
        tweets['all'].length = 0;
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          tweet = data[_i];
          new_tweet = new Tweet(tweet);
          tweets['all'].push(new_tweet);
          if (new_tweet.lat && new_tweet.lon) {
            _results.push(tweets['location'].push(new_tweet));
          } else {
            _results.push(void 0);
          }
        }
        return _results;
      },
      fetch: function() {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/tweets'
        }).success(function(data) {
          $log.info("Succesfully fetched tweets.");
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

  services.factory('VerifiedTweets', function($log, $http, Tweet) {
    var tweets;
    tweets = {
      all: [],
      location: []
    };
    return {
      fromServer: function(data) {
        var new_tweet, tweet, _i, _len, _results;
        tweets['all'].length = 0;
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          tweet = data[_i];
          new_tweet = new Tweet(tweet);
          tweets['all'].push(new_tweet);
          if (new_tweet.lat && new_tweet.lon) {
            _results.push(tweets['location'].push(new_tweet));
          } else {
            _results.push(void 0);
          }
        }
        return _results;
      },
      fetch: function() {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/tweets/verified'
        }).success(function(data) {
          $log.info("Succesfully fetched tweets.");
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

  services.factory('UnVerifiedTweets', function($log, $http, Tweet) {
    var tweets;
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
          url: '/polls/tweets/unverified'
        }).success(function(data) {
          $log.info("Succesfully fetched tweets.");
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

  services.factory('LocationTweets', function($log, $http, Tweet) {
    var tweets;
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
          url: '/polls/tweets/location'
        }).success(function(data) {
          $log.info("Succesfully fetched tweets.");
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

  services.factory('TeamStats', function($log, $http, Team) {
    var teams;
    teams = {
      all: []
    };
    return {
      fromServer: function(data) {
        var team, _i, _len, _results;
        teams['all'].length = 0;
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          team = data[_i];
          _results.push(teams['all'].push(new Team(team)));
        }
        return _results;
      },
      fetch: function() {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/team/stats'
        }).success(function(data) {
          $log.info("Succesfully fetched teams.");
          return _this.fromServer(data);
        }).error(function(data) {
          return $log.info("Failed to fetch teams.");
        });
      },
      data: function() {
        return teams;
      }
    };
  });

  services.factory('MemberStats', function($log, $http, Member) {
    var members;
    members = {
      all: []
    };
    return {
      fromServer: function(data) {
        var member, _i, _len, _results;
        members['all'].length = 0;
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          member = data[_i];
          _results.push(members['all'].push(new Member(member)));
        }
        return _results;
      },
      fetch: function() {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/member/stats'
        }).success(function(data) {
          $log.info("Succesfully fetched members.");
          return _this.fromServer(data);
        }).error(function(data) {
          return $log.info("Failed to fetch members.");
        });
      },
      data: function() {
        return members;
      }
    };
  });

  services.factory('HashtagStats', function($log, $http, Hashtag) {
    var hashtags;
    hashtags = {
      all: []
    };
    return {
      fromServer: function(data) {
        var hashtag, _i, _len, _results;
        hashtags['all'].length = 0;
        _results = [];
        for (_i = 0, _len = data.length; _i < _len; _i++) {
          hashtag = data[_i];
          _results.push(hashtags['all'].push(new Hashtag(hashtag)));
        }
        return _results;
      },
      fetch: function() {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/hashtag/stats'
        }).success(function(data) {
          $log.info("Succesfully fetched hashtags.");
          return _this.fromServer(data);
        }).error(function(data) {
          return $log.info("Failed to fetch hashtags.");
        });
      },
      data: function() {
        return hashtags;
      }
    };
  });

}).call(this);
