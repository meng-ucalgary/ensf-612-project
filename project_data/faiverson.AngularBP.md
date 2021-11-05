# [AngularBP](https://github.com/faiverson/ngbp/tree/master) [![Build Status](https://api.travis-ci.org/ngbp/ngbp.png?branch=v0.0.1.release)](https://travis-ci.org/ngbp/ngbp)

An opinionated kickstarter for [AngularJS](http://angularjs.org) projects.

***

## Quick Start

Install Node.js and then:

```sh
$ git clone git://github.com/joshdmiller/ng-boilerplate
$ cd ng-boilerplate
$ sudo npm -g install grunt-cli karma bower
$ npm install
$ bower install
$ grunt watch
```

Finally, open `file:///path/to/ng-boilerplate/build/index.html` in your browser.

Happy hacking!

## Tools

[Twitter Bootstrap](http://getbootstrap.com),
[Angular UI](http://angular-ui.github.io),
[Angular Bootstrap](http://angular-ui.github.io/bootstrap),
[Font Awesome](http://fortawesome.github.com/Font-Awesome), and
[LESS](http://lesscss.org). Lastly, it contains a sophisticated
[Grunt](http://gruntjs.org)-based build system to ensure maximum productivity.

## Directory Structure

At a high level, the structure looks roughly like this:

```
root/
  |- grunt-tasks/
  |- karma/
  |- src/
  |  |- app/
  |  |  |- <app logic>
  |  |- assets/
  |  |  |- <static files>
  |  |- common/
  |  |  |- <reusable code>
  |  |- less/
  |  |  |- main.less
  |- vendor/
  |  |- angular-bootstrap/
  |  |- bootstrap/
  |  |- placeholders/
  |- .editorconfig
  |- .bowerrc
  |- bower.json
  |- build.config.js
  |- Gruntfile.js
  |- module.prefix
  |- module.suffix
  |- package.json
```

What follows is a brief description of each entry, but most directories contain
their own `README.md` file with additional documentation, so browse around to
learn more.
- `karma/` - test configuration.
- `src/` - our application sources. [Read more &raquo;](src/README.md)
- `vendor/` - third-party libraries. [Bower](http://bower.io) will install
  packages here. Anything added to this directory will need to be manually added
  to `build.config.js` and `karma/karma-unit.js` to be picked up by the build
  system.
- `.editorconfig` - To avoid indentation problems. You need to install a plugin [EditorConfig](http://editorconfig.org/)
- `.bowerrc` - the Bower configuration file. This tells Bower to install
  components into the `vendor/` directory.
- `bower.json` - this is our project configuration for Bower and it contains the
  list of Bower dependencies we need.
- `build.config.js` - our customizable build settings; see "The Build System"
  below.
- `Gruntfile.js` - our build script; see "The Build System" below.
- `module.prefix` and `module.suffix` - our compiled application script is
  wrapped in these, which by default are used to place the application inside a
  self-executing anonymous function to ensure no clashes with other libraries.
- `package.json` - metadata about the app, used by NPM and our build script. Our
  NPM dependencies are listed here.

### Considerations

In the future, should you want to add a new Bower package to your app, run the
`install` command:

```sh
$ bower install packagename --save-dev
```

The `--save-dev` flag tells Bower to add the package at its current version to
our project's `bower.js` file so should another developer download our
application (or we download it from a different computer), we can simply run the
`bower install` command as above and all our dependencies will be installed for
us. Neat!

When you're ready to push your app into production, just run the `compile`
command:

```sh
$ grunt compile
```

Lastly, a complete build is always available by simply running the default
task, which runs `build` and then `compile`:

```sh
$ grunt
```

### The Build System

The best way to learn about the build system is by familiarizing yourself with
Grunt and then reading through the heavily documented build script,
`Gruntfile.js`. But you don't need to do that to be very productive with
`AngularBP`. What follows in this section is a quick introduction to the
tasks provided and should be plenty to get you started.

The driver of the process is the `delta` multi-task, which watches for file
changes using `grunt-contrib-watch` and executes one of nine tasks when a file
changes:

* `delta:gruntfile` - When `Gruntfile.js` changes, this task runs the linter
  (`jshint`) on that one file and reloads the configuration.
* `delta:assets` - When any file within `src/assets/` changes, all asset files
  are copied to `build/assets/`.
* `delta:html` - When `src/index.html` changes, it is compiled as a Grunt
  template, so script names, etc., are dynamically replaced with the correct
  values configured dynamically by Grunt.
* `delta:less` - When any `*.less` file within `src/` changes, the
  `src/less/main.less` file is linted and copied into
  `build/assets/ng-boilerplate.css`.
* `delta:jssrc` - When any JavaScript file within `src/` that does not end in
  `.spec.js` changes, all JavaScript sources are linted, all unit tests are run,
  and the all source files are re-copied to `build/src`.
* `delta:coffeesrc` - When any `*.coffee` file in `src/` that doesn't match
  `*.spec.coffee` changes, the Coffee scripts are compiled independently into
  `build/src` in a structure mirroring where they were in `src/` so it's easy to
  locate problems. For example, the file
  `src/common/titleService/titleService.coffee` is compiled to
  `build/src/common/titleService/titleService.js`.
* `delta:tpls` - When any `*.tpl.html` file within `src/` changes, all templates
  are put into strings in a JavaScript file (technically two, one for
  `src/common/` and another for `src/app/`) that will add the template to
  AngularJS's
  [`$templateCache`](http://docs.angularjs.org/api/ng.$templateCache) so
  template files are part of the initial JavaScript payload and do not require
  any future XHR.  The template cache files are `build/template-app.js` and
  `build/template-common.js`.
* `delta:jsunit` - When any `*.spec.js` file in `src/` changes, the test files
  are linted and the unit tests are executed.
* `delta:coffeeunit` - When any `*.spec.coffee` file in `src/` changes, the test
  files are linted, compiled their tests executed.

As covered in the previous section, `grunt watch` will execute a full build
up-front and then run any of the aforementioned `delta:*` tasks as needed to
ensure the fastest possible build. So whenever you're working on your project,
start with:

```sh
$ grunt watch
```

And everything will be done automatically!

### Build vs. Compile

To make the build even faster, tasks are placed into two categories: build and
compile. The build tasks (like those we've been discussing) are the minimal
tasks required to run your app during development.

Compile tasks, however, get your app ready for production. The compile tasks
include concatenation, minification, compression, etc. These tasks take a little
bit longer to run and are not at all necessary for development so are not called
automatically during build or watch.

To initiate a full compile, you simply run the default task:

```sh
$ grunt
```

This will perform a build and then a compile. The compiled site - ready for
uploading to the server! - is located in `bin/`, taking a cue from
traditional software development. To test that your full site works as
expected, open the `bin/index.html` file in your browser. Voila!

### Live Reload!

`AngularBP` also includes [Live Reload](http://livereload.com/), so you no
longer have to refresh your page after making changes! You need a Live Reload
browser plugin for this:

- Chrome - [Chrome Webstore](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei)
- Firefox - [Download from Live Reload](http://download.livereload.com/2.0.8/LiveReload-2.0.8.xpi)
- Safari - [Download from Live Reload](http://download.livereload.com/2.0.9/LiveReload-2.0.9.safariextz)
- Internet Explorer - Surely you jest.

Note that if you're using the Chrome version with `file://` URLs (as is the
default with `AngularBP`) you need to tell Live Reload to allow it. Go to
`Menu -> Tools -> Extensions` and check the "Allow access to file URLs" box next
to the Live Reload plugin.

When you load your page, click the Live Reload icon in your toolbar and
everything should work magically. w00t!

If you'd prefer to not install a browser extension, then you must add the
following to the end of the `body` tag in `index.html`:

```html
<script src="http://localhost:35729/livereload.js"></script>
```