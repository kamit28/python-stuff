'''
Created on 19 Mar. 2018

@author: Amit
'''
import tempfile, shutil

from contextlib import contextmanager

@contextmanager
def tempdir():
    dirname = tempfile.mkdtemp()
    try:
        yield dirname
    finally:
        shutil.rmtree(dirname)
