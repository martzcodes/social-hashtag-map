controllers = angular.module('pollApp.controllers', [])

controllers.controller('tweetListController', ($scope, $state, $log, Tweets) ->
  $scope.tweets = Tweets.all
  $log.info("In controller",$scope.tweets)
)