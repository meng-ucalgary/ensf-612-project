Introduction to Array.prototype.forEach
---

## Objectives

1. Explain why we use `forEach()`
2. Explain how `forEach()` works

## The weaknesses of `for` loops

Up until now, we've been doing our iterating with `for` loops. These are great for one-off tasks, and they're reasonably explicit: "I'm incrementing a variable, `i`, from `0` to `myArray.length - 1`, and using `i` to access the elements of the array."

``` javascript
var evens = [0, 2, 4, 6, 8, 10]

for (var i = 0, l = evens.length; i < l; i++) {
  console.log(`${evens[i]} is not odd!`)
}
```

But wouldn't it be nice if there were a way to access the elements directly, without having to type out `evens[i]`?

Well, it's our lucky day!

Follow along in `index.js` — you can run your code by copying it into your browser's console.

## `forEach()`

Every array comes with the method `forEach()` in JavaScript.

This method lets us iterate over every element of the array directly, without writing out a whole `for` loop. Let's rewrite the above example with `evens` using `forEach`:

``` javascript
var evens = [0, 2, 4, 6, 8, 10]

evens.forEach(even => {
  console.log(`${even} is not odd!`)
})
```

Whoa! It's so much shorter! Even though this is just a tiny piece of code, let's make sure we understand what's happening.

On the array `evens` we call the method `forEach` by typing `evens.forEach`. The `.` tells JavaScript that we're going to access some _property_ of the `evens` array. This property, `forEach`, happens to be a function, which, as we know, we call with parentheses around its arguments. `forEach` requires one argument, a function.

Whaaaaat? Did we read that right? We can pass a _function_ as an argument? You bet your boots we can!

That function, in turn, accepts up to three arguments: the current element in the array, the index of that element in the array, and the array itself.

Let's rewrite the function and step through it with the debugger to get a feel for its arguments.

``` javascript
evens.forEach((even, index, array) => {
  debugger
  console.log(`${even} is not odd!`)
})
```

(As a reminder, `debugger` is globally available and opens up the debug console in your browser when it's evaluated. Clicking the arrow will let you jump around and inspect the arguments to `forEach`'s function argument on as it iterates over the `evens` array.)

This is a _super_ powerful idea that makes it much easier for us to build programs that can do _many_ things. Instead of having to operate on each element using a `for` loop, we can instead very succinctly pass a function to `Array.prototype.forEach` and let the function do the work for us!

## Functions as Arguments

When a language allows functions to be used as arguments, we say that the language treats functions as **first-class objects**. Oftentimes, these functions server as **callbacks**, which do just what their name implies: they are _called back_, potentially with arguments, and do their work on bits of data that weren't available outside of the function.

For example, let's say that we have a function for logging the square of a number called, appropriately enough, `square`.

``` javascript
function square(n) {
  console.log(n * n)
}
```

If we wanted to square all of the elements of `evens`, we could just write `evens.forEach(square)`. We'll see the squares of `evens` printed to console.

But what if we don't know ahead of time what we want to do to our `evens` array? We can make our little program even more generic by wrapping it all up in a function that accepts a function (a callback) as an argument:

``` javascript
// no need to redeclare if you've declared this above
var evens = [0, 2, 4, 6, 8, 10]

function doToEvens(callback) {
  evens.forEach(callback)
}
```

Now we can pass _any_ function to `doToEvens`, and that function will be called on every element of `evens`!

Let's take it a step farther — what if we don't know beforehand what array we're going to be operating on? We can define a function that accepts two arguments: _any_ array and a callback for `forEach`:

``` javascript
function doToElementsInArray(array, callback) {
  array.forEach(callback)
}
```

Our code is short and sweet; but it's also generic and enormously powerful.

``` javascript
function changeCompletely(element, index, array) {
  array[index] = (Math.random() * 100).toString() + '!!!'
}

var animals = ["dog", "fish", "cat"]

doToElementsInArray(animals, changeCompletely)

// log out animals -- pretty cool, right?
console.log(animals)
```

If you've been following along in `index.js`, you should now be able to run `learn submit` — all of the tests should pass!

## Resources

- [`Array.prototype.forEach()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
