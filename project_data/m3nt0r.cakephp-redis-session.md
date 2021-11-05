
### ATTENTION: 

Actually it is easier to just use the **Redis PECL extension** and leave **CakePHP** `Session.save` at `php`, 
which is the default. Just install the extension with: 

```
sudo pecl install redis
```

Provided everything compiled fine, follow the instructions to load the extension and then 
just edit your `php.ini`.
 
```example
session.save_handler = redis
session.save_path = "tcp://192.168.0.1:6379"
```

Now restart your webserver and refresh your CakePHP app. It should work out of the box. 

To verify that it works you can use the `redis-cli`. When you are at the redis prompt 
type `monitor` and leave the window open. Refresh again and you should see the GET and 
SETEX calls managing the session.

That is the same thing this wrapper would do.

Hope this works for you.

----

# Redis Session Store for CakePHP

This class can be used in [CakePHP](http://cakephp.org) and saves 
session data into [Redis](http://redis.io), an open source key-value store.

## Installation

1. Place the ```redis_session.php``` into ```[yourapp]/config/```.
2. Open ```[yourapp]/config/core.php``` and find ```'Session.save'```.
3. Change the value of the Configure call so that it looks like this:

    ```Configure::write('Session.save', 'redis_session');```
    
That's it.

## Usage

### Redis on localhost

If you have a default Redis installation running on localhost you don't 
need to change anything. It will connect and take over. 

To confirm that it does indeed write to Redis you can use ```redis-cli monitor```
and refresh your browser. You should see some GET and SETEX calls.

### Redis on a foreign host

If you run on a different host you have to add two config settings 
in your ```core.php``` to setup the connection.

    Configure::write('RedisSession.hostname', 'some.host.name');
    Configure::write('RedisSession.port', 1337);
    
## About

I've ran the core component tests with this store enabled (CakePHP 1.3.10).

The class comes with [iRedis](https://github.com/dhorrigan/iRedis), a very
lightweight Redis Library by Dan Horrigan. The library is embedded inside
the source file, wrapped in a class_exists() condition. If you want to use
your own version make sure to include it early or just delete the iRedis
block. I leave that up to you. I wanted to keep this store small.

Garbage collection is handled by Redis. I use SETEX (expire) when writing
to the store. The key will delete itself when the session expires. You can
verify the remaining time with ```TTL [key]```. 

I have no complex key-namespacing going on. The key however is prefixed with
the session name ('Session.cookie' value) followed by the session_id() 

The cookie.path is hardcoded to '/' 

Enjoy!
