import typing

from flask import request


def acquire_files(param_name: str) -> typing.List:
    """
    The get files function in flask includes Two ways, if the judgment is in the application layer,
    the code will be more redundancy. So this function will solve this problem.
    This function can replace request.files.get() and request.files.getlist().
    This function return a file list.
    """
    data = request.files.getlist(param_name)
    if data != []: return data

    data = request.files.get(param_name)
    if data != None:
        data_list = []
        data_list.append(data)
        return data_list

    return []
