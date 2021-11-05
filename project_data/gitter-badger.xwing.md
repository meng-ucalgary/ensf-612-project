(Yet Another) X-Wing Miniatures Squad Builder
=============================================

[![Build Status](https://travis-ci.org/geordanr/xwing.png)](https://travis-ci.org/geordanr/xwing)

What?
-----
This is a squad builder for Fantasy Flight Games' X-Wing Miniatures
game, completely in HTML and JavaScript.  No backend is necessary.
It can theoretically be dropped into any existing site, but since
it uses a lot of styling from [Twitter
Bootstrap](http://twitter.github.com/bootstrap/) it may require
some CSS trickery if you're using some other incompatible framework
(e.g. [Foundation](http://foundation.zurb.com)).

Can I save squads or share them on `$SOCIAL_NETWORK`?
-----------------------------------------------------
Saving: yes, if you provide a backend that adheres to the API.  See my [X-Wing Backend](https://github.com/geordanr/xwing-backend) project for an example.  Sharing, no.

Aren't there other squad builders out there already?
----------------------------------------------------
Yes.

So...?
------
I wanted a project to work on and screw around with stuff like HAML and Bootstrap and Select2, etc.

When will this be done?
-----------------------
It's an ongoing process.

Building
========

1. Install [Node.js](http://nodejs.org/) to get `npm`.
2. `sudo npm install -g grunt-cli` to install the global Grunt CLI.
3. `npm install` to install the dependencies listed in `package.json`.
4. `grunt` to build everything into the `app` directory.  The builder is at `app/index.html`.

Testing
=======

    npm test

Credits
-------
[X-Wing Miniatures](http://www.fantasyflightgames.com/edge_minisite.asp?eidm=174&enmi=X-Wing) is by [Fantasy Flight Games](http://www.fantasyflightgames.com/index.asp).
Icons and fonts originally from GeckoTH's excellent PSD, available [here](http://www.afewmaneuvers.com/topic/122-hi-res-photoshop-templates/).
X-Wing symbols and ships fonts courtesy [Hinny](https://github.com/Hinny) and [Josh Derksen](https://github.com/armoredgear7) and are available as a [Bower package](https://github.com/geordanr/xwing-miniatures-font).
Maneuver dial support by @hpanderson.
Fancy printout design inspired by TheKestrel on the FFG forums.
German translation by [failgod](https://github.com/failgod-marcus) and [strikegun](https://github.com/strikegun) from FFG Forums.
Spanish translation by [evil_wins Solo](http://boardgamegeek.com/user/sebaslocox) from BoardGameGeek forums and [negroscuro](https://github.com/negroscuro).
French translation by [pejuaxel](https://github.com/pejuaxel).
Polish translation by [Bober9000](https://github.com/Bober9000).
Upgrade card text integrated into printouts by [wffurr](https://github.com/wffurr).

I'm bad at keeping this up to date; see the About section of the builder.

CHANGELOG
=========

24 Nov 2014
-----------

* I'm terrible at updating this.
* [XWS](https://github.com/elistevens/xws-spec) support.

2 Oct 2014
----------
* Finally, support for tracking which expansions you own.

23 Apr 2014
-----------
* Add support for Epic play rules.  Squads saved in previous versions will not remember their game mode; re-saving them should fix it.

13 Apr 2014
-----------
* Spanish translations provided by [evil_wins Solo](http://boardgamegeek.com/user/sebaslocox) from BoardGameGeek forums.

2 Apr 2014
----------
* Maneuver dials are now displayed and are updated by upgrades!  Thanks to @hpanderson for the contribution.

29 Mar 2014
-----------
* Selecting Fancy or Simple now affects what kind of printout you get.

23 Mar 2014
-----------
* Add ship selector dropdown.  Pilot selector now only shows pilots for selected ship.

18 Mar 2014
-----------
* Add cards from Rebel Aces reveal.
* German translations for Imperial Aces provided by @failgod-marcus.

21 Feb 2014
-----------
* Add cards from Tantive IV reveal.
* Note: Limited is not supported, yet.  Fore and Aft parts of a ship are not linked, nor are required to both exist.
* Currently R2-D2 can exist both as Crew and as an Astromech. This will be resolved later.

17 Feb 2014
-----------
* Add desired/remaining points.

7 Feb 2014
----------
* Add cards revealed in Wave 4 preview.
* Sources are now properly sorted in the Card Browser.

1 Feb 2014
----------
* Add ships revealed in Rebel Transport preview.
* Add new icons from GeckoTH.

30 Nov 2013
-----------
* Add support for translations.
* Add German translations by @failgod-marcus.

8 Oct 2013
----------
* The simple version of View as Text returns!
* Sources for each card are now visible in the main builder.

4 Oct 2013
----------
* Add ability to clear current squad and start a new one.
* Add ability to clone non-unique pilots and their non-unique addons.

18 Sep 2013
-----------
* Add ships from _Imperial Aces_ unveil.
* Update serialization to support new title functionality in _Imperial Aces_.
* Display effective ship stats.

13 Sep 2013
-----------
* Fancy printout; design inspired by TheKestrel off the FFG forums.

8 Sep 2013
----------
* Finish Wave 3 ship integration.
* Add unique dots.
* Monkeypatch Select2 to stop focusing on the search input when on mobile.

29 May 2013
-----------
* Add card browser.
* Upgrade to Select2 3.4.0.

20 Apr 2013
-----------
* Add support for backend storage.

5 Jan 2013
----------
* Add fonts and more images from GeckoTH.

31 Dec 2012
-----------
* Add random squad builder.  Will attempt to generate a squad totalling the given number of points, stopping after a certain period of time or iterations.  May go over.  It's random.

30 Dec 2012
-----------
* Overhaul backend to be much less crappy.
* Add full support for Wave 2 ships (from what I can tell from what's been spoiled on [BoardGameGeek](http://boardgamegeek.com/).
* Switch from [Foundation](http://foundation.zurb.com) to [Twitter Bootstrap](http://twitter.github.com/bootstrap/).
* Switch from [Chosen](http://harvesthq.github.com/chosen/) to [Select2](http://ivaynberg.github.com/select2/).
* Now has a printer-friendly mode.
