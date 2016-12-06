# Learning Outline 

## Content

The workshop is divided into the following three sections:

### The Unix Shell

The aim of this section is not to teach learners basic unix commands,
or syntax for bash scripting,
but rather to motivate them
to **automate tasks and develop pipelines**.
Topics covered will include filesystem navigation and manipulation,
redirection and piping of standard input and output,
file permissions, and shell scripts.

### Cluster structure and scheduling

This section will be very brief. It is meant to convey a simplistic mental model of the cluster,
and how tasks get submitted, assigned and executed on the cluster. The used HPC infrastructure

At the end of the section, they will
submit a number of "Hello World" style batch jobs that are aligned to the Unix Shell section above.

### Parallel workflows

This section will guide learners through the process of
performing a large HPC simulation (code available),
and a high-throughput analysis (code available) of related data. The end goal will be to compare the simulation to the data (i.e. to relate their actions on a HPC installation to the scientific method).

For this, they will develop the workflow for a specific research scenario,
for example:

> Lola was hired by a research lab to help prepare the purchase of a multi-million dollar experiment.
The experiment is known to fail at temperatures that are too low or too high.
She knows that the temperature changes follow a daily pattern,
and she's written some code to simulate these temperature changes.
After running this code and generating the temperature predictions,
she determines how closely her predictions match the actual temperature readings
she has for every day in the last year.
The simuation would take too long to run
and generate too much data for her lab workstation,
so she will use the local University's HPC facility for this work.

