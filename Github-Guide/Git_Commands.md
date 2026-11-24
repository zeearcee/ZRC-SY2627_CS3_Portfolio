# Git & GitHub Student Guide

## A Step-by-Step Guide: From Initial Setup to Pushing Your Code

This guide introduces the Git commands students commonly need when
working on programming activities and submitting code through GitHub.
Follow the steps in order the first time you use Git. After your initial
setup, use the **Daily Student Workflow** for succeeding activities.

------------------------------------------------------------------------

## 1. Git vs. GitHub

-   **Git** is a version control system. It records changes to files and
    helps you manage different versions of your work.
-   **GitHub** is an online platform where Git repositories can be
    stored, shared, and collaborated on.

**Simple way to remember:** Git manages your code history on your
computer; GitHub hosts a copy of your repository online.

## 2. Install and Verify Git

1.  Download Git from <https://git-scm.com/downloads>.
2.  Install Git using the recommended/default options.
3.  Open **Git Bash** (Windows) or Terminal (macOS/Linux).
4.  Check whether Git is installed:

``` bash
git --version
```

If Git is installed, a version number will appear.

## 3. Configure Git for the First Time

Set the name and email address that Git will associate with your
commits. Use the name and email you intend to use for your
schoolwork/GitHub account.

``` bash
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"
```

Check your configuration:

``` bash
git config --global --list
```

Useful configuration commands:

``` bash
# Set the default initial branch name to main
git config --global init.defaultBranch main

# View one setting
git config user.name
git config user.email
```

> **Important:** The name and email in Git configuration identify the
> author of commits. They do not log you in to GitHub.

## 4. Create or Prepare a GitHub Repository

1.  Sign in to <https://github.com>.
2.  Select **New repository**.
3.  Enter a repository name, such as `CS-Programming-Activities`.
4.  Add a short description if required.
5.  Choose **Public** or **Private** according to your teacher's
    instructions.
6.  If you are following the command-line setup below, create the
    repository without a README, `.gitignore`, or license to keep the
    first push straightforward.
7.  Select **Create repository**.
8.  Copy the repository URL. It normally looks like:

``` text
https://github.com/your-username/your-repository.git
```

Keep the repository URL available. You will use it when connecting your
local project to GitHub.

## 5. Open the Correct Project Folder

Before running Git commands, make sure the terminal is inside the folder
containing your project.

``` bash
# Display the current folder
pwd

# List files and folders
ls
```

On Windows Command Prompt, use:

``` cmd
cd
dir
```

Change to your project folder. Example:

``` bash
cd Documents/CS-Programming-Activities
```

**Tip:** In many file managers, you can open the project folder,
right-click, and choose **Open Git Bash here** or **Open in Terminal**.

## 6. Initialize a Local Git Repository

Use this step if you already have a project folder on your computer and
it is **not yet** a Git repository.

``` bash
git init
```

This creates a hidden `.git` directory that stores the repository's
version history.

Check the repository status:

``` bash
git status
```

You should see the current branch and the files Git has detected.

> Do not run `git init` repeatedly in an already initialized project. If
> the folder is already a Git repository, continue with `git status`.

## 7. Stage and Commit Your First Files

Git uses three important areas:

1.  **Working directory** -- the files you create or edit.
2.  **Staging area** -- changes selected for the next commit.
3.  **Repository history** -- committed snapshots of your work.

### 7.1 Review your files

``` bash
git status
```

### 7.2 Stage files

Stage all changes in the current project:

``` bash
git add .
```

Or stage only one file:

``` bash
git add Activity1.py
```

### 7.3 Review what is staged

``` bash
git status
git diff --cached
```

### 7.4 Commit the staged changes

``` bash
git commit -m "Add Activity 1"
```

A **commit** is a saved checkpoint in your project's history. Write a
short message that describes the changes.

Examples:

