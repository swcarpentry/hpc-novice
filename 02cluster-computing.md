---
layout: page
title: Cluster computing
---

1.  Queues and partitions/allocations (30 min)

    a.  Discussion of batch job scheduler, queuing and scheduling

    b.  Queue structure and priority

    c.  Job scheduler commands

    d.  **Activity:** Start an interactive session, specifying specific
        options (number of cores, notification when job finishes,
        sending output to file, runlimit, etc.)

2.  Accessing tools in the cluster by exporting PATH and using modules
    (30-45 min)

    a.  Explain the PATH variable (15-20 min)

    b.  Explain modules, discuss module commands (15-20 min)

    c.  **Activity:** perform blastn or other exercise by exporting to
        the PATH variable

    d.  **Activity:** perform blastn (or other exercise) by loading the
        blastn module (or other tool)

3.  Submission scripts and batch job submission (30 min)

    a.  Explain required components of a submission script

    b.  Display how to write a submission script for the blastn exercise
        previously performed

    c.  Discuss batch job submission

    d.  **Activity:** Change the submission script to perform batch
        submission of blastn on multiple files and monitor progress of
        job in queue.

    e.  **Activity:** Submit the same job to a different queue and see
        differences in time to job completion
