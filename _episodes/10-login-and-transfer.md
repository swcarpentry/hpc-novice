---
title: "Logging In And Transfer Data To and From"
questions:
- "How do I open a terminal?"
- "How do I connect to a remote computer?"
- "How do I log in to the cluster?"
- "How do I transfer data back and forth to the cluster?"
- "How do I upload/download files to the cluster?"
objectives:
- "Connect to a cluster."
- "Be able to transfer files to and from a computing cluster."
keypoints:
- "A cluster is many small computers rather than one large computer"
- "The login (head) node is the entry-point to the cluster"
- "A secure shell client is a program that lets us log-in
to other computers and run a command-line on them"
- "To connect to a cluster using SSH: `ssh yourUsername@{{site.remote_address}}`"
- "`wget` downloads a file from the Internet."
- "`sftp`/`scp` transfer files to and from your computer."
- "You can use an SFTP client like FileZilla to transfer files through a GUI."
---

## Opening a Terminal

Connecting to an HPC system is most often done through a tool known as "SSH"
(Secure SHell) and usually SSH is run through a terminal. So, to begin using
an HPC system we need to begin by opening a terminal. Different operating
systems have different terminals, none of which are exactly the same in terms
of their features and abilities while working on the operating system. When
connected to the remote system the experience between terminals will be
identical as each will faithfully present the same experience of using that
system.

Here is the process for opening a terminal in each operating system.

### Linux
There are many different versions (aka "flavours") of Linux and how to open a
terminal window can change between flavours.

A very popular version of Linux is Ubuntu. There are many ways to open a
terminal window in Ubuntu but a very fast way is to use the terminal shortcut
key sequence: <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T<kbd>.

### Mac

Macs have had a terminal built in since the first version of OSX since it is
built on a Linux flavour known as BSD (Berkeley Systems Designs).
The terminal can be quickly opened through the use of the Searchlight tool.
Hold down the command key and press the spacebar.
In the search bar that shows up type "terminal", choose the terminal app from the list of results (it will
look like a tiny, black computer screen) and you will be presented with a terminal window.
Alternatively, you can find Terminal under "Utilities" in the Applications menu.

### Windows

While Windows does have a command-line interface known as the "Command
Prompt" that has its roots in MS-DOS (Microsoft Disk Operating System) it
does not have an SSH tool built into it and so one needs to be installed.
There are a variety of programs that can be used for this, two common ones we
describe here, as follows:

#### MobaXterm

MobaXterm is a terminal window emulator for Windows and the home edition can
be downloaded for free from
[mobatek.net](https://mobaxterm.mobatek.net/download-home-edition.html). If
you follow the link you will note that there are two editions of the home
version available: Portable and Installer. The portable edition puts all
MobaXterm content in a folder on the desktop (or anywhere else you would like
it) so that it is easy add plug-ins or remove the software. The installer
edition adds MobaXterm to your Windows installation as any other program you
might install. If you are not sure that you will continue to use MobaXterm in
the future you are likely best to choose the portable edition.

Download the version that you would like to use and install it. Once the software is
installed you can run it by either opening the folder installed with the
portable edition and double-clicking on the file named
*MobaXterm_Personal_10.2* or, if the installer edition was used, finding the
executable through either the start menu or the Windows search option.

Once the MobaXterm window is open you should see a large button in the middle
of that window with the text "Start Local Terminal". Click this button and
you will have a terminal window at your disposal.

#### PuTTY

It is strictly speaking not necessary to have a terminal running on your local computer in order to access and use a remote system, only a window into the remote system once connected. PuTTy is a well-known and widely used software solution to take this approach.

PuTTY is available for free download from [www.putty.org](http://www.putty.org/). Download the version that is correct for your operating system and install it as you would other software on you Windows system. Once installed it will be available through the start menu or similar.

Running PuTTY will not initially produce a terminal but instead a window full of connection options.  Putting the address of the remote system in the "Host Name (or IP Address)" box and either pressing enter or clicking the "Open" button should begin the connection process.

If this works you will see a terminal window open that prompts you for a username through the `login as:` prompt and then for a password.  If both of these are passed correctly then you will be given access to the system and will see a message saying so within the terminal.  If you need to escape the authentication process you can hold the <kbd>ctrl</kbd>+<kbd>c</kbd> key to exit and start again.

Note that you may want to paste in your password rather than typing it.  Hold <kbd>ctrl</kbd> and right-click of the mouse to paste content from the clipboard to the PuTTY terminal.

For those logging in with PuTTY it would likely be best to cover the terminal basics already mentioned above before moving on to navigating the remote system.

## Logging onto the system

With a terminal available, we can now log into a remote systems.
For these examples, we will connect to {{site.remote_name}} - a high-performance cluster located at the {{site.location_name}}.
Although it's unlikely that every system will be exactly like {{site.remote_name}},
it's a very good example of what you can expect from a supercomputing installation.
To connect to our example computer, we will use SSH (if you are using PuTTY, see above).

SSH allows us to connect to UNIX computers remotely and use them as if they were our own.
The general syntax of the connection command follows the format `ssh yourUsername@some.remote.address`
Let's attempt to connect to the cluster now:

```
ssh yourUsername@{{site.remote_address}}
```
{: .bash}

```{.output}
The authenticity of host '{{site.remote_address}} (199.241.166.2)' can't be established.
ECDSA key fingerprint is SHA256:JRj286Pkqh6aeO5zx1QUkS8un5fpcapmezusceSGhok.
ECDSA key fingerprint is MD5:99:59:db:b1:3f:18:d0:2c:49:4e:c2:74:86:ac:f7:c6.
Are you sure you want to continue connecting (yes/no)?  # type "yes"!
Warning: Permanently added the ECDSA host key for IP address '199.241.166.2' to the list of known hosts.
yourUsername@{{site.remote_address}}'s password:  # no text appears as you enter your password
Last login: Wed Jun 28 16:16:20 2017 from s2.n59.queensu.ca

Welcome to {{site.remote_name}}.
```

If you've connected successfully, you should see a prompt like the one below.
This prompt is informative, and lets you grasp certain information at a glance:
in this case `[yourUsername@computerName workingDirectory]$`.
(If you don't understand what these things are, don't worry!
We will cover things in depth as we explore the system further.)

```{.output}
[yourUsername@{{site.machine_name}} ~]$
```

## Telling the Difference between the Local Terminal and the Remote Terminal

You may have noticed that the prompt changed when you logged into the remote
system using the terminal (if you logged in using PuTTY this will not apply
because it does not offer a local terminal). This change is important because
it makes it clear on which system the commands you type will be run when you
pass them into the terminal. This change is also a small complication that we
will need to navigate throughout the workshop. Exactly what is reported
before the `$` in the terminal when it is connected to the local system and
the remote system will typically be different for every user. We still need
to indicate which system we are entering commands on though so we will adopt
the following convention:

`[local]$` when the command is to be entered on a terminal connected to your local computer

`[remote]$` when the command is to be entered on a terminal connected to the remote system

`$` when it really doesn't matter which system the terminal is connected to.

> ## Being Certain Which System your Terminal is connected to
> If you ever need to be certain which system a terminal you are using is connected to
> then use the follwing command: `$ hostname`.
{: .callout}

> ## Keep Two Terminal Windows Open
> It is strongly recommended that you have two terminals open, one connected
> to the local system and one connected to the remote system, that you can
> switch back and forth between. If you only use one terminal window then you
> will need to reconnect to the remote system using one of the methods above
> when you see a change from `[local]$` to `[remote]$` and disconnect when you
> see the reverse.
{: .callout}

One thing people frequently struggle with is transferring files 
to and from a cluster.
We'll cover several methods of doing this from the command line,
then cover how to do this using the GUI program FileZilla,
which is much more straightforwards.

## Grabbing files from the internet

To download files from the internet,
the easiest tool to use is `wget`.
A good tool for downloading files from the internet is `wget` form the command line.
Here is an example of the `wget` syntax: `wget https://some/link/to/a/file.tar.gz`
We've actually done this before to download our example files:

```
[remote]$ wget https://hpc-carpentry.github.io/hpc-intro/files/bash-lesson.tar.gz
```
{: .bash}

## Transferring single files and folders with scp

To copy a single file to or from the cluster, we can use `scp`.
Here we will break down the syntax for `scp`.

This is similar to `cp` in that there are source and destination arguments.
```
[local]$ scp source destination
```
{: .bash}

The difference between `cp` and `scp` is that in `scp` the source or destination can be remote locations.

The syntax for referencing a remote location is as follows:
 `yourUsername@remotehost:remotepath`
Before the colon is the address for the remote resources, where after the colon is the location of the file on that remote resource.

To transfer *to* another computer:
```
[local]$ scp /path/to/local/file.txt yourUsername@{{site.remote_address}}:/path/on/remote/computer
```
{: .bash}

To download *from* another computer:
```
[local]$ scp yourUsername@{{site.remote_address}}:/path/on/remote/computer/file.txt /path/to/local/copy
```
{: .bash}

Note that we can simplify doing this by shortening our paths.
On the remote computer, everything after the `:` is relative to our home directory.
We can simply just add a `:` and leave it at that if we don't care where the file goes.

```
[local]$ scp local-file.txt yourUsername@{{site.remote_address}}:
```
{: .bash}

To recursively copy a directory, we just add the `-r` (recursive) flag:

```
[local]$ scp -r some-local-folder/ yourUsername@{{site.remote_address}}:target-directory/
```
{: .bash}

## Transferring files interactively with sftp

`scp` is useful, but what if we don't know the exact location of what we want to transfer?
Or perhaps we're simply not sure which files we want to tranfer yet.
`sftp` is an interactive way of downloading and uploading files.
Let's connect to a cluster, using `sftp`- you'll notice it works the same way as SSH:

```
sftp yourUsername@{{site.remote_address}}
```
{: .bash}

This will start what appears to be a bash shell (though our prompt says `sftp>`).
However we only have access to a limited number of commands.
We can see which commands are available with `help`:

```
sftp> help
```
{: .bash}
```
Available commands:
bye                                Quit sftp
cd path                            Change remote directory to 'path'
chgrp grp path                     Change group of file 'path' to 'grp'
chmod mode path                    Change permissions of file 'path' to 'mode'
chown own path                     Change owner of file 'path' to 'own'
df [-hi] [path]                    Display statistics for current directory or
                                   filesystem containing 'path'
exit                               Quit sftp
get [-afPpRr] remote [local]       Download file
reget [-fPpRr] remote [local]      Resume download file
reput [-fPpRr] [local] remote      Resume upload file
help                               Display this help text
lcd path                           Change local directory to 'path'
lls [ls-options [path]]            Display local directory listing
lmkdir path                        Create local directory
ln [-s] oldpath newpath            Link remote file (-s for symlink)
lpwd                               Print local working directory
ls [-1afhlnrSt] [path]             Display remote directory listing

# omitted further output for clarity
```
{: .output}

Notice the presence of multiple commands that make mention of local and remote.
We are actually connected to two computers at once (with two working directories!).

To show our remote working directory:
```
sftp> pwd
```
{: .bash}
```
Remote working directory: /global/home/yourUsername
```
{: .output}

To show our local working directory, we add an `l` in front of the command:

```
sftp> lpwd
```
{: .bash}
```
Local working directory: /home/jeff/Documents/teaching/hpc-intro
```
{: .output}

The same pattern follows for all other commands:

* `ls` shows the contents of our remote directory, while `lls` shows our local directory contents.
* `cd` changes the remote directory, `lcd` changes the local one.

To upload a file, we type `put some-file.txt` (tab-completion works here).

```
sftp> put config.toml
```
{: .bash}
```
Uploading config.toml to /global/home/yourUsername/config.toml
config.toml                                   100%  713     2.4KB/s   00:00
```
{: .output}

To download a file we type `get some-file.txt`:

```
sftp> get config.toml
```
{: .bash}
```
Fetching /global/home/yourUsername/config.toml to config.toml
/global/home/yourUsername/config.toml                               100%  713     9.3KB/s   00:00
```
{: .output}

And we can recursively put/get files by just adding `-r`.
Note that the directory needs to be present beforehand.

```
sftp> mkdir content
sftp> put -r content/
```
{: .bash}
```
Uploading content/ to /global/home/yourUsername/content
Entering content/
content/scheduler.md              100%   11KB  21.4KB/s   00:00    
content/index.md                  100% 1051     7.2KB/s   00:00    
content/transferring-files.md     100% 6117    36.6KB/s   00:00    
content/.transferring-files.md.sw 100%   24KB  28.4KB/s   00:00    
content/cluster.md                100% 5542    35.0KB/s   00:00    
content/modules.md                100%   17KB 158.0KB/s   00:00    
content/resources.md              100% 1115    29.9KB/s   00:00    
```
{: .output}

To quit, we type `exit` or `bye`.

## Transferring files interactively with FileZilla (sftp)

FileZilla is a cross-platform client for downloading and uploading files to and from a remote computer.
It is absolutely fool-proof and always works quite well.
In fact, it uses the exact same protocol as `sftp` under the hood.
If `sftp` works, so will FileZilla!

Download and install the FileZilla client from [https://filezilla-project.org](https://filezilla-project.org).
After installing and opening the program,
you should end up with a window with a file browser of your local system
on the left hand side of the screen.
When you connect to the cluster, your cluster files will appear on the right hand side.

To connect to the cluster,
we'll just need to enter our credentials at the top of the screen:

* Host: `sftp://login.cac.queensu.ca`
* User: Your cluster username
* Password: Your cluster password
* Port: (leave blank to use the default port)

Hit "Quickconnect" to connect!
You should see your remote files appear on the right hand side of the screen.
You can drag-and-drop files between the left (local) and right (remote) sides
of the screen to transfer files.

## Compressing files

Sometimes we will want to compress files ourselves to make file transfers easier.
The larger the file, the longer it will take to transfer.
Moreover, we can compress a whole bunch of little files into one big file to make it easier
on us (no one likes transferring 70000 little files)!

The two compression commands we'll probably want to remember are the following:

* Compress a single file with Gzip - `gzip filename`
* Compress a lot of files/folders with Gzip - `tar -czvf archive-name.tar.gz folder1 file2 folder3 etc`

> ## Transferring files
> Using one of the above methods, try transferring files to and from the cluster.
> Which method do you like the best?
{: .challenge}

> ## Working with Windows
> When you transfer files to from a Windows system to a Unix system
> (Mac, Linux, BSD, Solaris, etc.) this can cause problems.
> Windows encodes its files slightly different than Unix,
> and adds an extra character to every line.
>
> On a Unix system, every line in a file ends with a `\n` (newline).
> On Windows, every line in a file ends with a `\r\n` (carriage return + newline).
> This causes problems sometimes.
>
> Though most modern programming languages and software handles this correctly,
> in some rare instances, you may run into an issue.
> he solution is to convert a file from Windows to Unix encoding with the `dos2unix` command.
>
> You can identify if a file has Windows line endings with `cat -A filename`.
> A file with Windows line endings will have `^M$` at the end of every line.
> A file with Unix line endings will have `$` at the end of a line.
>
> To convert the file, just run `dos2unix filename`.
> (Conversely, to convert back to Windows format, you can run `unix2dos filename`.)
{: .callout}

> ## A note on ports
> All file tranfers using the above methods use encrypted communication over port 22.
> This is the same connection method used by SSH.
> In fact, all file transfers using these methods occur through an SSH connection.
> If you can connect via SSH over the normal port, you will be able to transfer files.
{: .callout}
