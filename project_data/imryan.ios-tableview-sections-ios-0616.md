# Tableview Sections

## Goals
   * Recognize UITableView as a display pattern and learn more about customizing it.
   * Learn how to implement sections (with headers) in a table view.
   * Stimulate thinking about how custom objects can be displayed using a tableview.

We've been working with tableviews, but so far we've only put out a unified list based off a single array. Let's get into sections as well as displaying custom objects.

## Instructions
   1. Open the project — there's already a blank tableview linked to a custom class set up for you.
   2. Make a `FISStudent` class with a public `NSArray` property called `favoriteThings`.
   3. In `FISTableViewController`, make an array property called `students`. 
   4. In your tableView controller's `viewDidLoad`, make some `FISStudent`s and give them all `name`s. Then fill in their `favoriteThings` properties with strings of their favorite things. No specific amount necessary, be creative or simply ask people around you! 
   5. Set these students to your TVcontroller's `students` property.
   6. Set up your tableView to match the following:     
      * each student should have their own section (*hint:* `numberOfSectionsInTableView:`)
      * set up `tableView:numberOfRowsInSection:` so that the rows in each section match that student's `favoriteThings`.
      * set your cell's `textLabel` to a favorite thing, and its `detailTextLabel` to its row index. 
   7. Cool, everyone's favorite things are listed, but theres no distinction between sections... implement `tableView:titleForHeaderInSection:`.
` using the student's `name` property.
   8. Houston, we have sections! But this is still kinda hard to read, it's just a big list of text after all. Implement `tableView:indentationLevelForRowAtIndexPath:` to clean it up a bit.
      
## Advanced
Add the following properties to your `FISStudent`:

   * `favoriteFood`
   * `favoriteColor`
   * `favoriteMusicalArtist`
   * `favoriteGame`

Set these for your student objects in your `viewDidLoad`. Now instead of using `favoriteThings` in your tableView data source, have it use these new properties to fill in the rows.

Then if you wanna make it real fancy, include the property name in the cell (eg "Food: Pizza" as opposed to "Pizza")

<p data-visibility='hidden'>View <a href='https://learn.co/lessons/ios-tableview-sections' title='Tableview Sections'>Tableview Sections</a> on Learn.co and start learning to code for free.</p>
