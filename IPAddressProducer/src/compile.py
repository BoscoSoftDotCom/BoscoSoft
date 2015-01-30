'''
Created on Jan 23, 2015

@author: gstumpf
'''

from distutils.core import setup
import py2exe

def main(): 
    setup(console=['IPAddressNotifier.py'])

if __name__ == '__main__':
    main()