``` bash
git commit -m "Add Activity 2 solution"
git commit -m "Fix input validation"
git commit -m "Update project documentation"
```

## 8. Connect Your Local Repository to GitHub

If you created an empty GitHub repository in Step 4, connect it to your
local repository:

``` bash
git remote add origin https://github.com/your-username/your-repository.git
```

Replace the sample URL with your actual repository URL.

Check the remote connection:

``` bash
git remote -v
```

The remote named `origin` should display your GitHub repository URL.

### If `origin` already exists

Do not add it again. Check its URL:

``` bash
git remote -v
```

If the URL is incorrect, update it:

``` bash
git remote set-url origin https://github.com/your-username/your-repository.git
```

## 9. Check and Change Branches

A **branch** is a separate line of development. The usual default branch
is `main`. You can create another branch to work on a feature or
activity without directly changing `main`.

### 9.1 See your current branch

``` bash
git branch
```

The branch with an asterisk (`*`) is your current branch.

You can also use:

``` bash
git status
```

### 9.2 Create a new branch

``` bash
git branch activity-1
```

This creates a branch but does not switch to it.

### 9.3 Switch to an existing branch

``` bash
git switch activity-1
```

### 9.4 Create and switch to a new branch in one command

``` bash
git switch -c activity-1
```

### 9.5 Return to the main branch

``` bash
git switch main
```

### 9.6 List local branches

``` bash
git branch
```

### Older equivalent commands

You may encounter these older commands in tutorials:

``` bash
git checkout activity-1       # Switch to an existing branch
git checkout -b activity-1    # Create and switch to a new branch
```

For new work, `git switch` is generally easier to understand.

## 10. Push Your Code to GitHub

**Push** means uploading your local commits to the remote repository on
GitHub.

### 10.1 First push of the `main` branch

If your current branch is `main`, use:

``` bash
git push -u origin main
```

The `-u` option sets the upstream connection. After this is configured,
you can usually push future commits on that branch using:

``` bash
git push
```

### 10.2 First push of a new branch

If you are working on `activity-1`, use:

``` bash
git push -u origin activity-1
```

After the first push on that branch, use:

``` bash
git push
```

### 10.3 Push later updates

After editing your files, stage, commit, and push:

``` bash
git add .
git commit -m "Update Activity 1"
git push
```

**Remember:** `git add` stages changes, `git commit` saves them locally,
and `git push` uploads committed changes to GitHub. Running `git push`
alone will not upload uncommitted edits.

## 11. Get the Latest Changes from GitHub

Before working with a shared repository, check whether other changes
have been pushed.

``` bash
git pull
```

For a specific branch:

``` bash
git pull origin main
```

`git pull` downloads and integrates remote changes into your current
branch. Make sure you are on the intended branch before pulling.

A useful sequence before starting work is:

``` bash
git switch main
git pull origin main
```

If your teacher or team uses a different branch, use the branch
specified for your task.

## 12. Merge a Branch into Another Branch

Merging combines the changes from one branch into the branch you are
currently on.

Example: merge `activity-1` into `main`.

``` bash
# Move to the branch that will receive the changes
git switch main

# Get the latest main branch
git pull origin main

# Merge activity-1 into main
git merge activity-1
```

If the merge is successful, Git records the combined result. You may
then push the updated `main` branch:

``` bash
git push origin main
```

> Only merge branches when your teacher or team workflow requires it. If
> you are instructed to submit work on a separate branch, push that
> branch instead of merging it into `main`.

## 13. Daily Student Workflow

Use this routine whenever you continue working on an existing Git
project.

### Before editing

``` bash
git status
git branch
git pull
```

### After editing your code

``` bash
# Stage your changes
git add .

# Review staged changes
git status

# Save a commit
git commit -m "Complete Activity 1"

# Upload your commit to GitHub
git push
```

### Complete example

