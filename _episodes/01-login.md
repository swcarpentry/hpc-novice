---
title: "Logging In"
questions:
- "What is a command-line?"
- "How do I log in to the cluster?"
- "How is a cluster structured?"
keypoints:
- "A cluster is many small computers rather than one large computer"
- "The login (head) node is the entry-point to the cluster"
- "A command-line is one way to talk to a computer and make it
do things"
- "A secure shell client is a program that lets us log-in
to other computers and run a command-line on them"
---

## What is a cluster?

Brief cluster description, including: 

* Typical HPC cluster
* Distributed system

Basically, anything where you log in at a single entry point and 
then your work is run on other execute points has the potential 
to be a large scale system.  

## Logging in

To log into the head node, you will need the name of the node, 
called the `hostname` and a specific username and password.  This 
information can be given to a log-in protocol called `ssh` or 
"secure shell", which establishes a secure connection for you 
between your computer and the head node, and creates a shell session 
on the head node.  

On a Mac or Linux system, you can use ssh via the "Terminal" application 
to log in.  The structure of an ssh login looks like this.  

~~~
$ ssh username@hostname
~~~
{: .bash}

There are multiple programs to connect to remote servers for Windows.  One 
easy to use option is "PuTTy", which can be 
downloaded [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). When 
you open the Putty executable (putty.exe), you should see a screen like this:

![](img/putty-7.jpeg)

See the field where you should enter the hostname of the head node.  
You should use Port 22 and connect using "ssh" -- these are usually the defaults.  
After you click "connect" you will be prompted to fill in your username and password. 

> ## Logging in
> 
> Based on the information given by the instructor, log in 
> to the system that you'll be using for this workshop.  
{: .callout}