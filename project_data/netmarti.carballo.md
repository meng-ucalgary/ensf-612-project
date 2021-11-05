Carballo Chess Engine
=====================

Carballo (the galician word for Oak, it's all about search trees) is an Open Source Java chess engine with two interfaces:

* UCI: a text interface for chess GUIs like Arena: https://github.com/albertoruibal/carballo/raw/master/carballo-uci-1.2.tgz
* HTML5: developed with Google Web Toolkit (GWT) using the Vectomatic SVG library: http://www.mobialia.com/webchessgwt

It is organized into modules:

* Core: the chess engine
* Jse: the Java Standard Edition version with the UCI interface and JUnit tests
* Gwt: components needed for the GWT GUI
* GwtGui: an HTML5 interface developed by Lukas Laag, it depends on Core and Gwt
* Applet: the applet code (deprecated), it depends on Core and Jse

The Core and the UCI interface are converted to C# in the project http://github.com/albertoruibal/carballo_cs

It is licensed under GPLv3 and the source code is hosted at https://github.com/albertoruibal/carballo.
You are free to use, distribute or modify the code, we ask for a mention to the original authors and/or a link to our pages.

Features
========

* UCI interface for chess GUIs like Arena
* It includes a great GWT interface by Lukas Laag and a deprecated Java Applet GUI
* Based on bitboards with a magic bitboard move generator, it also includes code for magic number generation
* Move iterator sorting moves with four killer move slots, SEE, MVV/LVA and history heuristic
* PVS searcher
* Aspiration window, moves only one border of the window if falls out
* Transposition Table (TT) with zobrist keys (it uses two zobrist keys per board to avoid collisions) and multiprobe
* Quiescent Search (QS) with only good or equal captures (according to SEE) and limited check generation
* Internal Iterative Deepening to improve sorting
* Extensions: Check, pawn push and passed pawns and mate threat
* Reductions: Late Move Reductions (LMR)
* Pruning: Null move Pruning, static null move pruning, futility pruning and aggressive futility pruning
* Pluggable evaluator function, distinct functions provided: the Simplified Evaluator Function, other Complete and other Experimental
* Parameterizable evaluator (only for the complete &amp; experimental evaluators)
* Polyglot opening book support; in the code it includes Fruit's Small Book
* FEN notation import/export support, also EPD support for testing
* JUnit used for testing, multiple test suites provided (Perft, BS2830, BT2630, LCTII, WAC, etc.)

Test results in my Intel Core i7-3667U CPU @ 2.00GHz:

* WinAtChess: 287 positions of 300 (1 second each)
* SilentButDeadly: 89 positions solved of 134 (5 seconds each)
* Arasan: 22 positions of 250 (60 seconds each)

His real strength is about 2400 ELO points, you can check his tournament rankings at http://www.computerchess.org.uk/ccrl/

Authors
=======

* Alberto Alonso Ruibal: http://www.alonsoruibal.com
* Lukas Laag, developer of a great GWT SVG library (http://www.vectomatic.org) and the Carballo GWT interface

Building
========

Carballo uses the Gradle build system, you need to install Gradle from http://www.gradle.org

Build all the jars and install them to your local Maven repository:
```
gradle install
```
Build the UCI interface:
```
cd jse
gradle proguard
```
Build the GWT interface:
```
cd gwtgui
gradle compileGwt
```

Testing
=======

Run fast tests:
```
gradle fastTest
```
Run Win at Chess tests:
```
cd jse
gradle -Dtest.single=WinAtChessTest cleanTest test
```
Run Silent but Deadly tests:
```
cd jse
gradle -Dtest.single=SilentButDeadlyTest cleanTest test
```

History
=======

Version 1.2: A new MoveIterator, Chess960 and lots of UCI improvements

* New MoveIterator that generates only legal moves with a check flag set
* Added support for Chess960 (Fischer Random Chess)
* Implemented UCI Ponder
* New replace strategy for the TT, taking into account the entry depth and the generation difference
* In the TT in QS, store the entries with checks generated with depth 1 and entries without checks with depth 0
* Four killer move slots
* Set default razoring margin to 400
* Fix the futility in QS and set the default futility in QS to 80
* Remove the null move margin and improve the null move reduction calculation
* Remove the recapture extension
* New time management strategy adding a "panic time" when the search in the root node fails low by a margin of 100
* Do not penalize pinned pawns in the evaluators, multiply the hung pieces bonus by the number of hung pieces, and pawn center opening corrections
* Fixed a bug multiplying the opening/ending values in the evaluators by negative factors
* Generate piece-square values in different classes
* Fixed an important bug in the SWAP algorithm for the SSE evaluation
* Now it uses 1" for the WinAtChess tests

Version 1.1: Urgent bug fix for 1.0

* The UCI interface was ignoring all the UCI options
* Do not allocate memory inside ExperimentalEvaluator.evaluate()
* Added the new pawn and endgame logic to the CompleteEvaluator (ExperimentalEvaluator continues as the default)

Version 1.0: Lots of fixes, small advances in test results: 294 in WAC (5") and 2520 in BT2630.

* New Transposition Table with a separated slot for the eval values
* Now uses the TT in quiescence search
* Fix mate values before inserting them in the TT, now the mate problems are solved with the right distance to the mate
* Fixes to futility pruning in quiescence search
* New pawn classification in the ExperimentalEvaluator
* Now the PV line is shown every time that a move is found in the root node
* Implemented UCI seldepth, lowerbound, upperbound and hashfull
* Implemented the depth and nodae limit for the search
* Enabled the endgame knowledge
* In the search, assume that pawn pushes are to the 6th, 7th or 8th rank
* Extend only checks with positive SSE
* Disable by default the recapture and pawn extensions, set the mate threat extension to one full PLY
* Fix recapture extension (now disabled by default)
* Tests migrated to the JUnit 4 format with annotations, and created a "fastTest" gradle task to run only the fast tests
* C# code separated in another GitHub project

Version 0.9: Fixes evaluator bugs

* Reordered some logic in the ExperimentalEvaluator
* Fixed a bug in the detection of the 2 bishop bonus
* Fixed another bug in the detection of candidate passer pawns
* Bug in the detection of the adjacent columns found by Yonathan Maalo
* Some improvements in the HTML5 interface

Version 0.8: Build system and GWT modifications

* Project build system migrated from Maven to Gradle
* Solved some evaluator bugs
* New option to do not use Magic Bitboard Attacks: optimizes start time in HTML5
* Removed specific Bitboard attacks code from GWT, can be simulated setting BitboardAttacks.USE_MAGIC = false
* New ArrayBufferBook for GWT, it can process any opening book loaded as a JS ArrayBuffer

Version 0.7: A small leap on the engine performance and a big code clean

* Code moved to Github
* Integrated ROOT, PV and NULL nodes search routine
* Activated singular movement extensions and changed default singular extension margin
* Do null move only when the remaining depth is > 3 PLY
* No not overwrite the value in the TT if there is no room
* Converted code to C# using sharpen. At the moment only the core of the engine
* Solved a big bug getting the move from the transposition table
* Also found another bug on the search getting the last captured piece value
* And the complete evaluator had a bug calculating the attacks value

Version 0.6: Source code reorganization, GWT and PGN improvements, no changes on the engine code

* Code splitted in carballo-core, carballo-jse and carballo-applet
* Carballo-core is GWT-friendly
* Integrated SAN notation on Board class
* Improved PGN export with SAN notation
* Added a GWT interface based on the one by Lukas Laag (http://vectomatic.org) code

Version 0.5: Improves about 150 ELO points over Carballo 0.4

* PVS searcher: SearchEngine completely changed
* Futility pruning now works!
* New TT algorithm, now also uses TT to store evaluation values
* Bug with draw detection with 3-fold repetition
* Bug with time management on tournament, was using the opponent's time amount
* Bug with history table overflow

Version 0.4: First version integrated with Mobialia Chess

* Parametrizable evaluator
* Evaluator changes