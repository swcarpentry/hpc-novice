---
title: "HPC architecture"
questions:
- "What is a high-performance computer?!"
- "How are high-performance computers different from personal computers?"
- "How do these differences influence how I use HPC systems most effectively?"
objectives:
- "Provide a general mind map of how HPC resources are connected together (head node, compute node, NAS)"
keypoints: 
- "A high-performance computer system provides a larger compute capability than is possible to package in a personal computer."
- "HPC systems are typically an aggregation of a bunch computers, each one of which can look pretty similar to your personal computer."
- "HPC systems are usually accessed remotely, over the network."
- "HPC systems are usually shared among many users.  Each user typically gets a dedicated portion of the computer's resources for a period of time."
- "Special measures have to be taken to provide a file system that can keep up with an HPC system."
- "HPC systems often provide a lot of different software packages, and provide ways of selecting and configuring them to get the environment you need."
---

# What is a High-Performance Computer?

A high-performance computer (HPC system) is a tool used by computational scientists and engineers to tackle problems that require more computing resources or time than they can obtain on the personal computers available to them. HPC systems range in size from the equivalent of just a few personal computers to tens, or even hundreds of thousands of them.  They tend to be expensive to buy and operate, so they are often shared at the departmental or institutional level.  There are also many regional and national HPC centers.  Because of this, most HPC systems are accessed remotely, over the network.

HPC systems are generally constructed from many individual computers, similar in capability to many personal computers.  Each of these individual computers is often referred to as a **node**. HPC systems often include several different types of nodes, which are specialized for different purposes.  **Head** (or **front-end** or **login**) nodes are where you login to interact with the computer.  **Compute** nodes are where the real computing is done.  **Storage** nodes provide the specialized filesystems used on HPC systems.  Some HPC systems also have **service** nodes, which you don't usually interact with directly, but you will sometimes read about.  These nodes are connected by a network (or interconnect), which is often designed to provide very high performance as well.

<!-- It would be nice to have a diagram that showed the different types of nodes, and the network. 
Something like http://www.archer.ac.uk/training/course-material/2018/03/intro-hw/slides/L01_WhyHPC.pdf
-->

Depending on the HPC system, the compute nodes, even individually, might be much more powerful than a typical personal computer.  They often have multiple processors (each with many cores), and may have accelerators (such as GPUs) and other capabilities less common on personal computers.

In order to share these large systems among many users, it is common to allocate subsets of the compute nodes to tasks (or **jobs**), based on requests from users.  These jobs may take a long time to complete, so they come and go in time. To manage the sharing of the compute nodes among all of the jobs, HPC systems use a **batch system** or **scheduler**.  The batch system usually has commands for submitting jobs, inquiring about their status, and modifying them.  The HPC center defines the algorithms by which jobs are prioritized for execution on the compute nodes, while ensuring that the compute nodes are not overloaded. <!-- reference to episode 30 -->

The kind of computing that people do on HPC systems often involves very large files, and/or many of them.  Further, the files have to be accessible from all of the front-end and compute nodes on the system.  So most HPC systems have specialized filesystems that are designed to do a better job of meeting these needs than typical network filesystems, like NFS. Frequently, these specialized filesystems are intended to be used only for short- or medium-term storage, not permanent storage.  So HPC systems often have several different filesystems available -- for example **home**, and **scratch** filesystems.  It can be very important to select the right filesystem to get the results you want (performance or permanence are the typical trade-offs).  <!-- reference to episode 35 -->

Because HPC systems serve many users with different software needs, HPC systems often have multiple versions of commonly used software packages installed.  Since you can't easily install and use different versions of a package easily at the same time, HPC systems often use an approach called **modules**, which allows you to configure your software environment with the particular versions of software that you need. <!-- reference to episode 40 -->
