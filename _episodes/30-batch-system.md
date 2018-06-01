---
title: "Using the Batch System 101"
teaching: 25
exercises: 20
questions:
- "To be filled."
keypoints: 
- "To be filled." 
---

# What is a scheduler and why do we need it?

An HPC system might have thousands of nodes and thousands of users.
How do we decide who gets what and when?
How do we ensure that a task is run with the resources it needs?
This job is handled by a special piece of software called the scheduler.
On an HPC system, the scheduler manages which jobs run where and when.

**here we need a simple schematic image showing what a scheduler does**

- 

# Working interactively

A first exercise would be to submit a job that does nothing else but print "Hello World!".

~~~
{% include /snippets/02/submit_hello_world_to_void.{{ site.workshop_scheduler }} %}
~~~
{: .bash}

~~~
{% include /snippets/02/output_hello_world_to_void.{{ site.workshop_scheduler }} %}
~~~
{: .output}


That worked out pretty well. The problem is, it's not very helpful and doesn't help Lola or anyone to do her job. But Lola wonders if the job really was executed on another node. She thinks of a little experiment to explore the scheduler a bit. 

~~~
{% include /snippets/02/submit_hostname_experiment.{{ site.workshop_scheduler }} %}
~~~
{: .bash}

~~~
{% include /snippets/02/output_hostname_experiment.{{ site.workshop_scheduler }} %}
~~~
{: .output}

If she repeats this command, over and over again, the output changes. 
So these commands must be running on another node. 

The above instructions may not work on all sites, i.e. they are configurable for different 
schedulers and may be deactivated on your cluster.

### Limitation of interactive work
- what if we have a very long job, and we don't have time to wait for it to finish?
- what if I need to run a lot of different commands?


# Batch jobs


# Managing jobs

- errors, cancelling
- monitoring
- email
