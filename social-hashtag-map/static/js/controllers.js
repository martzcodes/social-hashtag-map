(function() {
  var controllers;

  controllers = angular.module('pollApp.controllers', []);

  controllers.controller('postListController', function($scope, Posts, MemberStats, HashtagStats) {
    Posts.fetch(function() {
      $scope.posts = Posts.all();
      $scope.location_posts = Posts.location();
      MemberStats.fetch(function() {
        $scope.memberstats = MemberStats.all();
        return $scope.teamstats = MemberStats.teams();
      });
      return HashtagStats.fetch(function() {
        return $scope.hashtagstats = HashtagStats.counts();
      });
    });
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
