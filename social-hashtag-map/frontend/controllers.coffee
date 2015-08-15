controllers = angular.module('pollApp.controllers', [])

controllers.controller('tweetListController', ($scope, $state, $log, Tweets) ->
    Tweets.fetch()
    $scope.tweets = Tweets.data()
    $log.info("In controller",$scope.tweets)
)