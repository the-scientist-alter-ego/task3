# tinyURL
- mkdir task-3
- cd task-3/
- git init
- git add README.md
- git commit -m 'add README'
- git branch -M main     (rename M)
- git remote add origin https://github.com/the-scientist-alter-ego/task3.git
- git push -u origin main

- git add .
- git commit -m 'update README'
- git push -u origin main
ERROR
- git pull
Conflict shown in README.md, fixed manually
- git add .
- git commit -m 'resolved README conflict'
- git push -u origin main
SUCCESS resolve README.md
- git checkout -b new-feature
create FEATURE.md
?????????? ERROR    我懂了！！！！
- git add .
- git commit -m 'add FEATURE.md in new-feature'
- git push -u origin main
main has nothing to update
- git push -u origin new-feature
MERGE on github, issue closed
- git checkout main
- git pull

- git checkout -b bug-1
- git checkout -b bug-2
- git checkout bug-1
- git add BUG-1.md
- git commit -m 'on bug1'
'MZ' in bug1 saved but not added & commited
- git stash (before going to bug2)
- git checkout bug-2
bug2
- git add BUG-2.md
- git commit -m 'fixed bug2'
- git checkout bug-1
- git stash pop
- git add BUG-1.md
- git commit -m 'fixed bug1'
- git checkout main
- git branch
