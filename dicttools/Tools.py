# All rights for this file belong to George Imedashvili <george.lifeslice@gmail.com>. Do NOT edit these comments
# You can copy this file, modify it (but don't edit these comments) and use in your own project for free

import typing


class KeyTools:
    def __init__(self):
        pass

    @classmethod
    def __has_dicts(cls, __obj: typing.Union[list, tuple, dict]):
        """
        Check if there is any dictionaries inside a list, a tuple or a dict

        :param __obj: a list, a tuple, or a dict to check
        :return: boolean
        """
        if not isinstance(__obj, (list, tuple, dict)):
            return False
        for i in __obj:
            if type(i) == dict:
                return True
            if isinstance(i, (list, tuple, dict)) and not type(i) == str:
                return cls.__has_dicts(i)
            return False

    @classmethod
    def edit_all_keys(cls, obj: dict, function: typing.Callable, **kwargs):
        """
        Edit ALL the keys in a given dictionary with recursive descending with a given function

        :param obj: a dictionary to edit
        :param function: function to edit the keys, should have a key parameter as the first one
        :param kwargs: should be **kwargs to your function
        :return: new dictionary with edited keys
        """
        new_dict = {}
        for key in obj:
            if not isinstance(key, (list, tuple, dict)):
                new_dict[function(key, **kwargs)] = obj[key]
            if type(obj) == dict and type(obj[key]) == dict or type(obj) == dict and cls.__has_dicts(
                    obj[key]):
                new_dict[function(key, **kwargs)] = cls.edit_all_keys(obj[key], function, **kwargs)
            elif cls.__has_dicts(obj):
                to_return = []
                for k in obj:
                    to_return.append(cls.edit_all_keys(obj[obj.index(k)], function, **kwargs))
                return type(obj)(to_return)
        del obj
        return new_dict

    @classmethod
    def iter_all_keys(cls, dictionary):
        """
        Iter over ALL the keys in a given dictionary with recursive descending

        :param dictionary: a dictionary to iter over
        :return: generator
        """
        for key in dictionary:
            if not isinstance(key, (list, tuple, dict)):
                yield key
            if type(dictionary) == dict and type(dictionary[key]) == dict or type(dictionary) == dict and cls.__has_dicts(dictionary[key]):
                for k in cls.iter_all_keys(dictionary[key]):
                    yield k
            elif cls.__has_dicts(dictionary):
                for k in dictionary:
                    for input_key in cls.iter_all_keys(dictionary[dictionary.index(k)]):
                        yield input_key
