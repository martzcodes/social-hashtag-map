(function() {
  var controllers;

  controllers = angular.module('pollApp.controllers', []);

  controllers.controller('tweetListController', function($scope, $state, $log, Tweets, TeamStats, MemberStats, HashtagStats, mapboxService) {
    Tweets.fetch();
    TeamStats.fetch();
    MemberStats.fetch();
    HashtagStats.fetch();
    $scope.tweets = Tweets.data().all;
    $scope.teamstats = TeamStats.data().all;
    $scope.memberstats = MemberStats.data().all;
    return $scope.hashtagstats = HashtagStats.data().all;
  });

}).call(this);
