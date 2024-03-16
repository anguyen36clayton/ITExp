<p align="center"><strong>Github Scripts and Commands</strong></p>

**Legend:**
```
$ - denotes a command
# - denotes a comment
```

**Login Github from git bash**
```
The account name is the account.
The password is the PAT (Personal Access Token), not the account's password.

```

**How to Clone into PC**
- Open the repository, click on <> Code, then copy the link in HTTPS.
$git clone HTTPS #HTTPS is the link of the repository.

**Add item/items to github**
```
$git add . OR $git add file.extension #Stage item/items 
$git commit -m "Add comment here"
$git push
```

**Create a new Branch and track it on the website**
```
$git checkout -b new_branch_name #Create a new branch
$git checkout branch_name #Check out the branch
$git push -u origin new_branch_name #To track it on github website
$git branch --set-upstream-to=origin/main main #To push to main instead of new branch
```

**Files**
```
Git Pull: 
1. CD into a specific directory and pull. Also keeps the command prompt opened after executing commands.
```

**Formatting README Files:**
```
markdown
Center and Bold Text
\```
<p align="center"><strong>Your Heading</strong></p>
\```

Bold String
\**Bold**

Code Block
\``` 
Text Here
\```


```
