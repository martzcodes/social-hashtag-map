controllers = angular.module('pollApp.controllers', [])

controllers.controller('tweetListController', ($scope, $state, $log, $timeout, Tweets, TeamStats, MemberStats, HashtagStats) ->
    Tweets.fetch()
    TeamStats.fetch()
    MemberStats.fetch()
    HashtagStats.fetch()

    $scope.tweets = Tweets.data().all
    $scope.teamstats = TeamStats.data().all
    $scope.memberstats = MemberStats.data().all
    $scope.hashtagstats = HashtagStats.data().all

    $scope.mapMovedCallback = (bounds) ->
      console.log 'You repositioned the map to:'
      console.log bounds
      return

    $scope.mapZoomedCallback = (bounds) ->
      console.log 'You zoomed the map to:'
      console.log bounds.getCenter().toString()
      return
)