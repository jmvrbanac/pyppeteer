import cffi

# Constant from prctl.h
PR_SET_PDEATHSIG = 1

ffi = cffi.FFI()
ffi.cdef('int prctl (int __option, ...);')
lib = ffi.dlopen(None)


def set_pdeathsig(signal):
    lib.prctl(PR_SET_PDEATHSIG, ffi.cast('int', signal))
