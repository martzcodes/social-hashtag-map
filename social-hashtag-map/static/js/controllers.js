(function() {
  var controllers;

  controllers = angular.module('pollApp.controllers', []);

  controllers.controller('postListController', function($scope, $interval, Posts, MemberStats, HashtagStats) {
    var checkPosts, fetchPosts;
    $scope.exchange_points = [
      {
        name: 'Start',
        lat: '39.700',
        lon: '-78.653'
      }, {
        name: 'Exchange 1',
        runner: 1,
        van: 1,
        lat: '39.701',
        lon: '-78.651'
      }, {
        name: 'Exchange 2',
        runner: 2,
        van: 1,
        lat: '39.708',
        lon: '-78.567'
      }, {
        name: 'Exchange 3',
        runner: 3,
        van: 1,
        lat: '39.662',
        lon: '-78.507'
      }, {
        name: 'Exchange 4',
        runner: 4,
        van: 1,
        lat: '39.616',
        lon: '-78.490'
      }, {
        name: 'Exchange 5',
        runner: 5,
        van: 1,
        lat: '39.603',
        lon: '-78.463'
      }, {
        name: 'Exchange 6',
        runner: 6,
        van: 1,
        lat: '39.627',
        lon: '-78.389'
      }, {
        name: 'Exchange 7',
        runner: 7,
        van: 2,
        lat: '39.705',
        lon: '-78.329'
      }, {
        name: 'Exchange 8',
        runner: 8,
        van: 2,
        lat: '39.697',
        lon: '-78.249'
      }, {
        name: 'Exchange 9',
        runner: 9,
        van: 2,
        lat: '39.701',
        lon: '-78.188'
      }, {
        name: 'Exchange 10',
        runner: 10,
        van: 2,
        lat: '39.689',
        lon: '-78.118'
      }, {
        name: 'Exchange 11',
        runner: 11,
        van: 2,
        lat: '39.612',
        lon: '-78.006'
      }, {
        name: 'Exchange 12',
        runner: 12,
        van: 2,
        lat: '39.612',
        lon: '-77.937'
      }, {
        name: 'Exchange 13',
        runner: 1,
        van: 1,
        lat: '39.630',
        lon: '-77.861'
      }, {
        name: 'Exchange 14',
        runner: 2,
        van: 1,
        lat: '39.594',
        lon: '-77.821'
      }, {
        name: 'Exchange 15',
        runner: 3,
        van: 1,
        lat: '39.550',
        lon: '-77.800'
      }, {
        name: 'Exchange 16',
        runner: 4,
        van: 1,
        lat: '39.513',
        lon: '-77.756'
      }, {
        name: 'Exchange 17',
        runner: 5,
        van: 1,
        lat: '39.473',
        lon: '-77.656'
      }, {
        name: 'Exchange 18',
        runner: 6,
        van: 1,
        lat: '39.457',
        lon: '-77.603'
      }, {
        name: 'Exchange 19',
        runner: 7,
        van: 2,
        lat: '39.438',
        lon: '-77.527'
      }, {
        name: 'Exchange 20',
        runner: 8,
        van: 2,
        lat: '39.380',
        lon: '-77.478'
      }, {
        name: 'Exchange 21',
        runner: 9,
        van: 2,
        lat: '39.380',
        lon: '-77.474'
      }, {
        name: 'Exchange 22',
        runner: 10,
        van: 2,
        lat: '39.293',
        lon: '-77.432'
      }, {
        name: 'Exchange 23',
        runner: 11,
        van: 2,
        lat: '39.293',
        lon: '-77.357'
      }, {
        name: 'Exchange 24',
        runner: 12,
        van: 2,
        lat: '39.147',
        lon: '-77.293'
      }, {
        name: 'Exchange 25',
        runner: 1,
        van: 1,
        lat: '39.128',
        lon: '-77.237'
      }, {
        name: 'Exchange 26',
        runner: 2,
        van: 1,
        lat: '39.099',
        lon: '-77.204'
      }, {
        name: 'Exchange 27',
        runner: 3,
        van: 1,
        lat: '39.070',
        lon: '-77.169'
      }, {
        name: 'Exchange 28',
        runner: 4,
        van: 1,
        lat: '39.053',
        lon: '-77.105'
      }, {
        name: 'Exchange 29',
        runner: 5,
        van: 1,
        lat: '39.021',
        lon: '-77.094'
      }, {
        name: 'Exchange 30',
        runner: 6,
        van: 1,
        lat: '38.963',
        lon: '-77.092'
      }, {
        name: 'Exchange 31',
        runner: 7,
        van: 2,
        lat: '38.962',
        lon: '-77.107'
      }, {
        name: 'Exchange 32',
        runner: 8,
        van: 2,
        lat: '38.907',
        lon: '-77.112'
      }, {
        name: 'Exchange 33',
        runner: 9,
        van: 2,
        lat: '38.890',
        lon: '-77.103'
      }, {
        name: 'Exchange 34',
        runner: 10,
        van: 2,
        lat: '38.892',
        lon: '-77.087'
      }, {
        name: 'Exchange 35',
        runner: 11,
        van: 2,
        lat: '38.867',
        lon: '-77.046'
      }, {
        name: 'Finish',
        runner: 12,
        van: 2,
        lat: '38.873',
        lon: '-77.002'
      }
    ];
    fetchPosts = function() {
      Posts.getLocation(function(location_posts) {
        return $scope.location_posts = location_posts.reverse();
      });
      return Posts.getRecent(function(posts) {
        $scope.posts = posts.all.reverse();
        $scope.tweets = posts.tweets.reverse();
        return $scope.instas = posts.instas.reverse();
        /*
        MemberStats.fetch ->
          $scope.memberstats = MemberStats.all()
          $scope.teamstats = MemberStats.teams()
        HashtagStats.fetch ->
          $scope.hashtagstats = HashtagStats.counts()
        */

      });
    };
    checkPosts = function() {
      return Posts.getRecent(function(posts) {
        $scope.posts = posts.all.reverse();
        $scope.tweets = posts.tweets.reverse();
        $scope.instas = posts.instas.reverse();
        return $scope.location_posts = posts.location;
      });
    };
    fetchPosts();
    $interval(checkPosts, 30000);
    $scope.mapMovedCallback = function(bounds) {
      console.log('You repositioned the map to:');
      console.log(bounds);
    };
    return $scope.mapZoomedCallback = function(bounds) {
      console.log('You zoomed the map to:');
      console.log(bounds.getCenter().toString());
    };
  });

}).call(this);
