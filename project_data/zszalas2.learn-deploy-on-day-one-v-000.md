# Your first deployment

There is no better way to feel like a developer than by actually becoming one, which you do by shipping code. With everything you've learned thus far, with think you're ready for the challenge. In this lab, you'll make a change to the Learn website: you will be asked to add your information to our public student directory (visible to the world at http://students.learn.co) and put in motion the sequence of events to have your change go live in production. 

We have already created a template, but you need to use your Git, HTML and CSS skills to submit an updated version of the site with your information. Here we go!

## Requirements

You'll need the following information about yourself:

* Name
* Blog Url (if you have one)
* Twitter URL
* LinkedIn URL
* Github URL
* Tagline
* Profile Picture (something normal, a headshot, of a good reusable size that can be easily cropped)
* Background Picture (like your cover picture from Twitter)
* Previous Work Experience
* Short Bio
* Education

## Structure

The structure of this project looks something like this:

```text
├── README.md
├── css
│   ├── css style sheets
├── assets
|   |__ img
|   |   ├── lots of images
|   |__ fonts
|   |   ├── some fonts
├── index.html
└── students
    └── student-name.html
    └── profile.html

```

### Files you will need to alter:
  * `index.html`
  * `css/styles.css`
  * `students/student-name.html`

## Getting Started

Fork and clone this lab.

#### Add your images

The first thing you'll need to do is add your image assets.

  * Add two pictures to the `assets/img` folder (they can be jpg or png files):
    * A cover picture (named `student-name-cover.jpg` or `student-name-cover.png`)
    * A profile picture (name `student-name.jpg` or `student-name.png`)

#### Add your Profile page

  1. Copy another students `student-name.html` file and rename it to your name. 
  2. Double-check that you added your cover and profile photo to the `img` directory
  3. Open up `your-name.html` and modify it with your information (links, bio etc).
     * Adding the images is a bit tricky! Take a look at the `css/styles.css` or use inspect element for an idea of where those images come from.

#### Add To The Index

  1. Open up `index.html`
  2. Copy one of the existing `div`s to make a new slot for you. Add in your information
  3. Re-use the profile image from your profile page and link to your profile page

#### Taking stock

Now that you have everything locally, let's take stock of what we have. Take a look at `index.html` and `profile.html` in the browser. To do this: 

* If you're working on a Mac, you can just find the file locally using Finder and click to view the webpage in Chrome. 
* If you're working on Nitrous, it's a bit more involved: first push your changes to your GitHub fork, then download your GitHub repo to your computer as a zip file, unzip it and open up the HTML files locally. 

You may need to cycle a few times until everything looks good. Once you're happy with it, you're ready to submit.

#### Submit!

  1. Easy, just submit a Pull Request back to us. We'll take a look ASAP and get your change merged and deployed.

## Deployment

Once we merge in your Pull Request, your profile will be viewable on [http://students.learn.co](http://students.learn.co), but we want you to be able to show all your friends your new website RIGHT NOW. Thankfully, GitHub makes this easy.

  1. Delete the `CNAME` file and commit that change. Reminder: you can delete a file with `rm CNAME`. Make sure you `git add .`, then `git commit -m "removing CNAME"`, then `git push`.
  2. Create a new branch called `gh-pages`. Reminder: you can do this with `git co -b gh-pages`
  3. Due to the process involved with forking, you will need to force push to GitHub. Force push `gh-pages` to GitHub. Reminder: after staging and commiting your changes, you can do this with `git push -f`
  4. Go to GitHub and go to the Settings for your repository (on the right side bar)
  5. Scroll down to the Github Pages Section. Take a look! You have a URL. For me (because my username is `jmburges`) it's http://jmburges.github.io/learn-deploy-on-day-one-1
