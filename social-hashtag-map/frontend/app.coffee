app = angular.module('pollApp', ['ui.router','pollApp.controllers','pollApp.services'])

app.config(($interpolateProvider, $stateProvider, $urlRouterProvider) ->
    #Play nice with django's template
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
    #Default to question list
    $urlRouterProvider.otherwise('/');

    $stateProvider
        .state('tweetList'
            url: '/'
            templateUrl: 'tweetList'
            controller: 'tweetListController'
            resolve:
                tweets : (Tweets)->
                    Tweets.fetch()
                    return Tweets.data()
        )
)


app.config(($httpProvider) ->
    getCookie = (name) ->
        for cookie in document.cookie.split ';' when cookie and name is (cookie.trim().split '=')[0]
            return decodeURIComponent cookie.trim()[(1 + name.length)...]
        null
    # Add Header to comply with Django's CSRF implementation
    $httpProvider.defaults.headers.common['X-CSRFToken'] = getCookie("csrftoken")
)
