controllers = angular.module('pollApp.controllers', [])

controllers.controller('tweetListController', ($scope, $state, $log, Tweets, VerifiedTweets) ->
    Tweets.fetch()
    VerifiedTweets.fetch()
    $scope.tweets = Tweets.data().all
    $scope.verifiedtweets = VerifiedTweets.data().all
    $log.info("Tweets",$scope.tweets)
    $log.info("Verified Tweets",$scope.verifiedtweets)
)