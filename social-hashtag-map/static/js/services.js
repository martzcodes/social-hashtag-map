(function() {
  var services;

  services = angular.module('pollApp.services', []);

  services.factory('Post', function($log) {
    var Post;
    Post = (function() {
      function Post(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Post.prototype.init = function(data) {
        this.name = data.display_name;
        this.user_name = data.user_name;
        this.known_user = data.known_user;
        this.content = data.content;
        if (data.has_location) {
          this.lat = data.lat;
          this.lon = data.lon;
        }
        this.thumbnail = data.thumbnail_link;
        this.image = data.image_link;
        this.profile_pic = data.profile_pic;
        this.content_date = data.content_date;
        return this.source = data.source_type;
      };

      return Post;

    })();
    return Post;
  });

  services.factory('Hashtag', function($log) {
    var Hashtag;
    Hashtag = (function() {
      function Hashtag(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Hashtag.prototype.init = function(data) {
        this.hashtag = data.hashtag;
        this.verified = data.verified_count;
        return this.unverified = data.unverified_count;
      };

      return Hashtag;

    })();
    return Hashtag;
  });

  services.factory('Member', function($log) {
    var Member;
    Member = (function() {
      function Member(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Member.prototype.init = function(data) {
        this.display_name = data.display_name;
        this.tweet_count = data.tweet_count;
        this.insta_count = data.insta_count;
        this.team = data.team_choice;
        this.van = data.van_choice;
        return this.runner = data.runner_number;
      };

      return Member;

    })();
    return Member;
  });

  services.factory('Van', function($log) {
    var Van;
    Van = (function() {
      function Van(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Van.prototype.init = function(data) {
        if (data.van === 'V1') {
          this.name = 'Van 1';
        }
        if (data.van === 'V2') {
          this.name = 'Van 2';
        }
        this.tweet_count = data.tweet_count;
        this.insta_count = data.insta_count;
        return this.runners = [data];
      };

      return Van;

    })();
    return Van;
  });

  services.factory('Team', function($log, Van) {
    var Team;
    Team = (function() {
      function Team(data) {
        if (data !== null) {
          this.init(data);
        }
      }

      Team.prototype.init = function(data) {
        if (data.team === 'T1') {
          this.name = 'Team 1';
        } else if (data.team === 'T2') {
          this.name = 'Team 2';
        } else {
          this.name = 'Boundary Stone Supporters';
        }
        this.tweet_count = data.tweet_count;
        this.insta_count = data.insta_count;
        if (data.team === 'T1' || data.team === 'T2') {
          this.vans = [];
          this.runners = [data];
          return this.processVan(data);
        }
      };

      Team.prototype.processVan = function(data) {
        var new_van, van_index;
        van_index = this.vans.map(function(van) {
          return van.name;
        }).indexOf(data.van);
        if (van_index !== -1) {
          this.vans[van_index]['tweet_count'] += data.tweet_count;
          this.vans[van_index]['insta_count'] += data.insta_count;
          return this.vans[van_index]['runners'].push(data);
        } else {
          new_van = new Van(data);
          return this.vans.push(new_van);
        }
      };

      return Team;

    })();
    return Team;
  });

  services.factory('Posts', function($log, $http, Post) {
    var posts;
    posts = {
      all: [],
      verified: [],
      unverified: [],
      tweets: [],
      instas: [],
      location: []
    };
    return {
      postsReset: function(callback) {
        posts = {
          all: [],
          verified: [],
          unverified: [],
          tweets: [],
          instas: [],
          location: []
        };
        return callback();
      },
      fromServer: function(data, callback) {
        return this.postsReset(function() {
          var new_post, post, _i, _len;
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            post = data[_i];
            new_post = new Post(post);
            posts['all'].push(new_post);
            if (new_post.source === 'TW') {
              posts['tweets'].push(new_post);
            }
            if (new_post.source === 'IN') {
              posts['instas'].push(new_post);
            }
            if (new_post.known_user) {
              posts['verified'].push(new_post);
              if (new_post.lat && new_post.lon) {
                posts['location'].push(new_post);
              }
            } else {
              posts['unverified'].push(new_post);
            }
          }
          return callback(posts);
        });
      },
      fetch: function(callback) {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/posts'
        }).success(function(data) {
          $log.info("Succesfully fetched posts.");
          return _this.fromServer(data, callback);
        }).error(function(data) {
          return $log.info("Failed to fetch posts.");
        });
      },
      recent: function(callback) {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/posts/recent'
        }).success(function(data) {
          return $log.info("Succesfully fetched recent posts.");
        }).error(function(data) {
          return $log.info("Failed to fetch posts.");
        });
      },
      recent: function(callback) {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/posts/recent'
        }).success(function(data) {
          return $log.info("Succesfully fetched location posts.");
        }).error(function(data) {
          return $log.info("Failed to fetch posts.");
        });
      },
      data: function() {
        return posts;
      },
      all: function() {
        return posts.all;
      },
      tweets: function() {
        return posts.tweets;
      },
      instas: function() {
        return posts.instas;
      },
      location: function() {
        return posts.location;
      },
      verified: function() {
        return posts.verified;
      },
      unverified: function() {
        return posts.unverified;
      }
    };
  });

  services.factory('MemberStats', function($log, $http, Member, Team) {
    var members;
    members = {
      all: [],
      teams: []
    };
    return {
      membersReset: function(callback) {
        members = {
          all: [],
          teams: []
        };
        return callback();
      },
      fromServer: function(data, callback) {
        return this.membersReset(function() {
          var member, new_member, new_team, team_index, _i, _len;
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            member = data[_i];
            new_member = new Member(member);
            members['all'].push(new_member);
            team_index = members['teams'].map(function(team) {
              return team.name;
            }).indexOf(new_member.team);
            if (team_index !== -1) {
              members['teams'][team_index]['tweet_count'] += new_member.tweet_count;
              members['teams'][team_index]['insta_count'] += new_member.insta_count;
              members['teams'][team_index].processVan(new_member);
              members['teams'][team_index]['runners'].push(new_member);
            } else {
              new_team = new Team(new_member);
              members['teams'].push(new_team);
            }
          }
          return callback();
        });
      },
      fetch: function(callback) {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/member/stats'
        }).success(function(data) {
          $log.info("Succesfully fetched members.");
          return _this.fromServer(data, callback);
        }).error(function(data) {
          return $log.info("Failed to fetch members.");
        });
      },
      data: function() {
        return members;
      },
      all: function() {
        return members.all;
      },
      teams: function() {
        return members.teams;
      }
    };
  });

  services.factory('HashtagStats', function($log, $http, Hashtag) {
    var hashtags;
    hashtags = {
      all: [],
      verified: 0,
      unverified: 0,
      total: 0
    };
    return {
      hashtagsReset: function(callback) {
        hashtags = {
          all: [],
          verified: 0,
          unverified: 0,
          total: 0
        };
        return callback();
      },
      fromServer: function(data, callback) {
        return this.hashtagsReset(function() {
          var hashtag, new_hashtag, _i, _len;
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            hashtag = data[_i];
            new_hashtag = new Hashtag(hashtag);
            hashtags['all'].push(new_hashtag);
            hashtags['verified'] += new_hashtag.verified;
            hashtags['unverified'] += new_hashtag.unverified;
            hashtags['total'] += new_hashtag.verified + new_hashtag.unverified;
          }
          return callback();
        });
      },
      fetch: function(callback) {
        var _this = this;
        return $http({
          method: 'GET',
          url: '/polls/hashtag/stats'
        }).success(function(data) {
          $log.info("Succesfully fetched hashtags.");
          return _this.fromServer(data, callback);
        }).error(function(data) {
          return $log.info("Failed to fetch hashtags.");
        });
      },
      data: function() {
        return hashtags;
      },
      all: function() {
        return hashtags.all;
      },
      verified: function() {
        return hashtags.verified;
      },
      unverified: function() {
        return hashtags.unverified;
      },
      counts: function() {
        return {
          verified: hashtags.verified,
          unverified: hashtags.unverified,
          total: hashtags.total
        };
      }
    };
  });

}).call(this);
