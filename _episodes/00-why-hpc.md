---
title: "Introducing High-Performance Computing"
questions:
- "What is a super computer?"
- "Why use a remote computer?"
- "How is using a cluster different than your laptop?"
objectives:
- "Be able to describe what an HPC system is"
- "Identify how an HPC system could benefit you."
keypoints:
- "Super computers do not have screens."
- "Super computers are setup in remote places."
- "Super computers can be reached with ssh."
- "Files are transferred using scp/rsync."
- "There is a difference between cloud and HPC."
- "High Performance Computing (HPC) typically involves connecting to very large computing systems elsewhere in the world."
- "These other systems can be used to do work that would either be impossible or much slower or smaller systems."
- "The standard method of interacting with such systems is via a command line interface called Bash."
---

Through out this material, we will assist Lola Curious over her shoulder while she is starting to work at the Institute of Things as a side job to earn some extra money. 

On the first day, her supervisor greets her friendly and welcomes her to the job. He explains what her task is and suggests her that she will need to use the HPC cluster on the campus. Lola has so far used her Laptop at home for her studies, so the idea of using a super computer appears a bit intimidating to her. Her supervisor notices her anxiety and tells her that she will receive an introduction to the super computer after she has requested an account on the cluster. The word _super computer_ however doesn't bring Lola to ease.

Lola walks to the IT department and finishes the paper work to get an account. One of the admins, called Rob, promises to sit down with her in the morning to show her the way around the machine. And as Lola expected, they don't own a super computer. Rob explains that Lola will use a small to mid-range HPC cluster.

> ## A Super Computer ?
> Generally, a super computer refers to the worlds fastest machines available irrespective of their design but with the limitations that they need to be general purpose. Smaller computers of similar design than the above are commonly referred to as High performance computing (HPC) farms, batch farms, HPC clusters etc. A list of the fastest super computers is available on [top500.org](https://www.top500.org/lists/).
{: .callout}

First of all, Rob asks Lola to connect to the super computer. Rob mentions that in the past, compute clusters were named after planets or moons as they often presented distant somewhat mythological places. One of Rob's first instructors then often said, that they would use the Space Shuttle (or `ssh` briefly) to reach that planet or moon. So Rob asks Lola to open a terminal on her laptop and type in the following commands:

~~~ 
$ ssh lola@{{ site.workshop_login_host }}
~~~
{: .bash}

~~~ 
Last login: Tue Mar 14 14:13:14 2017 from lolas_laptop
-bash-4.1$ 
~~~
{: .output}

Rob explains to Lola that she is using the secure shell or `ssh`. This establishes a temporary encrypted connection between Lola's laptop and `{{ site.workshop_login_host }}`. The word before the `@` symbol, e.g. `lola` here, is the user account name that Lola has access permissions for on the cluster. 

> ## Where do I get this `ssh` from ?
> On Linux and/or macOS, the `ssh` command line utility is typically pre-installed. Just open a terminal and you are good to go. At the time of writing, the openssh support on microsoft is still pretty [recent](https://blogs.msdn.microsoft.com/powershell/2017/12/15/using-the-openssh-beta-in-windows-10-fall-creators-update-and-windows-server-1709/). Alternatives to this are [putty](http://www.putty.org), [bitvise SSH](https://www.bitvise.com/ssh-client-download) or [mRemoteNG](https://mremoteng.org/). Download it, install it and open the GUI. They typically ask for your user name and the destination address or IP. Once provided, you will be queried for your password just like in the example above.
{: .callout}


Rob tells her to use a UNIX command called `ls` (for list directory contents) to have a look around. 

~~~ 
$ ls
~~~
{: .bash}

~~~ 
~~~
{: .output}

To no surprise, there is nothing in there. Rob asks Lola to issue a command to see on what machine she currently is on.

~~~ 
$ hostname
~~~
{: .bash}

~~~ 
{{ site.workshop_login_host }}
~~~
{: .output}

Lola wonders a bit what this may be about, that you need a dedicated command to tell you where you are, but Rob explains to her that he has so many machines under his responsibility, that the output of `hostname` is often very valuable.

> ## Am I in the cloud now?
> Not really, sorry. At the time of writing, there are a couple of distinctive features that separate cloud computing from HPC.
> + *HPC*:
>   + machines are always available, i.e. the URL or address that you give to ssh to doesn't change over time typically and the servers of an HPC infrastructure are operating 24/7 behind this address
>   + machines typically run so called bare metal operating systems, i.e. when you ssh into an HPC cluster, the operating system that you will use is the same one the server was booted into
> - *cloud*:
>   - instances have to be requested (albeit this can be automated) e.g. on a web page. Then a user will be supplied a URL or address to point ssh to.
>   - cloud instances are run in so called virtual machines, i.e. an operating system inside an operating system, this is one of the reasons why the performance of cloud instances can be inferior to HPC clusters
{: .callout}

Rob explains to Lola that she has to work with this remote shell session in order to run programs on the HPC cluster. Launching programs that open a Graphical User Interface (GUI) is possible, but the interaction with the GUI will be slow as everything will have to get transferred through the WiFi network her laptop is currently logged into. Before Rob continues, he suggests to leave the cluster node again. For this, Lola can type in `logout` or `exit`.

~~~ 
$ logout
~~~
{: .bash}


Topics

When it is appropriate to use a cluster

> ## How can you use a cluster?
> 
> Talk to your neighbor about your research.  How does computing 
> help you do your research?  How could more computing help you 
> do more or better research?  
{: .callout}

How is using a cluster different than your laptop?  

> ## Thinking ahead
> How is using a large-scale computing system different 
> from using your laptop? Talk to your neighbor about some 
> differences you may already know about, and some 
> differences/difficulties you imagine you may run into.


