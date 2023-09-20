Git Commands
============
Create a local repository
-------------------------
#. Create a new directory
#. Open a terminal window and go to the new directory, then type

.. prompt:: bash

    git init

Add user configuration to repository
------------------------------------
Add user information to allow commits

.. prompt:: bash

    git config user.email "johndoe@company.com"
    git config user.name "johndoe"

Add remote repository
---------------------
Add new remote repository (here named ``origin``). Remote repository must already exist.

.. prompt:: bash

    git remote add origin <remote_repo_url>

Change remote repository URL

.. prompt:: bash

    git remote set-url origin <new_remote_repo_url>

Check remote URLs

.. prompt:: bash

    git remote -v

Log into remote repository account
----------------------------------
In case your IDE isn't managing your remote login (for example Github), you may use
the `git-credential-manager` (already included in `Git for Windows`_ if checked
during installation, see
`here <https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md>`
for installation instruction on Linux & macOS)

From inside your git repository, run

.. prompt:: bash

    git config --global credential.helper wincred

to set the *git-credential-manager* as your global credential helper tool.

Next, run a git command involving the remote repository, for example ``git pull``.
In case, the git config doesn't have your login credentials, it launches the
credential manager, which asks for it.

To see your set credential manager, run:

.. prompt:: bash

    git config credential.helper

.. _Git for Windows: https://git-scm.com/download/win

Add files to source control
---------------------------
#. Create files within local repository
#. Add the files to source control via

.. prompt:: bash

    git add <path/to/fileA> <path/to/fileB> ...

Un/Stage files
--------------
Add files to git index:

.. prompt:: bash

    # stage single files
    git add <path/to/fileA> <path/to/fileB>
    # stage all files within current directory
    git add .
    # stage all new, modified, deleted files within repository
    git add -A

Revoke staged files from git index:

.. prompt:: bash

    git reset HEAD </path/to/fileA> </path/to/fileB>

Remove files from repo that have already been committed before (doesn't remove them
from the local file system |:slight_smile:|)

.. prompt:: bash

    git rm --cached <path/to/file>

Commits
-------
Commit to current branch with a message

.. prompt:: bash

    git commit -m "Important changes"

Stage and commit all modified or deleted file (excluding new files)

.. prompt:: bash

    git commit -a -m "Important changes

Change message on most recent commit

.. prompt:: bash

    git commit --amend

    An editor opens, edit message and close to confirm.

Stashing
--------
In contrast to 'staging', a stash is a temporary storage of any recent changes made
inside a directory and thereby cleaning it from those changes

.. prompt:: bash

    git stash -m "Stashing potential implementation"

Apply changes from stash to current directory and remove them from the stash

.. prompt:: bash

    git stash pop

Apply changes from stash to current directory, but keep them in the stash

.. prompt:: bash

    git stash apply

List all stashed changes

.. prompt:: bash

    git stash list

Branching
---------
List all local branches

.. prompt:: bash

    git branch

List all local and remote branches

.. prompt:: bash

    git branch -a

Create a new branch

.. prompt:: bash

    git branch <branch_name>

Switch to another branch

.. prompt:: bash

    git checkout <branch_name>

Create and switch to a new branch

.. prompt:: bash

    git checkout -b <branch_name>

