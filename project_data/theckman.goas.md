# Tideland Go Application Support

## Description

The *Tideland Go Application Support* (GOAS) is a collection of smaller 
helpful packages for multiple purposes. They are those little helpers we
always need. See their descriptions below.

## Installation

```
go get github.com/tideland/goas/v3/errors
go get github.com/tideland/goas/v2/identifier
go get github.com/tideland/goas/v2/logger
go get github.com/tideland/goas/v3/logger
go get github.com/tideland/goas/v2/loop
go get github.com/tideland/goas/v2/monitoring
go get github.com/tideland/goas/v1/scene
go get github.com/tideland/goas/v2/timex
go get github.com/tideland/goas/v1/version
```

## Usage

### Errors

Typical errors in Go are often created using `errors.New()` or `fmt.Errorf()`. Those
errors only contain a string as information. When trying to differentiate between
errors or to carry helpful payload own types are needed.

The errors package allows to easily create formatted errors with `errors.New()` or 
`errors.Annotate()` like with the `fmt.Errorf()` function, but also with an error code. 
This easily can be tested with `errors.IsError(err, code)`. 

[![GoDoc](https://godoc.org/github.com/tideland/goas/v3/errors?status.svg)](https://godoc.org/github.com/tideland/goas/v3/errors)

### Identifier

The identifier packge provides different ways to produce identifiers like UUIDs. The
UUID generation provides

- version 1 based on timestamp and MAC address,
- version 3 based on MD5 hash of namespace UUID and a value,
- version 4 based on random numbers, and
- version 5 based on SHA1 hash of namespace UUID and a value.

Other identifier types are based on passed data or types. Here the individual parts are 
harmonized and concatenated by the passed seperators. It is the users responsibility to 
check if the identifier is unique in its context.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v2/identifier?status.svg)](https://godoc.org/github.com/tideland/goas/v2/identifier)

### Logger

#### Version 2

This package helps to log with different levels and on different backends like on an
io.Writer or the Go logging. Own backends can be defined based on a simple interface.
Setting the level controls what will be logged. `Debugf()` and `Criticalf()` logging also 
print filename, function name and line number.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v2/logger?status.svg)](https://godoc.org/github.com/tideland/goas/v2/logger)

#### Version 3

Like version 2, but with new log level *Fatal*. After logging it directly ends the application
with a return code of -1 or with a panic. Own functions for the termination after `Fatalf()`
can be set too.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v3/logger?status.svg)](https://godoc.org/github.com/tideland/goas/v3/logger)

### Loop

A typical Go idiom for concurrent applications is running a loop in the background doing
a select on one or more channels. Stopping those loops or getting aware of internal errors
requires extra efforts. The loop package helps to manage this kind of goroutines.

The loop function, or method, looks like

```
func (f *Foo) backendLoop(l loop.Loop) error {
        select {
        case <-l.ShallStop():
                return nil
        case bar := <-f.barChan:
                ...
                if err != nil {
                        return err
                }
        case baz := <-f.bazChan:
                ...
                if err != nil {
                        return err
                }
        }
}
```

The loop is started with `l := loop.Go(f.backendLoop)`. Now the loop can be stopped with
`l.Stop()` which will return `nil` in case of no error or the error that has been returned
by the loop during message processing. The loop also can be killed with `l.Kill(err)` or
the status retrieved with `status, err := l.Error()`. The status is one of

- `loop.Running`,
- `loop.Stopping`, or 
- `loop.Stopped`.

Another variant is `loop.GoRecoverable(f.backendLoop, f.recoverFunc)`. Here a loop error
or the value of a recovering after a panic are passed to the recover function. It then
can decide if the loop shall be restarted or really terminated.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v2/loop?status.svg)](https://godoc.org/github.com/tideland/goas/v2/loop)

### Monitoring

The monitoring package supports three kinds of system monitoring. They are helpful to
understand what's happening inside a system during runtime. So execution times can be
measured and analyzed, stay-set indicators integrated and dynamic control value retrieval
provided.

```
etm := monitoring.BeginMeasuring("foo")
defer etm.EndMeasuring()

monitoring.SetVariable("bar", 4711)
monitoring.IncrVariable("bar")
monitoring.DecrVariable("bar")

monitoring.Register("baz", func() (string, error) { ... })
```

[![GoDoc](https://godoc.org/github.com/tideland/goas/v2/monitoring?status.svg)](https://godoc.org/github.com/tideland/goas/v2/monitoring)

### Scene

Scene provides a shared access to common used data in a larger context.

By definition a scene is a sequence of continuous action in a play,
movie, opera, or book. Applications do know these kind of scenes too,
especially in concurrent software. Here aspects of the action have to
passed between the actors in a secure way, very often they are interwoven
and depending.

Here the scene package helps. Beside a simple atomic way to store and
fetch information together with optional cleanup functions it handles
inactivity and absolute timeouts.

A scene without timeouts is started with

```
scn := scene.Start()
```

Now props can be stored, fetched, and disposed.

```
err := scn.Store("foo", myFoo)
foo, err := scn.Fetch("foo")
foo, err := scn.Dispose("foo")
```

It's also possible to cleanup if a prop is disposed or the whole
scene is stopped or aborted.

```
myCleanup := func(key string, prop interface{}) error {
        // Cleanup, e.g. return the prop into a pool
        // or close handles.
        ...
        return nil
}
err := scn.StoreClean("foo", myFoo, myCleanup)
```

The cleanup is called individually per prop when disposing it, when the
scene ends due to a timeout, or when it is stopped with `err := scn.Stop()`
or `scn.Abort(myError)`.

Another functionality of the scene is the signaling of a topic. So
multiple goroutines can wait for a signal with a topic, all will be
notified after the topic has been signaled. Additionally they can wait
with a timeout.

```
go func() {
        err := scn.WaitFlag("foo")
        ...
}()
go func() {
        err := scn.WaitFlagLimited("foo", 5 * time.Second)
        ...
}()
err := scn.Flag("foo")
```

In case a flag is already signaled wait immediatily returns. `Store()`
and `Flag()` can also be combined to `StoreAndFlag()`. This way the key
will be used as flag topic and a waiter knows that the information is
available.

A scene knows two different timeouts. The first is the time of inactivity,
the second is the absolute maximum time of a scene.

```
inactivityTimeout := 5 * time.Minutes
absoluteTimeout := 60 * time.Minutes
scn := scene.StartLimited(inactivityTimeout, absoluteTimeout)
```

Now the scene is stopped after 5 minutes without any access or at the
latest 60 minutes after the start. Both value may be zero if not needed.
So `scene.StartLimited(0, 0)` is the same as `scene.Start()`.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v1/scene?status.svg)](https://godoc.org/github.com/tideland/goas/v1/scene)

### Timex

The timex package supports the work with dates and times. Additionally it provides a
simple crontab.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v2/timex?status.svg)](https://godoc.org/github.com/tideland/goas/v2/timex)

### Version

The version package allows other packages to provide information about their version
and to compare it to other versions. It follows the idea of [semantic versioning](http://semver.org). 
Here given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when you make incompatible API changes,
- MINOR version when you add functionality in a backwards-compatible manner, and
- PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the 
MAJOR.MINOR.PATCH format.

[![GoDoc](https://godoc.org/github.com/tideland/goas/v1/version?status.svg)](https://godoc.org/github.com/tideland/goas/v1/version)

And now have fun. ;)

## Contributors

- Frank Mueller - <mue@tideland.biz>
- Benedikt Lang - <github@benediktlang.de>

## License

*Tideland Go Application Support* is distributed under the terms of the BSD 3-Clause license.
