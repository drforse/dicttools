[![Build Status](https://travis-ci.com/drforse/dicttools.svg?branch=master)](https://travis-ci.com/drforse/dicttools)

dicttools - a module for iterating over all the keys in a dictionary with recursive descending or modifying them


installation:
    `pip install -e git://github.com/drforse/dicttools.git#egg=dicttools`
    
uninstallation:
    `pip uninstall dicttools`

example:

    from dicttools import KeyTools
    me = {'me': {'age of me': 8}}
    
    def replace(s, to_replace, replacement):
        return s.replace(to_replace, replacement)
    
    he = KeyTools.edit_all_keys(obj=me, function=replace, to_replace='me', replacement='he')
    
    # he will be {'he': {'age of he': 8}}