``` bash
cd Documents/CS-Programming-Activities
git switch main
git pull origin main
git status

# Edit your Python files, then:

git add .
git commit -m "Complete Activity 1"
git push
```

## 14. Clone an Existing GitHub Repository

Use `git clone` when the repository already exists on GitHub and you
want to download a local copy. **Do not initialize a second repository
with `git init` after cloning.**

1.  Open the repository on GitHub.
2.  Select **Code**.
3.  Copy the HTTPS URL.
4.  Open Git Bash or Terminal.
5.  Navigate to the folder where you want the project saved.
6.  Run:

``` bash
git clone https://github.com/your-username/your-repository.git
```

7.  Enter the downloaded project folder:

``` bash
cd your-repository
```

8.  Check the status and remote:

``` bash
git status
git remote -v
```

The cloned repository is already connected to its GitHub remote, usually
named `origin`.

## 15. Useful Git Commands Cheat Sheet

  Purpose                              Command
  ------------------------------------ ----------------------------------------------------
  Check Git version                    `git --version`
  Set your name                        `git config --global user.name "Your Name"`
  Set your email                       `git config --global user.email "you@example.com"`
  View configuration                   `git config --global --list`
  Initialize repository                `git init`
  Check status                         `git status`
  Stage all changes                    `git add .`
  Stage one file                       `git add filename.py`
  Unstage a file (keep edits)          `git restore --staged filename.py`
  View unstaged changes                `git diff`
  View staged changes                  `git diff --cached`
  Commit changes                       `git commit -m "Message"`
  View commit history                  `git log --oneline`
  List branches                        `git branch`
  Create a branch                      `git branch branch-name`
  Switch branch                        `git switch branch-name`
  Create and switch branch             `git switch -c branch-name`
  Rename current branch                `git branch -m new-name`
  Delete a merged local branch         `git branch -d branch-name`
  Add remote                           `git remote add origin URL`
  View remote URLs                     `git remote -v`
  Change remote URL                    `git remote set-url origin URL`
  Download and integrate updates       `git pull`
  Upload commits                       `git push`
  First push of a branch               `git push -u origin branch-name`
  Clone a repository                   `git clone URL`
  Merge a branch into current branch   `git merge branch-name`

## 16. Common Errors and How to Fix Them

### Error: `Author identity unknown`

Git does not know the name or email to attach to your commits.

``` bash
git config --global user.name "Your Full Name"
git config --global user.email "your-email@example.com"
```

Then try the commit again.

### Error: `remote origin already exists`

A remote named `origin` has already been configured.

``` bash
git remote -v
```

If the URL is wrong:

``` bash
git remote set-url origin https://github.com/your-username/your-repository.git
```

### Error: `src refspec main does not match any`

Common causes include having no commit yet or using a branch name that
does not exist.

Check your branch and status:

``` bash
git branch
git status
```

If you have not made a commit, stage and commit your files first:

``` bash
git add .
git commit -m "Initial commit"
```

If your branch is named `master` rather than `main`, either push the
actual branch:

``` bash
git push -u origin master
```

Or rename the current branch to `main`:

``` bash
git branch -M main
git push -u origin main
```

### Error: `failed to push some refs`

The remote repository may contain commits that your local repository
does not have.

First, check that you are on the correct branch. Then:

``` bash
git pull --rebase origin main
git push
```

Replace `main` with your actual branch name if necessary. If Git reports
conflicts, resolve them before continuing.

### Error: `Authentication failed`

GitHub may require you to authenticate through a browser or credential
manager. Follow the sign-in prompt provided by Git. GitHub account
passwords are not accepted for ordinary HTTPS Git operations.

-   Use Git Credential Manager/browser authentication when prompted, or
-   Configure an SSH key if your course or computer setup requires SSH.

Never share your password, personal access token, or private SSH key
with anyone.

### Error: `Your local changes would be overwritten`

You have uncommitted edits that may be affected by the operation.

Check your changes:

``` bash
git status
```

