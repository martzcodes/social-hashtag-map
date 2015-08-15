(function() {
  var controllers;

  controllers = angular.module('pollApp.controllers', []);

  controllers.controller('tweetListController', function($scope, $state, $log, Tweets, VerifiedTweets) {
    Tweets.fetch();
    VerifiedTweets.fetch();
    $scope.tweets = Tweets.data().all;
    $scope.verifiedtweets = VerifiedTweets.data().all;
    $log.info("Tweets", $scope.tweets);
    return $log.info("Verified Tweets", $scope.verifiedtweets);
  });

}).call(this);
