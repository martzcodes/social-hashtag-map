(function() {
  var controllers;

  controllers = angular.module('pollApp.controllers', []);

  controllers.controller('tweetListController', function($scope, $state, $log, Tweets) {
    $scope.tweets = Tweets.all;
    return $log.info("In controller", $scope.tweets);
  });

}).call(this);
