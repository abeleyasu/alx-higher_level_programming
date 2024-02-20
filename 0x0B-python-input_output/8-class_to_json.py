#!/usr/bin/python3

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary description of the object.
    """
    # Get all attributes of the object
    obj_dict = obj.__dict__.copy()

    # Check for attributes that are instances of classes
    for key, value in obj_dict.items():
        if hasattr(value, '__dict__'):
            obj_dict[key] = value.__dict__

    return obj_dict
