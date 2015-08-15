module.exports = (grunt) ->
    grunt.initConfig
        pkg: grunt.file.readJSON('package.json')
        watch:
            coffeescript:
                files: ['social-hashtag-map/frontend/**/*.coffee']
                tasks: ['coffee:compile']
        coffee:
            compile:
                expand: true
                cwd: 'social-hashtag-map/frontend/'
                src: ['**/*.coffee']
                dest: 'social-hashtag-map/static/js/'
                ext: '.js'



    grunt.loadNpmTasks('grunt-contrib-coffee')
    grunt.loadNpmTasks('grunt-contrib-watch')
