Resource
========

A <code>Resource</code> constructor for JS.

    var resource = Resource(url, options);

Creates an array-like object that loads and saves RESTfully to the
<code>url</code>, and stores and retrieves locally if <code>localforage</code>
is available.

### Dependencies

- <a href="http://jquery.com/">jQuery</a>
- <a href="https://github.com/cruncher/sparky">Sparky.Collection</a>
- <a href="https://github.com/mozilla/localForage">localforage</a> [optional,
fails silently without]

## Resource(url, options)

Creates a <code>resource</code>, an array-like object that stores model objects.

    var resource = Resource('/path/to/resource');

Pass in an options object to change the behaviour of <code>resource</code>.

    var resource = Resource('/path/to/resource', {
        index: 'uuid'
    });

The index is the name of the model property that <code>resource</code> appends to the
resource URL to form a URL for a model. By default <code>index</code> is <code>'id'</code>.
It is also the key used by <code>.find(id)</code> and various other methods to uniquely
identify models.


### resource methods

- .create(data)
- .add(object)
- .remove(id)
- .find(id)
- .validate(object)
- .get(property)
- .set(property, value)

###### events

- .on(name, fn)
- .off(name, fn)
- .trigger(name, args ... )

###### remote server

- .save()
- .load()
- .request(method)

###### local store

- .store()
- .retrieve()
- .storage(method)

### model methods

- .validate()
- .destroy()

###### remote server

- .save()
- .load()
- .request(method)

###### local store

- .store()
- .retrieve()
- .storage(method)

## resource methods

### .create(data)

Creates an object and stores it in <code>resource</code>.

    var item = resource.create({
        id: 42
    });

The <code>id</code> of the object is appended to <code>resource.url</code> when
server requests are made.

### .validate(object)

Checks that properties of <code>object</code> conform to this resource's
validation rules. To define validation rules, pass them in with property
descriptors when you create the resource:

    var resource = Resource(url, {
        properties: {
            username: {
                validate: 'required string'
            }
        }
    });

    resource.validate({});                        // false
    resource.validate({ username: 'sparky' });    // true

### .save()

Returns a promise that resolves to an array of objects in <code>resource</code>
that have been saved. Objects without an <code>id</code> are <code>PUT</code>,
while objects with are <code>PATCH</code>ed.

###### .save(id)

Sends a single object in <code>resource</code> to the server. Returns a promise
that resolves to an array containing that one object on successful response.

### .load()

###### .load(id)

Returns a promise that resolves to an array of objects in
<code>resource</code> that have been loaded from the server.

### .delete()

### .request(method, object)

Makes requests to the remote server. Returns a jQuery deferred (like a promise)
that represents the response. The resource is not updated and the objects in
resource are not changed. For that, use <code>.save()</code> and
<code>.load()</code>.

###### .request('get')

Get all objects from the sever.

    resource.request('get').then(function(array) {
        // Array contains all loaded objects.
    });

###### .request('put')

###### .request('patch')

###### .request('delete')

### .store()

Stores the resource locally. Returns a promise that resolves to an array of 
objects in <code>resource</code> that were sent to storage. Depends on the
<code>localforage</code> library, but fails silently without.

###### .store(id)

### .retrieve()

###### .retrieve(id)

Returns a promise that resolves to an array of all objects in
<code>resource</code> that have been retrieved from storage.

### .storage(method, object)

Stores and retrieves data from local storage. Depends on the
<code>localforage</code> library, but fails silently without.

Returns a promise that resolves to an array of all objects that have been
updated in storage. These are not the same objects that are in the resource.
The resource is not updated and the objects in resource are not changed.
To update the resource and get an array of objects that have been changed use
<code>.store()</code> and <code>.retrieve()</code>.

###### .storage('set')
###### .storage('set', object)

###### .storage('get')

Get all objects from storage.

    resource.storage('get').then(function(array) {
        // Array contains all retrieved objects.
    });

###### .storage('get', id)

Get a single object from storage.

    resource.storage('get', 42).then(function(array) {
        // The array contains the object with id 42 found in storage.
    });

###### .storage('remove')

###### .storage('remove', id)

### resource properties

###### .index <small>string</small>

Name of property to use as id

###### .properties <small>object</small>

An object containing properties to be defined on all objects created with
<code>resource.create()</code>.

## model methods

### .save()

Returns a promise that resolves to the updated model.

### .load()

Returns a promise that resolves to the loaded model.

### .delete()

### .request(method)

Makes requests to the remote server. Returns a jQuery deferred (like a promise)
that represents the response. The model is not updated.

### .store()

Stores the model locally. Returns a promise that resolves to the model.

### .retrieve()

Retrieves the model locally. Returns a promise that resolves to the updated model.

### .storage(method)

Stores and retrieves the model from local storage. Depends on the
<code>localforage</code> library, but fails silently without.

Returns a promise that resolves to data returned from storage.
