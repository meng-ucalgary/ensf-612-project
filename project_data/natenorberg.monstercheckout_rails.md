MONSTER Checkout
================

[![Build Status](https://travis-ci.org/natenorberg/monstercheckout_rails.svg?branch=master)](https://travis-ci.org/natenorberg/monstercheckout_rails) [![Code Climate](https://codeclimate.com/github/natenorberg/monstercheckout_rails/badges/gpa.svg)](https://codeclimate.com/github/natenorberg/monstercheckout_rails) [![Test Coverage](https://codeclimate.com/github/natenorberg/monstercheckout_rails/badges/coverage.svg)](https://codeclimate.com/github/natenorberg/monstercheckout_rails/coverage)

MONSTER Checkout is an interdisciplinary project created by Nate Norberg, Brian Maher, and Joe Sweeney to simplify the checkout process for the Montana State University Music Technology program.

The old checkout system was simple and easy to follow, but it used a lot of paper. The new system follows the same procedure but you can use it anywhere. You only need to come to the building to check equipment in and out.

##Status

The [initial version](https://github.com/natenorberg/monstercheckout) of the product was finished in May 2014. Due to difficulties finding a place to host a Django app for free, and because we wanted to play around with some new technology, this project is a re-write using Ruby on Rails. You can see a preview of this site in a production environment [here](http://damp-badlands-1212.herokuapp.com). There is a good chance that this product will later migrate to [Laravel](http://laravel.com) so that it can be hosted on a LAMP server at MSU.

##Technology Used

The original app was created in Python with the [Django](https://www.djangoproject.com) framework. In order to make it easier to test and deploy, and to incorporate more things we've learned since we started, this site was built with [Ruby on Rails](http://rubyonrails.org), plus some other goodies like [Bootstrap](http://getbootstrap.com), [FontAwesome](http://fontawesome.io), and [AngularJS](https://angularjs.org).

##Release information

###1.0
The original release will be when the rails version of the product reaches feature parity with the Django app

###1.1
This release contains some non-essential but helpful features. Email notifications is the biggest feature, but it also includes things like the ability for an admin to provide a reason why a reservation was denied and other simple features that were easy to implement but no one knew we'd want them until after it started being used.

###1.2
Added a couple nice to have features, such as categories for equipment
and search lookahead

###2.0 (not really started)
Eventually, the product should be enhanced by replacing a few of the static pages (such as the lab monitor views) with AngularJS apps. I might just use this along with the ionic framework to create a mobile app while I'm at it
