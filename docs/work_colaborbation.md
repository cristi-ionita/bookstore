# Work collaboration
## How to create branch
```
git checkout -b type_of_work/ID-NUMBER/short_title_to_represent_idea_of_change
```

Types of work:
* feature
* bugfix
* hotfix
* documentation
* tech_debt

Id and number should be id of project and number of ticket:
* BS-1: - Book Store, first task in jira and (BS-1, BS-2 etc.)

```feature/BS-2/add_possibility_to_create_users```

## How to commit changes

To be able find anything in git history we should keep our commits strict and clear.
```git commit -am "message of commit"``` such commit is good but not enough details for anyone (even for author)

1. Every commit should be multiline. It should contains title and details as non numeric list
2. Commit title should contains id of ticket too

BS-1: create basic structure for fast api application

* add configuration file
* add core folder for basic common logic
* add docker file and dockr compose
* ...

Such multiline commit could be added in several different ways:
* by means of GUI of IDE (Pycharm of VS Code contains tons of plugins to work with git and create multiline commit)
* manually from console:
  ```
  git commit -am "BS-1: it is title of commit" -am "* this is first item from the list"
  ```

[back](../README.md)