from nested_dictionary import get_value_by_obj_key

def run_tests():
    #provided input examples
    obj1 = {"a": {"b": {"c": "d"}}}
    assert get_value_by_obj_key(obj1, "a/b/c") == "d"

    obj2 = {"x": {"y": {"z": "a"}}}
    assert get_value_by_obj_key(obj2, "x/y/z") == "a"

    #empty key path returns the object itself
    assert get_value_by_obj_key(obj1, "") == obj1

    #missing/wrong path returns default
    assert get_value_by_obj_key(obj1, "a/b/k") is None
    assert get_value_by_obj_key(obj1, "a/b/k", default="NOT FOUND") == "NOT FOUND"

    #raise on missing
    try:
        get_value_by_obj_key(obj1, "a/b/k", raise_on_missing=True)
    except KeyError:
        pass
    else:
        raise AssertionError("KeyError for missing key")

    # intermediate value is not a nested_dictionary
    obj3 = {"a": {"b": "not-a-dict"}}
    assert get_value_by_obj_key(obj3, "a/b/c") is None
    try:
        get_value_by_obj_key(obj3, "a/b/c", raise_on_missing=True)
    except KeyError:
        pass
    else:
        raise AssertionError("KeyError when descending into non-dict")

    print("Tests passed!")

if __name__ == "__main__": run_tests()