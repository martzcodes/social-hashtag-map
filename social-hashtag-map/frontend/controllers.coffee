controllers = angular.module('pollApp.controllers', [])

controllers.controller('postListController', ($scope, Posts, MemberStats, HashtagStats) ->
    Posts.fetch ->
      $scope.posts = Posts.all()
      $scope.location_posts = Posts.location()
      MemberStats.fetch ->
        $scope.memberstats = MemberStats.all()
        $scope.teamstats = MemberStats.teams()
      HashtagStats.fetch ->
        $scope.hashtagstats = HashtagStats.counts()

    $scope.mapMovedCallback = (bounds) ->
      console.log 'You repositioned the map to:'
      console.log bounds
      return

    $scope.mapZoomedCallback = (bounds) ->
      console.log 'You zoomed the map to:'
      console.log bounds.getCenter().toString()
      return
)