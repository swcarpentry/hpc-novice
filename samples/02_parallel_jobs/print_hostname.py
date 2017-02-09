#/usr/bin/env python3

from mpi4py import MPI

def print_hostname():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    hname = MPI.Get_processor_name()

    print("this is {nrank}/{nsize} running on {hname}".format(nrank=rank,nsize=size,hname=hname))

    comm.Barrier()


if __name__ == '__main__':

    print_hostname()
