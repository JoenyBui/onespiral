# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

* Reindexing
The final step, now that you have everything setup, is to put your data in from your database into the search index.
Haystack ships with a management command to make this process easy.

`
python manage.py rebuild_index
`

Using the standard SearchIndex, your search index content is only updated whenever you run either
`./manage.py update_index` or start afresh with `./manage.py rebuild_index`.

You should cron up a `./manage.py update_index` job at whatever interval works best for your site (using
--age=<num_hours> reduces the number of things to update).

Alternatively, if you have low traffic and/or your search engine can handle it, the RealtimeSignalProcessor
automatically handles updates/deletes for you.

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact