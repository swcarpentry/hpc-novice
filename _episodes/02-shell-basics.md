---
title: "Shell Basics"
teaching: 15
exercises: 15
objectives:
- "Understand that the shell can be used to do the same tasks as a graphical file browser"
- "Learn to navigate the filesystem and create, remove, delete and move files and directories"
- "Learn to use a command-line text editor like `nano`"
questions:
- "How do I view the files and folders in the filesystem?"
- "How do I specify the location of a file or folder in the filesystem?"
- "How do I create, delete, move and rename files and folders?"
- "How do I create and edit text files?"
keypoints:
- "Use `cd`, `pwd` and `ls` to navigate the file system and inspect its contents"
- "Use `cp`, `mv` and `rm` to copy, move and remove files or directories"
- "Use `mkdir` and `touch` to create new empty directories and files respectively"
- "The location of a file or folder, i.e., the *path* to the file or folder can be relative or absolute. An absolute path always starts from the root directory (`/`)"
- "Text files can be created and edited from the command-line using an editor like `nano` or `vim`"
---

The command-line or **shell** is another way of interacting with a computer,
just like the graphical interface (windows, pointer, icons, toolbars and menus)
that you may be more familiar with.
The difference is that rather than
clicking on buttons, menu items and check-boxes, or entering text into graphical boxes,
you provide instructions to the computer by
issuing commands to it.

As a few examples of tasks you might do on your computer,
consider:

* Creating new files or folders
* Navigating between folders on your computer and viewing their contents
* Moving, renaming, deleting or copying files and folders

You are probably familiar with using a graphical file browser
such as **Windows Explorer** (Windows) or **Finder** (Mac OS X)
for doing the above tasks:
The same tasks can be performed on the command-line,
using a few simple commands:

| Command 	  			| Action
------------------------|-------------------------------------------
| `pwd`		  			| Print working directory
| `cd DIR` 				| Change directory to `DIR`	
| `ls`					| List contents of current directory
| `mkdir DIR`			| Make new empty directory `DIR`
| `touch FILE`          | Make new empty file `FILE`
| `cp SRC DEST`			| Copy file `SRC` into file `DEST`
| `cp -r SRC DEST`		| Copy directory `SRC` into directory `DEST`
| `rm FILE`				| Remove (delete) file `DIR`
| `rm -r DIR`			| Remove (delete) directory `DIR`
| `mv SRC DEST`         | Move the file (or directory) `SRC` into the directory `DEST`.

In this part of the lesson we'll explore
and familiarize ourselves with such commands.

When you login to the cluster,
you begin at the home directory:

~~~
[nelle@login001 ~]$ pwd
~~~
{: .bash}

~~~
/home/nelle
~~~
{: .output}

You can list the files and folders
in this directory using `ls`:

~~~
[nelle@login001 ~]$ ls
~~~
{: .bash}

~~~
genomics-workshop   genomics-workshop.zip
~~~
{: .output}

> ## File and folder names
> Notice that we used a hyphen (`-`) between the words
> `genomics` and `workshop` for the folder `genomics-workshop`.
> Always avoid using spaces in file and folder names.
> To see why it's a bad idea, try running the following command:
>
> ~~~
> [nelle@login001 ~]$ mkdir genomics workshop
> ~~~
>
> Now, type `ls`. What do you see?
>
{: .callout}

The `ls` command accepts many **switches**
which modify its behaviour;
try the following command:

~~~
[nelle@login001 ~]$ ls -a

.bash_profile   .bashrc     genomics-workshop
~~~

The `-a` switch prints files/directories beggining with a dot (`.`).
These are usually hidden from the output of `ls`.

> ## Switches, inputs, parameters or arguments
>
> These are all names for similar things,
> and often they are used interchangeably.
> Anything that follows the name of a command entered into the shell
> can be a switch, input, parameter or argument to that command.
> Many commands can accept multiple switches
> and compose them in meaningful ways.
> Try the following `ls` commands:
>
> 1. `ls`
> 2. `ls -a`
> 3. `ls -F`
> 4. `ls -l`
> 5. `ls -F -a`
> 6. `ls -Fa`
> 7. `ls genomics-workshop`
> 8. `ls -Fa genomics-workshop`
>
{: .callout}

So far, we have been working in our "home" directories (`/home/username`).
Let's change directories using `cd`:

~~~
[nelle@login001 ~]$ cd genomics-workshop
~~~
{: .bash}

~~~
[nelle@login001 genomics-workshop]$
~~~
{: .output}

The prompt has changed to indicate our working directory.
We can confirm this using `pwd`:

~~~
[nelle@login001 genomics-workshop]$
~~~
{: .bash}

~~~
/home/nelle/genomics-workshop
~~~
{: .output}

> ## Exploring the `shell-basics` folder
> 
> This is a pen-and-paper exercise.
>
> Inside the `genomics-workshop` directory,
> you will find the directory `shell-basics`.
> Explore the directory `shell-basics`
> using the commands you have learned so far,
> and draw a diagram representing the
> layout of the files and folders inside it.
> Here is an example diagram:
>
> ~~~
> ├── reminders.txt
> ├── software/
> │   ├── README.txt
> │   └── matlab/
> │       └── install.txt
> └── thesis/
> ~~~
>
> Compare your diagram with your neighbour's.
> Did you find any differences?
>
> Here are some additional commands you may find useful
>
> Command           | Action
> ------------------|--------------------------
> `cd ..`           | Go "up" one directory
> `ls DIR`          | List the contents of the directory `DIR`
> `cd A/B`          | Change directory to `B`, a sub-directory of `A`
>
{: .challenge}

> ## Copying and deleting things
> 
> Navigate to your home directory `/home/username`.
> Create a copy of the `genomics-workshop` directory
> called `genomics-workshop-backup`.
> In the original `genomics-workshop` directory,
> delete all files beginning with the letter `c`
> in the folder `shell-basics/data/pdb`, i.e., the files:
> 
> ~~~
> camphene.pdb       cinnamaldehyde.pdb codeine.pdb        cyclobutane.pdb    cyclopropane.pdb
> cholesterol.pdb    citronellal.pdb    cubane.pdb         cyclohexanol.pdb
> ~~~
>
> Hint: you can delete several files at once using `rm`:
>
> ~~~
> $ rm FILE1 FILE2 .... FILEN
> ~~~
> {: .bash}
>
> You can also use the asterisk (`*`) **wildcard** to generate a list of files that match a pattern,
> for instance `*.txt` matches all files that end with the extension `.txt`.
>
{: .challenge}

The word "path" is often used to refer to the location
of a file or folder.
Paths can be *relative* or *absolute*.
 
A relative path specifies the location of a file or folder
*relative* to the current directory. For example,
starting from the home directory, `genomics-workshop/shell-basics/data/molecules`
is a relative path to the `molecules` directory:
 
~~~
[nelle@login001 ~]$ cd genomics-workshop/shell-basics/data/molecules/
~~~
{: .bash}

But starting from the `genomics-workshop` directory,
the relative path is instead `shell-basics/data/molecules`:

~~~
[nelle@login001 molecules]$ cd genomics-workshop
[nelle@login001 shell-basics]$ cd shell-basics/data/molecules/
~~~
{: .bash}

Thus the relative path to a file or directory
is different from different locations in the filesystem.

An absolute path specifies the location of a file or folder
starting from the top-most (i.e., the "root" directory `/`).
It always begins with a slash `/`:

~~~
[nelle@login001 molecules]$ cd /home/nelle/genomics-workshop/shell-basics/data/molecules
~~~
{: .bash}

The absolute path to a file or directory
is the same everywhere.

{: .callout}

> ## Relative and absolute paths
> 
> Discuss with your neighbour: what do you think
> each of the following commands does?
>
> 1. `cd .`
> 2. `cd /`
> 3. `cd /home/amanda`
> 4. `cd ../..`
> 5. `cd ~`
> 6. `cd home`
> 7. `cd ~/data/..`
> 8. `cd`
> 9. `cd ..`
>
> Starting from `/home/amanda/data`, which of the above
> commands can Amanda use to navigate to her home directory
> `/home/amanda`?
{: .challenge}

Looking at the `shell-basics` directory,
we see two files `notes.txt` and `solar.pdf`:

~~~
[nelle@login001 shell-basics]$ ls
~~~
{: .bash}

~~~
data  notes.txt  programs  solar.pdf
~~~
{: .output}

The extension of a file (e.g., `.txt` or `.pdf`)
is a *hint* to the user about the contents of that file.
There is no requirement that filenames include an extension,
and a file may be given any extension regardless of its contents.
For example, you may rename a PDF file called `whale.pdf` to `whale.mp3`.
This will not change the contents of the file or transform it into a beautiful whalesong!

A related idea is the *type* of a file.
Broadly speaking, files are of two types:

1. **Text files** are files that contain data in human-readable
format such as letters and numbers.
A text file can be easily viewed and edited using any text-editor,
such as Notepad, TextEdit or Atom.

2. **Binary files** are files that contain data in machine-readable format.
Special programs are required to open, view or edit binary files.
For example, a `.docx` file can only be understood by programs
like Microsoft Word or OpenOffice Writer.

> ## Text v/s binary files
>
> The commands `cat`, `head` and `tail` are useful
> for viewing files.
>
> Command           | Action
> ------------------|--------------------------
> `cat FILE`        | Print the contents of the file `FILE`
> `cat FILE1 FILE2` | Concatenate (join) the files `FILE1` and `FILE2` and print the result
> `head FILE`       | Print the first 10 lines of the file `FILE`
> `head -n 4 FILE`  | Print the first 4 lines of the file `FILE`
> `tail FILE`       | Print the last 10 lines of the file `FILE`
> `tail -n 4 FILE`  | Print the last 4 lines of the file `FILE`
>
> Print the first few lines of the two files
> `notes.txt` and `solar.pdf`.
> Can you explain the output of each command?
>
{: .challenge}

As a user of the cluster,
you will frequently be working with text files
such as scripts, source code, documentation, configuration files, etc.,
so it's important that you learn to view and edit these files efficiently.

Graphical text editors like Notepad or Atom are unavailable on the cluster.
Instead, you must use a terminal-based text editor
to edit text files.
`nano` is a very simple editor that can be used
for basic text editing:

~~~
[nelle@login001 shell-basics]$ nano notes.txt
~~~
{: .bash}

When you open a text file such as `notes.txt` using `nano`,
you should see the following screen:

~~~
  GNU nano 2.3.1		File: notes.txt

- finish experiments
- write thesis
- get post-doc position (pref. with Dr. Horrible)











^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Page ^K Cut Text  ^C Cur Pos
^X Exit      ^J Justify   ^W Where Is  ^V Next Page ^U UnCut Text^T To Spell
~~~
{: .output}

Here, you can add or remove text.
Along the bottom of the editor window,
you will see that you can type `^O` (or `Control+O`)
to write out or "save" any changes you make,
and `Control+X` to exit `nano`.
When prompted for "Yes" or "No",
you can type the `Y` or `N` key respectively.

> ## Other text editors
> While `nano` is well-suited for basic-editing
> and a good choice for beginners,
> you will probably want to learn a text editor designed for
> [real programmers](https://xkcd.com/378/)
> such as [`vim`](https://en.wikipedia.org/wiki/Vim_(text_editor))
> or [`emacs`](https://en.wikipedia.org/wiki/Emacs).
> Type `vimtutor` on the command-line for a quick introduction
> to `vim`.
{: .callout}


> ## Using `nano` to create a new file
> In addition to editing existing files,
> you can use `nano` to create new files as well.
>
> If you type `nano` without any arguments,
> you have the option of specifying a file name
> before saving and exiting.
>
> ~~~
> $ nano
> ~~~
> {: .bash}
>
> You can also provide the filename as an argument
> (even if it doesn't exist):
>
> ~~~
> $ nano FILENAME
> ~~~
> {: .bash}
> 
> Create a new file `abstract.txt` in your home directory,
> containing a short abstract of your research.
> Share with your neighbour.
>
{: .challenge}
