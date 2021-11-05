Github Crawler
=============

Stage 1: Find all repositories
------------------------------
### Goal
Find all repositories using a certain library.
For this project, the libraries Objectify and Morphia have been chosen as targets.

All public repositories on Github are to be searched and filtered for the use of one of the specified libraries.
The libraries are being detected by the presence of certain keywords in the codebase of each repository.

### Approach
The keywords `"import com.googlecode.objectify"` and `"import org.mongodb.morphia"` have been chosen to identify all files
containing logic or annotations related to Objectify or Morphia.

The Github search API has various arbitrary limitations:

*   For each search term, only the first 1,000 results can be accessed.
*   Rate limit of 30 requests per minute when using the search API, respectively 10 per minute if not authenticated.
*   No more than 5 modifiers can be used per search clause.
*   All result sets are paginated into groups of 100 rows, each page counts as an individual query.
*   Code search via the API can only search inside a single repository.

Based on these limitations, a number of possible approaches have been identified:

*   Iterate over all known repositories and issue a code search query for each single repository.
    This approach has been ruled out as there is a total of far beyond 20 million repositories on Github which would have
    meant a runtime of more than a year per search term.
*   Use Google search with site scope to find all repositories containing specific keywords.
    Google could offer results for about every keyword, but apparently it had only indexed less than 10% of the repositories.
    This made this approach unreliable.
*   Use the web interface instead of the API, as the code search exposed via the web interface is not limited to a single repository.

The first 3 limitations of the API also apply to web interface.
In addition, the web interface will paginate the results, exposing only 10 rows at a time.

The limit of 1,000 results is a problem, since e.g. only for  "import com.googlecode.objectify" alone, there are over 20,000 relevant results from over 1,600 repositories.
Being limited to the first 1,000 of these results yielded less than 200 distinct repositories which isn't enough.

This limitation can be avoided by forming tautologies with auxiliary search terms.
Per default, the search function joins all terms with an implicit "AND" which does not count towards the modifier limit.
By splitting the query for clause `A` into the clauses `A B` and `A NOT B`, the size of the result set can be brought below the limit.

Multiple auxiliary terms need to be appended recursively in that way to be able to fetch the entire result set.
Due to the limit of 5 modifiers, the binary tree spanned by the call graph needs to be deliberately unbalanced towards the use of non-negated terms.

This is achieved by choosing mostly uncorrelated auxiliary terms with a high frequency, occurring in preferably at least 50% of all relevant documents.
The terms are sorted descending by frequency in order to avoid long chains of negations as far as possible.

### Performance
This approach allows to fetch results at a rate of roughly 100 results per minute.
For Objectify, this means that all 1,600 repositories, containing a total of 21,000 matching files, can be fetched in less than 6 hours.

The runtime is still unsatisfying, but as low as it gets considering the current limitations.

Stage 2: Download and filter sources
------------------------------------
### Goal
Find all sources related to the use of the libraries.
Each repository identified in the previous step needs to be processed.

For each relevant source, all revisions are stored individually in order to detect schema evolutions.

In addition to the sources, also a full commit history with timestamps is saved.

### Approach
The naive approach would have been to clone and save each individual repository locally, this however would have
required several hundred gigabytes of disk storage which would have to be accessed in later stages.

The chosen solution is to checkout the individual repositories to a RAM disk instead and only to store the relevant files.
This approach has the distinct advantage of fast processing speed, both during checkout and when restoring various file revisions.

The files are identified using the POSIX `grep` tool, relevant file revision are extracted using `git show`.

### Performance
For Objectify and Morphia, this approach allowed to distill over 400GB of sources into <4GB of relevant data within less than 20 minutes using only a dual core processor.

Even with a Gigabit Internet connection, a quad core would be sufficient to saturate the network bandwidth.

Stage 3: Parse and analyze
--------------------------
### Goal
Classify all sources and projects. For each project or file attribute of interest, provide a boolean predicate which can be queried for.


Of interest are:

*   Identification of used technology (Morphia, Objectify, etc.).
*   Identification of entity classes.
*   Use of lifecycle events in entities.
*   Use of migration related annotations in entities.
*   Schema evolutions, identified by tracking class attributes.
*   Generic statistics regarding activity.

### Approach
The clean approach would have been to parse the Java source code.

Performing a pure text search is sufficient to identify the use of annotations.
For each file identified in the previous stage, the latest revision is matched against the use of annotations.

Any file containing one of the following annotations is considered as using live cycle events:

-	`@OnLoad`
-	`@OnSave`
-	`@PrePersist`
-	`@PreSave`
-	`@PostPersist`
-	`@PreLoad`
-	`@PostLoad`

Any file containing one of the following annotations is considered as potentially performing lazy migration:

-	`@AlsoLoad`
-	`@NotSaved`
-	`@IgnoreLoad`
-	`@IgnoreSave`

A file importing from a package containing `objectify` in its name is classified as using Objectify.

A file importing from a package containing `morphia` in its name is classified as using Morphia.

A file containing a class annotated with `@Entity` is classified as containing an entity class.

A project is classified as using Objectify or Morphia when it contains a single entity using the corresponding framework.

For tracking evolutions, the set of class attributes is compared in between two following revisions each.
Each newly found and removed attribute is tracked, as well as all attributes where an annotation, type or default intializer has changed.

The summary of all projects is then stored in a single json file for further analysis.

### Performance
The data produced by this stage can be queried efficiently to perform statistical analysis.

The 4GB of source code from the previous stage are distilled into a compact database of <100MB.
The resulting database can easily be handled in memory.

### Output format
See [model.php](model.php) for the format of the generated `analysis.json` file.
This file contains an array of `Project` instances, describing each single analyzed project.

Summary
-------------------------------

Stage 1 and 2 are generic and can be adapted to a wide number of applications - only the queries need to be adapted in order match the files of interest.
The behavior of these stages is entirely controlled by the [config.ini](config.ini.dist) file in the same directory.

For stage 1, changes to the Github website may require to update the Xpatch queries accordingly.

Stage 3 is specific to the analysing Java projects for schema evolutions and only to a limited extent usable for other type of analysis.
