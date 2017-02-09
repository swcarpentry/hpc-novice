---
title: "Parallel Execution"
teaching: 90
exercises: 0
questions:
- "How do I execute a compute job that uses multiple nodes at once?"
- "How do I analyze multiple large files on a cluster the best way?"
objectives:
- "Explain how message passing allows performing computations in more than 1 computer at the same time."
- "Observe the effects of parallel execution of commands with a simple hostname call."
- "Perform a calculation of pi on multiple nodes with 8 CPUs."
- "Perform a serial analysis on a lot of large files to extract a given text token."
- "Map the serial execution of independent analysis steps onto a cluster of compute nodes that are connected by a parallel file system."
- "Perform a Map-Reduce style operation to extract information from large files and collect these into one final answer."
keypoints:
- "The mpi dirver `mpirun` sends compute jobs to a set of allocated computers."
- "The mpi software then executes these jobs on the remote hosts and synchronizes their state/memory."
- "The mpi software is controlled from the binaries to allow custom synchronization."
- "The `print_hostname.py` program is likely to run on different machines and print different hostnames for some ranks."
---