Delete an existing branch (if it's merged)

.. prompt:: bash

    git branch -d <branch_name>

Force delete an existing branch

.. prompt:: bash

    git branch -D <branch_name>

Delete all branches except *master*:

.. prompt:: bash

    git branch | grep -v master | xargs git branch -D

.. hint::

    **Delete "useless" branches locally**

    *Useless* branches are considered those who are merged, not currently
    checked out and not *master* (the main branch).

    Copy those lines into ``~/.gitconfig``:

    .. code-block:: ini

        [alias]
            # Delete all local branches but master and the current one, but only if they are fully merged with master
            br-delete-useless = "!f(){\
                git branch | grep -v "master" | grep -v ^* | xargs git branch -d;\
            }; f"
            # Delete all local branches but master and the current one
            br-delete-useless-force = "!f(){\
                git branch | grep -v "master" | grep -v ^* | xargs git branch -D;\
            }; f"

    This enables those two git aliases:

    .. prompt:: bash

        git br-delete-useless
        git br-delete-useless-force

    which deletes all *useless* local branches. Be careful, using
    ``git br-delete-useless-force`` also deletes them if they haven't
    yet been merged to master.

Delete branch on remote

.. prompt:: bash

    git push <remote_name> --delete <branch_name>

Rename currently checked out branch

.. prompt:: bash

    git branch -m "New branch name"

Merging & Rebase
----------------
**Merge the active branch with the branch <branch_name>**

You will create a new commit for the active branch with the merged changes remain in the
active branch (use ``-m`` to overwrite default commit message)

.. prompt:: bash

    git merge <branch_name> -m "merge with <branch_name>"

**Abort a merge**

If a merge results in a conflict, it has to be aborted, before it can be resolved

.. prompt:: bash

    git merge --abort

**Rebase a branch**

This puts the *active branch* on top of the *specified branch*. It is basically a merge,
where the inheritance tree of the *specified branch* becomes a sequential line with the commits of the
*active branch* at its end. If the changes of the *active branch* are lower than in the tree as the latest
changes of the *specified branch*, it merges the changes onto the latest commit *specified branch*.

Rebasing allows for cleaner commit history, since all commits are eventually gathered onto the same branch.

.. prompt:: bash

    git rebase <target_branch_name>

.. note::

    Never rebase public history (e.g. master), but rebase your changes onto the current state of master.

    .. prompt:: bash

        git checkout <master_branch>
        git pull
        git checkout <feature_branch>
        git rebase <master_branch>

Rebase a ``<on_top_branch_name>`` onto a ``<base_branch_name>`` without having checked out any of them

.. prompt:: bash

    git rebase <base_branch_name> <on_top_branch_name>

After a successful rebase, the master branch HEAD is still pointing to its latest commit, not the latest commit
added to the stream via the rebase. To get *master* back to the very front of the stream (so you can
continue with it), you need to merge the master with the rebased branch:

.. prompt:: bash

    git checkout <master_branch>
    git merge <rebased_branch>

**Abort rebase**

If a rebase action results in a conflict, it has to be aborted before it can be resolved

.. prompt:: bash

    git rebase --abort

**Interactive rebase**

It means to pick certain commits of the current branch for a rebase (here: using the three latest commits)

.. prompt:: bash

    git rebase -i <target_branch_name>~3

This opens a text editor window, which allows you to *pick* certain commits from the list.
Delete commits from the list you want to omit:

.. code-block:: none

    pick f7f3f6d changed my name a bit
    pick 310154e updated README formatting and added blame
    pick a5f4a0d added cat-file
    ...

The commit order can be changed by changing the pick order. Close the file to execute.

Tagging
-------
A lightweight tag is a pointer to a specific commit in a branch.

**Create a tag for the current commit**

.. prompt:: bash

    git tag <TAG_NAME>

**Push the tag to the remote (here: origin)**

.. prompt:: bash

    git push origin <TAG_NAME>

**Push all local tabs to the remote**

.. prompt:: bash

    git push --tags

**List all available tags (in current branch)**

.. prompt:: bash

    git tag -l

**Checkout a tag**

While having checked out the same branch as tag is applied onto, run:

.. prompt:: bash

    git checkout <TAG_NAME>

.. warning::

    Checking out a tag puts the repo into *detached HEAD* state

**Delete a tag**

Delete a local tab:

.. prompt:: bash

    git tag -d <TAG_NAME>

Delete a remote tab:

.. prompt:: bash

    git push --delete origin <TAG_NAME>

Moving along the tree
---------------------
The currently selected commit is the HEAD. Going up the tree means shifting to older commits,
going down means shifting to newer commits.

Select a different commit

.. prompt:: bash

    git checkout <commit_hash_sum>

**Getting previous commit's hash sum**

.. prompt:: bash

    git log

For short hashes (here: latest commit)

.. prompt:: bash

    git log -s --pretty=format:%h -1

Increase the last number to show the last n entries in the commit tree. Also use tools
such as Gitkraken to get hash code of commits easily.

Get previous xx commits

.. prompt:: bash

    git log -<number_of_previous_commits>

Get previous commits by a certain author

.. prompt:: bash

    git log --author="<name>"

Get commits within a certain time frame (date format: YYYY-MM-DD)

.. prompt:: bash

    git log --before="<date>" --after="<date>"

**Relative Refs**

Move upwards by one commit on a certain branch

.. prompt:: bash

    git checkout <branch_name>^

Move upwards by three commits on a certain branch

.. prompt:: bash

    git checkout <branch_name>^^^
    git checkout <branch_name>~3

Move up from current HEAD (here: two commits)

.. prompt:: bash

    git checkout HEAD^^
    git checkout HEAD~2

**Move a branch to a different commit**

This sets the latest commit of a branch to a certain previous commit

.. prompt:: bash

    git branch -f <branch_name> HEAD~3
    git branch -f <branch_name> <target_commit_hash_sum>

Revert changes
--------------
Move back the branch and undo all in-between changes (here: by one commit)

.. prompt:: bash

    git reset <branch_name>~1

Revert changes done to a staged file (first un-stage, then checkout latest commit)

.. prompt:: bash

    git restore --staged <path_to_file>
    git checkout .

Revert changes made to current working copy since last checkout

.. prompt:: bash

    git checkout .

Remove all unstaged files and directories (``-f`` ... force; ``-d`` ... include directories)

.. prompt:: bash

    git clean -fd

Reverts changes of previous commits. In contrast to ``git reset``, the revert command does not delete
the reverted commits, but creates a new commit, which excludes the reverted commits.

.. prompt:: bash

    # revert changes from specific commit
    git revert <bad_commit_hash_sum>
    # revert changes of previous three commits
    git revert HEAD~3

Reset HEAD to latest commit, reverting all changes since then

.. prompt:: bash

    git reset --hard
    git reset --hard HEAD

Reset HEAD to previous commit (will delete all changes/commits in between)

.. prompt:: bash

    # to certain commit
    git reset --hard <commit_hash_sum>
    # three commits upwards
    git reset --hard HEAD~3

.. hint::
    Reverting is often preferred over resetting, since resetted commits are removed permanently,
    whereas reverted commits are still in the tree (in case, they are still needed later).

Cherry Pick
-----------
Cherry picking lets you pick specific commits from different branches and add it to the current HEAD

.. prompt:: bash

    git cherry-pick <commit_hash_sum_A> <commit_hash_sum_B>

Detached head mode
------------------
When checking out a commit instead of a branch that HEAD is not pointing to you are forced into the detached head mode.
You can work here, but in order to merge your changes into HEAD, you must first create a new branch,
make your changes there, then checkout *master* and merge it.

.. prompt:: bash

    git checkout <commit_hash_sum>
    git checkout -b <new_branch_name>
    git commit -m "important changes"
    git checkout master
    git merge <new_branch_name>

Clone remote repositories
-------------------------
Clone remote repository into the current working directory

.. prompt:: bash

    git clone <remote_repository_url>

Update a repository
-------------------
Download latest commits from the remote repository (same branch)

``git fetch`` fetches all commits (including branches and tags) that are not in the local repository.
Our local state (including the current branch) remain **unchanged** (no update). Newly fetched branches
become present in our local repo and are properly named, so it's obvious, those derive from remote changes.

.. prompt:: bash

    git fetch

Download changes from a specific remote. If not <remote_name> is given, **origin** is used by default.

.. prompt:: bash

    git fetch <remote_name>

Remove all local references to no more existing branches on the remote (not including tags, here the
option ``--prune-tags`` must be used).

.. prompt:: bash

    git fetch --prune

``git pull`` also fetches missing commits from the remote, but also merges them into new commits

.. prompt:: bash

    git pull

is the shorthand for

.. prompt:: bash

    git fetch
    git merge FETCH_HEAD

while FETCH_HEAD points to the fetched remote branch (i.e. origin)

**Update via ``pull --rebase``**

Gets remote changes (commits), adds them on top of the last common state (last merge),
packs my local changes (commits) on top, all inside one stream.

.. hint:: Must be applied on a specific branch.

.. prompt:: bash

    git pull --rebase <remote_name> <branch_name>

Push changes to remote repository
---------------------------------
Push all committed changes of the current branch to the branch's defined remote repository (default: origin)

.. prompt:: bash

    git push

Push committed changes of <local_branch_name> to <remote_branch_name> (default: origin)

.. prompt:: bash

    git push <remote_repo_name> <local_branch_name>

Push latest commit of a tag to the remote repository

.. prompt:: bash

    git push <remote_repo_name> <local_tag_name>

Push all local branches to the remote

.. prompt:: bash

    git push <remote_repo_name> --all

Resolve push conflicts
----------------------

:Error:
    When trying to push commits that are based on outdated commits, the push fails.

:Solution 1:
    Fetch the latest state of the remote repo, **rebase** that state with your local branch, then push teh resulting changes.

    .. prompt:: bash

        git fetch
        git rebase origin/master
        git push <remote_branch> <current_branch_name>

    or

    .. prompt:: bash

        git pull --rebase origin/master
        git push <remote_branch> <current_branch_name>

:Solution 2:
    Fetch the lastest state from the remote repo, **merge** that state with your current local branch, then push the resulting changes.

    .. prompt:: bash

        git fetch
        git merge origin/master
        git push <remote_branch> <current_branch_name>

    or

    .. prompt:: bash

        git pull origin/master
        git push <remote_branch> <current_branch_name>

:Solution 3:
    **Accept the remote version** of a conflicted file, then push your commit.

    .. prompt:: bash

        git checkout --theirs <conflicted_file_name>
        git commit -m "using theirs"
        git push <remote_branch> <current_branch_name>

:Solution 4:
    **Override the remote version** of a conflicted file, then push your commit.

    .. prompt:: bash

        git checkout --yours <conflicted_file_name>
        git commit -m "using ours"
        git push <remote_branch> <current_branch_name>

Working with forks
------------------
Forking a repository creates a full copy of repository, that can be freely experimented on
without affecting the original repository. You can contribute back to the original repo
using **pull requests**.

Cloning in comparison, does not unhook you from the original repository and you are not
able to contribute, unless you are authorized as a collaborator.

**Contribute to a repository**

#. Create a fork of the original repository. The steps depend on the used Git Host (e.g. Github, Bitbucket).
#. Clone the fork:

    .. prompt:: bash

        git clone <url_to_forked_repository>

#. Make changes, commit and push to remote.
#. Create a pull request towards the target branch of the original repository.
   The steps depend on the used Git Host (e.g. Github, Bitbucket).

**Keep your fork up-to-date**

As other contributors push and merge changes onto the original repository, your fork does not
receives these changes automatically. Having your fork up-to-date when starting your
changes makes merges back to the original much simpler.

#. Add the original repository as additional remote:

    .. prompt:: bash

        git remote add upstream <url_to_original_repository>

#. **Before you start making changes inside your fork**, get the latest changes from
   the original repository (upstream). First, fetch all branches from upstream:

    .. prompt:: bash

        git fetch upstream

#. Make sure you're on *master*:

    .. prompt:: bash

        git checkout master

#. Now rewrite your master branch so that any commits of yours that aren't already
   in upstream/master are replayed on top of that other branch:

    .. prompt:: bash

        git rebase upstream/master

#. Lastly, push the changes to your forked remote:

    .. prompt:: bash

        git push -f origin master

Now you go ahead creating a feature branch.