---
layout: page
title: High Performance Computing
---
1.  Introduction to HPC and accessing the cluster (30-45 min)

    a.  Discussion of computer components (CPU, storage, memory)

    b.  Explanation of terminology (nodes, cores, threads, cluster,
        serial/parallel processes)

    c.  Structure of the cluster (login nodes, job scheduler, etc.)

    d.  Accessing the cluster with ssh and discussion of cluster
        filesystem set-up

    e.  **Activity:** practice navigating the filesystem using Unix
        commands – navigate between /home and /groups

2.  Transferring files to/from the cluster (20-30 min)

    a.  Filezilla and scp (macs only)

    b.  **Activity:** transferring files to/from cluster

3.  Queues and partitions/allocations (30 min)

    a.  Discussion of batch job scheduler, queuing and scheduling

    b.  Queue structure and priority

    c.  Job scheduler commands

    d.  **Activity:** Start an interactive session, specifying specific
        options (number of cores, notification when job finishes,
        sending output to file, runlimit, etc.)

4.  Accessing tools in the cluster by exporting PATH and using modules
    (30-45 min)

    a.  Explain the PATH variable (15-20 min)

    b.  Explain modules, discuss module commands (15-20 min)

    c.  **Activity:** perform blastn or other exercise by exporting to
        the PATH variable

    d.  **Activity:** perform blastn (or other exercise) by loading the
        blastn module (or other tool)

5.  Submission scripts and batch job submission (30 min)

    a.  Explain required components of a submission script

    b.  Display how to write a submission script for the blastn exercise
        previously performed

    c.  Discuss batch job submission

    d.  **Activity:** Change the submission script to perform batch
        submission of blastn on multiple files and monitor progress of
        job in queue.

    e.  **Activity:** Submit the same job to a different queue and see
        differences in time to job completion

6.  MPI and multithreading (30 min)

    a.  Types of parallelism and MPI concepts

    b.  **Activity:** Submit a script that depends on MPI


This is the lesson plan that Calcul Québec is planning to give as its "First steps on an HPC cluster". The prerequisites are Unix command line. 

1. Introduction to advanced computing (30 minutes)
   
    a. Vocabulary, components of a computer and structure of a cluster

    b. Basic parallelism concepts
    
    c. **Activity:** Connecting to the cluster
    
2. File transfer from/to the cluster using Globus (30 minutes)

    a. Explain what is Globus at Compute Canada/Calcul Québec, what are its advantages over SCP
    
    b. **Activity:** Creating a Globus account, installing the Globus client on their computer, transfering files to/from the cluster using Globus
    
3. Using modules (15 minutes)

    a.  Explain modules, discuss module commands

    b.  **Activity:** load modules required for Python, list modules that are loaded by default
    
4. Using the scheduler (2 hours)

    a. Discuss why we use a scheduler, what it implies  (10 minutes)
    
    b. Submission script, required resources, mandatory options, and where to find information about other clusters (20 minutes)
    
    c. Job diagnostic (10 minutes)
    
    d. **Activity:** Based on attendance, a choice of (plan 30-40 minutes for each)
    
       * Sequential tasks within a job using "&" and "wait"
       * Short jobs using GNU Parallel
       * Job arrays
       * OpenMP jobs
       * MPI jobs
       * Jobs with checkpointing support
       * Advanced options of the scheduler
       

5. Conclude with common mistakes and good practices advices
    a. Common mistakes include :
       * Assuming that because you run your program on a supercomputer, it will run faster. 
       * Uploading Windows files to a Linux system and having the wrong end of line encoding (show them dos2unix/unix2dos)
       * Starting jobs on the login nodes
       * Doing a lot of small input/output on the filesystem
       * Submitting a lot of very short jobs
       * Requesting more than one node for non-MPI programs
       * Requesting too much memory (more than available in any cluster node)
