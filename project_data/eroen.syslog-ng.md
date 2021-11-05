[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/balabit/syslog-ng?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=body_badge)
[![Build Status](https://travis-ci.org/balabit/syslog-ng.svg?branch=master)](https://travis-ci.org/balabit/syslog-ng)
[![Build Status](https://drone.io/github.com/balabit/syslog-ng/status.png)](https://drone.io/github.com/balabit/syslog-ng/latest)

syslog-ng
=========

syslog-ng is an enhanced log daemon, supporting a wide range of input
and output methods: syslog, unstructured text, message queues,
databases (SQL and NoSQL alike) and more.

Quickstart
==========

The easiest configuration that accepts system logs on /dev/log (from
applications or forwarded by systemd) and writes everything to a single
file:

```
@version: 3.9
@include "scl.conf"

log {
	source { system(); };
	destination { file("/var/log/syslog"); };
};
```

This one also processes logs from the network (TCP/514 by default):

```
@version: 3.9
@include "scl.conf"

log {
	source {
		system();
		network();
	};
	destination { file("/var/log/syslog"); };
};
```
Structured/application logging, local submission via JSON, output in key=value format.

```
@version: 3.9
@include "scl.conf"

log {
	source { system(); };
	destination { file("/var/log/app.log" template("$(format-welf --subkeys .cim.)\n")); };
};
```

Here's how to submit a structured message using "logger":

```
$ logger '@cim: {"name1":"value1", "name2":"value2"}'
```

and the result will be:

```
name1=value1 name2=value2
```


Features
========
  * receive and send [RFC3164](https://tools.ietf.org/html/rfc3164)
    and [RFC5424](https://tools.ietf.org/html/rfc5424) style syslog
    messages
  * work with any kind of unstructured data
  * receive and send [JSON](http://json.org/) formatted messages
  * classify and structure logs with builtin parsers (csv-parser(),
    db-parser(), kv-parser(), ...)
  * normalize, crunch and process logs as they flow through the system
  * hand on messages for further processing using message queues (like
    [AMQP](http://www.amqp.org/)), files or databases (like
    [PostgreSQL](http://www.postgresql.org/) or
    [MongoDB](http://www.mongodb.org/)), and
  * forward log messages to big data tools like [Elasticsearch](https://www.elastic.co/),
    [Apache Kafka](http://kafka.apache.org/), or
    [Apache Hadoop](http://hadoop.apache.org/).

Performance:
  * syslog-ng provides performance levels comparable to a large
    cluster while running on a single node.
  * In the simplest use-case it scales up 600-800k messages per
    second.
  * But classification, parsing and filtering still produces several
    tens of thousands messages per second.

Community:
  * syslog-ng is developed by a community of volunteers, the best way to
    connect us is via our [github project page](http://github.com/balabit/syslog-ng)
    project, our [gitter channel](https://gitter.im/balabit/syslog-ng) or
    our [mailing list](https://lists.balabit.hu/mailman/listinfo/syslog-ng)
  * syslog-ng is integrated into almost all Linux distributions & BSDs, it
    is also incorporated into a number of products, see our [powered by
    syslog-ng] page for more details.

Sponsors:
  * [Balabit](http://www.balabit.com/) is the original creator and the
    largest current sponsor of the syslog-ng project, they provide support,
    professional services and addons you might be interested in.

Feedback
========

We are really interested in who uses our software, so if you do and you like
what you see, please tell us about it.  A simple "thanks" is also enough,
but learning about your usecase, experience, things to improve would be most
appreciated.

Just send an email to feedback (at) syslog-ng.org.

Should not take more than a minute, right?  Now go ahead. Please.

#FeedbackPowersOpenSource.

Installation from Source
========================

Releases and tarballs ready to compile are are made available at [GitHub][github-repo].

 [github-repo]: https://github.com/balabit/syslog-ng/releases

To compile from source, the usual drill applies (assuming you have
the required dependencies):

    $ ./configure && make && make install

Some of the functionality is compiled only in case the required
development libraries are present. The configure script displays a
summary of enabled features at the end of its run.
For details, see the [syslog-ng compiling instructions](https://www.balabit.com/sites/default/files/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/compiling-syslog-ng.html)


Installation from Binaries
==========================

Binaries are available in various Linux distributions and contributors
maintain packages of the latest and greatest syslog-ng version for
various OSes.

Debian/Ubuntu
-------------

Simply invoke the following command as root:

    # apt-get install syslog-ng

Latest versions of syslog-ng are available for a wide range of Debian
and Ubuntu releases and architectures from an
[unofficial repository](https://build.opensuse.org/project/show/home:laszlo_budai:syslog-ng).

 [madhouse-repo]: http://asylum.madhouse-project.org/projects/debian/

Fedora
------

syslog-ng is available as a Fedora package that you can install using
yum:

    # yum install syslog-ng

You can download packages for the latest versions from [here](https://copr.fedoraproject.org/coprs/czanik/).

Others
------

Binaries for other platforms are listed at the
official [third party page][3rd-party].

 [3rd-party]: https://syslog-ng.org/3rd-party-binaries/

Documentation
============

The documentation of the latest released version of syslog-ng Open Source Edition is available [here](https://www.balabit.com/sites/default/files/documents/syslog-ng-ose-latest-guides/en/syslog-ng-ose-guide-admin/html/index.html). For earlier versions, see the [Balabit Documentation Page](https://www.balabit.com/support/documentation). For ancient versions, see the [Balabit Documentation Archive](https://my.balabit.com/downloads/archived_documents).

Contributing
===========

If you want to modify the source of syslog-ng, for example, to correct a bug or develop a new module, the [syslog-ng gitbook](https://syslog-ng.gitbooks.io/getting-started/content/) helps you to take the first steps with the code base.
