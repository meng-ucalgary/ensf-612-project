#grunt-bower-release
[![Build Status](https://travis-ci.org/caitp/grunt-bower-release.svg?branch=master)](https://travis-ci.org/caitp/grunt-bower-release) [![Dependency Status](https://david-dm.org/caitp/grunt-bower-release.svg?theme=shields.io)](https://david-dm.org/caitp/grunt-bower-release) [![devDependency Status](https://david-dm.org/caitp/grunt-bower-release/dev-status.svg?theme=shields.io)](https://david-dm.org/caitp/grunt-bower-release#info=devDependencies) [![Coverage Status](http://img.shields.io/coveralls/caitp/grunt-bower-release/master.svg)](https://coveralls.io/r/caitp/grunt-bower-release)
####Push tagged Bower package releases to endpoint

##Installation

Install npm package:

```bash
npm install grunt-bower-release --save-dev
```

Add the following to your project's `Gruntfile` in order to load the task:

```js
grunt.loadNpmTasks('grunt-bower-release');
```

##Usage

This task is intended primarily for packages which are targeted at both CommonJS ecosystems such as Node.js, as well as web browsers. As such, it is expected that a package.json is available in the source tree, and that we are releasing built assets intended for the browser. This is as opposed to maintaining a separate repository for this process.

In order to make use of this package, several things must be specified:

1. The files/folders to be added to the tagged release. These should be present in bower.json, as well.
2. The git endpoint to which the tagged release shall be sent.
3. The name of the tagged release.
4. The bower package name (will override setting in bower.json)

As such, a `Gruntfile` may contain the following:

```js
bowerRelease: {
  options: {
    main: 'library.min.js',
    dependencies: {
      'jquery': '~2.0.3'
    }
  },
  stable: {
    options: {
      endpoint: 'git://github.com/someone/some-package-bower-stable.git',
      packageName: 'some-package-stable.js',
      stageDir: 'staging-stable/'
    },
    files: [
      {
        expand: true,
        cwd: 'build/stable/',
        src: ['library.js', 'library.min.js', 'css/**/*.css'],
      }
    ]
  },
  devel: {
    options: {
      endpoint: 'git://github.com/someone/some-package-bower-devel.git',
      packageName: 'some-package-devel.js',
      stageDir: 'staging-devel/'
    },
    files: [
      {
        expand: true,
        cwd: 'build/devel/',
        src: ['library.js', 'library.min.js', 'css/**/*.css'],
      }
    ]
  }
}
```

This will enable the publishing of two builds: `stable`, and `devel`, via `bowerRelease:stable` and `bowerRelease:devel`, respectively. In both cases, `bowerRelease.options` are merged into `target.options`, which means that for both releases, we specify a `main` file 'library.min.js', and specify a bower dependency on `jquery#~2.0.3`. The dependencies will be added to the dependencies in the template `bower.json`, while the `main` files will replace those in the template, if any.

It's super simple stuff, and I hope some people might find it useful!

##Options

1. `endpoint` -- A bower endpoint. Currently, only git repositories are supported. Please contribute different endpoint types if you need them!
2. `packageName` -- The bower package name. This overrides `name` in `bower.json`
3. `stageDir` -- A staging directory where the repository is built and tagged.
4. `main` -- Enables the grunt task to override `bower.json`'s `main` parameter. This will be ignored if it is not a string or an array.
5. `dependencies` -- Enables the grunt task to add dependencies to a build.
6. `extendDependencies` -- If true, the dependencies from the source repository will be extended with the grunt options dependencies.
7. `branchName` -- (Optional) Specify the branch used for the endpoint.
8. ```overwriteTag``` -- (Optional) If true, a Git tag will be overwritten. The plug-in creates a Git tag in order to specify a package version for ```Bower```.
A tag name is derived from the ```version``` attribute in ```bower.json```. If you have already released a certain version of a package and attempt to do overwrite that version,
the plug-in will fail, because it won't be able to push the same tag twice. The option ensures that a tag is deleted, before it gets pushed again.
9. ```removeVersionTags``` -- (Optional) If true, all Git tags whose name starts with a value of ```version``` in ```bower.json``` will be removed.
10. ```suffixTagWithTimestamp``` -- (Optional) If true, a Git tag will be suffixed with ```+[CURRENT_TIMESTAMP]```, e.g. ```1.0.0-SNAPSHOT+849829134829```

## Files

Files must currently be specified per-task, which is unfortunate and will hopefully be fixed soon.

They may be specified as per the guidelines in [Configuring files](http://gruntjs.com/configuring-tasks#files)

## Releasing Snapshot Version

In some development environments developers prefer to have a snapshot version, which indicates a work in progress. The plug-in allows releasing snapshot versions.
All you have to do is to set ```removeVersionTags``` and ```suffixTagWithTimestamp``` to ```true```.
Those options will ensure that typing ```bower update``` will fetch a new version of a snapshot dependency without having to change ```bower.json``` or clean bower cache.

##License

The MIT License (MIT)

Copyright (c) 2013 Caitlin Potter and Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
