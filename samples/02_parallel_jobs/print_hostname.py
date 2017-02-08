#/usr/bin/env python3

from mpi4py import MPI


def print_hostname():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    hname = MPI.Get_processor_name()


    print("this is {nrank} running on {hname}".format(nrank=rank,hname=hname))

if __name__ == '__main__':

    print_hostname()
