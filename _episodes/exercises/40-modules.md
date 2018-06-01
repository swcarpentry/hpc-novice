> ##  Using Default Modules
>
> Consider the following output from `module available`.
>
>    ------------------------- /opt/moose/Modules/versions --------------------------
>    3.2.10
>
>    -------------------- /opt/moose/Modules/3.2.10/modulefiles ---------------------
>    ...
>       python/2.7.3
>       python/2.7.10
>       python/2.7.11
>       python/3.4.3                        (D)
>       python3/3.4
>       python3/3.4.1
>       python3/3.5.2                       (D)
>       python3/3.6.2
>    ...
>
>What command would you run to load the default Python environment?
>
> > ## Solution
> > `module load python3` or `module add python3`
> {: .solution}
{: .challenge}

> ##  Using Specific Modules
>
> Based on the previous example, what command would you run to load the Python 3.6.2 environment?
>
> > ## Solution
> > `module load python3/3.6.2`
> {: .solution}
{: .challenge}


> ##  Changing the `$PATH`
>
> Begin a new terminal session on the machine you are using remotely.  Echo the `$PATH` to the screen:
>
>    echo $PATH
>
> Load a module of your choice:
>
>    module load python
>
> What change was made to your `$PATH` as a result of the `module load` command?
{: .challenge}

> ##  Finding a Module
>
> The `module keyword` command searches the descriptions of modules for a keyword.  If you are attempting to locate a module which supports a particular command, this is a reasonable first pass at locating such a module.
>
> On your remote system, attempt to locate a package which supports one of the following software systems:  `matlab`, `python`, `openmpi`, `mvapich`, `mpich2`.   Installations vary, so your instructor may suggest another suitable package for you to locate this way.
{: .challenge}
