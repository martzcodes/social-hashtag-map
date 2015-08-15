(function() {
  var controllers;

  controllers = angular.module('pollApp.controllers', []);

  controllers.controller('tweetListController', function($scope, $state, $log, Tweets) {
    Tweets.fetch();
    $scope.tweets = Tweets.data();
    return $log.info("In controller", $scope.tweets);
  });

}).call(this);
