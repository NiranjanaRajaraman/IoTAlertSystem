#  Getting started with Gitlab

first log in [gitlab.rz.htw-berlin.de](https://gitlab.rz.htw-berlin.de)


Scroll down [Gitlab help](https://gitlab.rz.htw-berlin.de/help/) and find the sections "New to Git and Gitlab?" and "Git and Gitlab"

### Git
An introduction to Git can be found [here](https://git-scm.com/book/en/v2).

After [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) you will want to set it up.

View all settings by running: `$ git config --list --show-origin`


`$ git config --global user.name "John Doe"`

`$ git config --global user.email johndoe@example.com`

### SSH Key

Generate an SSH key pair by: `ssh-keygen -t ed25519`

Copy the contents of your public key file ~/.ssh/.id_ed25519.pub to the clipboard

Sign in to GitLab, select your avatar in the top right corner, select **Preferences**, select **SSH Keys** from the left sidebar,
 paste contents of your public key in the box **Key** (make sure you copy the entire key which starts with `ssh-ed25519`may end 
 with a comment) and select `Add key`.

### Check connection

Run `ssh -T git@gitlab.rz.htw-berlin.de` and yo should get a response: 

> The authenticity of host 'gitlab.rz.htw-berlin.de (141.45.65.80)' can't be established.
> ECDSA key fingerprint is SHA256:zapliBs6RQrrFpMYtcqzc15UxD3QKrJIHMKd3QRuFvU.
> Are you sure you want to continue connecting (yes/no/fingerprint)?

Type ´yes´ and press Enter.

> Warning: Permanently added 'gitlab.rz.htw-berlin.de,141.45.65.80' (ECDSA) to the list of known hosts.
Connection closed by 141.45.65.80 port 22

Run again `ssh -T git@gitlab.rz.htw-berlin.de` (if you set a passphrase you need to enter that) and you should see a response
> Welcome to GitLab, @username!

### Create an empty Repository in Gitlab

Click **new Project** ... uncheck **Initialize repository with a README**

### Push an existing folder

cd existing_folder

`git init`

`git remote add origin git@gitlab.rz.htw-berlin.de:username/projectname.git`

`git add .`

`git commit -m "Initial commit"`

`git push -u origin master`

### Pull a project from GitLab

create a project folder

cd project folder

`git pull origin master` (or main, depending on branch name)

### Adding new file to a new branch

Create a new branch in GitLab

Create a new folder and add files to it

`git init -b branchname`

`git remote add origin git@gitlab.rz.htw-berlin.de:username/projectname.git`

`git pull origin branchname`

`git add .`

`git commit -m "commenting commit"`

`git push -u origin branchname`










## Change Project name

in the project select **Settings**, next select **General** and change the name.

## deleting files from a project

`git rm filename.xxx`

`git add -A`

`git commit -m "removed file xx"`

`git push -u origin branchname`

