controllers = angular.module('pollApp.controllers', [])

controllers.controller('tweetListController', ($scope, $state, $log, $timeout, Tweets, TeamStats, MemberStats, HashtagStats) ->
    $timeout(function() {
      var map = mapboxService.getMapInstances()[0];
      //mapboxService.fitMapToMarkers(map);
    }, 100);
    Tweets.fetch()
    TeamStats.fetch()
    MemberStats.fetch()
    HashtagStats.fetch()

    $scope.tweets = Tweets.data().all
    $scope.teamstats = TeamStats.data().all
    $scope.memberstats = MemberStats.data().all
    $scope.hashtagstats = HashtagStats.data().all
)