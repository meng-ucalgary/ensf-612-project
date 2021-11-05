# Create Action

So we have a form that can accept data and then print out the the values to the screen, which is great for learning how forms work in Rails. However, in a real life application we'll most likely want to add the data as a new record in the database. In the `CRUD` lifecycle, this is where the `C` comes in and we `create` a new record.

Before implementing this functionality, let's first open up a Rails console session and create a record manually:

```ruby
post = Post.new
post.title = "Title Goes Here"
post.description = "Desc goes here..."
post.save
```

This syntax will let you manually create a new `Post` record with a `title` and `description` attribute. After running the `save` method in the console you will see output similar to the following:

```shell
 (0.1ms)  begin transaction
SQL (0.3ms)  INSERT INTO "posts" ("title", "description", "created_at", "updated_at") VALUES (?, ?, ?, ?)  [["title", "Title Goes Here"], ["description", "Desc goes here..."], ["created_at", "2015-11-23 22:26:43.799742"], ["updated_at", "2015-11-23 22:26:43.799742"]]
 (1.2ms)  commit transaction
=> true

```

As you can see, the `save` method generates a SQL script that inserts a new record into the database, passing the `title` and `description` parameters into the statement and then returning the newly created `Post` object. At a high level, this is what the `create` method in our controller will be doing.

Open up the `posts_controller.rb` file. Let's do a few things to replicate the behavior we had in the console:

1. Create a new `Post` instance

2. Pass in the parameters from the form

3. Save the record

To build in this behavior, initially you can copy and paste the code that we ran in the console. The only key difference is that now we want to pull in the form data and have that populate the `title` and `description` attributes. You can access each of the form elements by using the hash syntax to grab the elements from the `params` hash that is submitted with the form. The new code in the `create` method should look something like this:

```ruby
def create
  post = Post.new
  post.title = params[:title]
  post.description = params[:description]
  post.save
end
```

If you go to `/posts/new` and fill out the form and submit it, you'll get the error shown below, but this is ok, Rails is simply complaining that we don't have a view template since by default it's trying to render a view template called `create.html.erb` that doesn't exist. Remember that Rails tries to map the controller action directly to a template, but in cases like `create` we wouldn't want to have a view template, it simply is communicating with the database.

![Missing Create Template Error](https://s3.amazonaws.com/flatiron-bucket/readme-lessons/template_error_create.png)

If you open up the console you will see that even though we ran into an error page the record was successfully created in the database, so the form and `create` action are working properly. How do you know if the record was successfully created? There are a couple of ways:

1. If you look at the record in the console by running `Post.last` it will show the record that was created and we can look at the `created_at` attribute to ensure the timestamp is current.
2. If you scroll up through the Rails server logs you can see that it prints out the SQL showing that the record was successfully created (example is below)

```shell
   (0.1ms)  begin transaction
  SQL (0.7ms)  INSERT INTO "posts" ("title", "description", "created_at", "updated_at") VALUES (?, ?, ?, ?)  [["title", "My Post"], ["description", "My desc"], ["created_at", "2015-12-26 18:00:31.393419"], ["updated_at", "2015-12-26 18:00:31.393419"]]
   (2.2ms)  commit transaction
```

To fix the error we simply need to redirect the user after they've filled out the form, let's do two refactors:

* Update the code with a redirect that leverages a route helper method

* Refactor the `post` variable to be an instance variable

The revised `create` method should look something like this:

```ruby
def create
  @post = Post.new
  @post.title = params[:title]
  @post.description = params[:description]
  @post.save
  redirect_to post_path(@post)
end
```

In this `create` action I'm following the standard convention of redirecting to the `show` page for the resource since it makes sense that you would want to see the completed record that was just created. With that being said, this page flow is completely up to you, and we could have had the `create` action redirect to the `index` action just as easily.

So everything is working and now users are able to create records in the database using the HTML form and  automatically be redirected to a `show` page where they can see the data that they entered in. There are a number of refactors that we will implement in the future, such as `strong parameters`, `error handling`, and tasks such as that, but we'll leave for a future lesson.

<p data-visibility='hidden'>View <a href='https://learn.co/lessons/rails-create-action-readme'>Create Action</a> on Learn.co and start learning to code for free.</p>
