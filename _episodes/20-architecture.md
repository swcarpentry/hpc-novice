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