If the changes are ready to save:

``` bash
git add .
git commit -m "Save current work"
```

Then retry the pull or branch switch. If the changes are not ready to
commit, ask your teacher for help before using reset or discard
commands.

### Merge conflict

A merge conflict occurs when Git cannot automatically combine changes to
the same part of a file.

1.  Run `git status` to identify conflicted files.
2.  Open each conflicted file in your code editor.
3.  Find conflict markers:

``` text
<<<<<<< HEAD
Your current branch's version
=======
The incoming branch's version
>>>>>>> branch-name
```

4.  Edit the file so that it contains the correct final code.
5.  Remove all conflict markers.
6.  Save the file.
7.  Stage the resolved file and complete the merge or rebase as Git
    instructs.

For a normal merge:

``` bash
git add filename.py
git commit
```

For a rebase conflict:

``` bash
git add filename.py
git rebase --continue
```

If you are unsure which version to keep, do not guess. Ask your teacher
or collaborator.

## 17. Use a `.gitignore` File

A `.gitignore` file tells Git which files or folders should normally not
be tracked.

For a Python project, you may use:

``` gitignore
# Python cache files
__pycache__/
*.py[cod]

# Virtual environments
venv/
.venv/

# Editor and operating-system files
.vscode/
.DS_Store
Thumbs.db
```

Create a file named exactly `.gitignore` in the root of your project
folder. Add the patterns above, then save it.

**Important:** `.gitignore` does not automatically remove files that Git
is already tracking. Also, do not ignore files that your teacher
requires you to submit.

## 18. Suggested Student Repository Organization

Keep your repository neat and easy to check. For example:

``` text
CS-Programming-Activities/
│
├── README.md
├── .gitignore
│
├── Activity1/
│   └── Activity1-YourLastname.py
│
├── Activity2/
│   └── Activity2-YourLastname.py
│
└── Activity3/
    └── Activity3-YourLastname.py
```

Follow the exact folder and file-naming instructions given by your
teacher. If a required naming format is provided, use it consistently.

## 19. Submission Checklist

Before submitting your GitHub repository link, verify the following:

-   [ ] Git is installed and configured.
-   [ ] I am working in the correct project folder.
-   [ ] My files have the required names and folder structure.
-   [ ] My code has been saved and checked.
-   [ ] I ran `git status` and reviewed the changes.
-   [ ] I staged the correct files using `git add`.
-   [ ] I committed my work with a meaningful message.
-   [ ] I pushed the correct branch to GitHub.
-   [ ] I opened GitHub in a browser and confirmed that the latest files
    are visible.
-   [ ] I copied the correct repository link.
-   [ ] I submitted the repository link through the platform specified
    by my teacher.

## 20. Important Git Safety Reminders

Be careful with commands that remove or overwrite work.

Avoid running these commands unless your teacher specifically instructs
you and you understand their effects:

``` bash
git reset --hard
git clean -fd
git push --force
```

-   `git reset --hard` can discard uncommitted changes.
-   `git clean -fd` can delete untracked files and folders.
-   `git push --force` can overwrite remote branch history and affect
    other collaborators.

Never upload passwords, API keys, access tokens, private keys, or
confidential personal information to GitHub.

------------------------------------------------------------------------

## Quick Reference: The Five Commands to Remember

For most individual programming activities in an existing repository,
these are the commands you will use most often:

``` bash
git status
git add .
git commit -m "Describe your changes"
git pull
git push
```

For a new local project that you want to upload for the first time, the
general sequence is:

``` bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/your-repository.git
git push -u origin main
```

Replace the sample repository URL with your own. If the GitHub
repository already contains files or commits, or if you are using an
existing repository, follow the appropriate clone/pull workflow instead
of blindly repeating the initialization sequence.

**Final reminder:** Always verify your work on GitHub after pushing. A
successful local commit does not automatically mean that your work has
been uploaded or submitted.
