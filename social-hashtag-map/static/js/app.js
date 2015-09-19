(function() {
  var app;

  app = angular.module('pollApp', ['ui.router', 'pollApp.controllers', 'pollApp.services', 'angular-mapbox']);

  app.run(function(mapboxService) {
    return mapboxService.init({
      accessToken: 'pk.eyJ1IjoibWF0dG1hcnR6IiwiYSI6IjQyOTRjNTBhOTFkNWM2OTZmOTQ4MWY5Yzg0OGJjNmY3In0.jtyfGzQVVy7Z71fblxlg0w'
    });
  });

  app.config(function($interpolateProvider, $stateProvider, $urlRouterProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $urlRouterProvider.otherwise('/');
    return $stateProvider.state('tweetList', {
      url: '/',
      controller: 'postListController'
    });
  });

  app.config(function($httpProvider) {
    var getCookie;
    getCookie = function(name) {
      var cookie, _i, _len, _ref;
      _ref = document.cookie.split(';');
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        cookie = _ref[_i];
        if (cookie && name === (cookie.trim().split('='))[0]) {
          return decodeURIComponent(cookie.trim().slice(1 + name.length));
        }
      }
      return null;
    };
    return $httpProvider.defaults.headers.common['X-CSRFToken'] = getCookie("csrftoken");
  });

}).call(this);
