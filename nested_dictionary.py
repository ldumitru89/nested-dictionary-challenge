def get_value_by_obj_key(obj, key_path, sep='/', default=None, raise_on_missing=False):
    if key_path == "" or key_path is None:
        return obj
    this = obj
    parts = key_path.split(sep)

    for i, part in enumerate(parts):
        if isinstance(this, dict):
            if part in this:
                this = this[part]
            else:
                if raise_on_missing:
                    raise KeyError(f"Key '{part}' not found at level {i} (path: '{key_path}')")
                return default
        else:
            #object is not a dictionary
            if raise_on_missing:
                raise KeyError(
                f"Non-dictionary object at level {i} ('{part}'). "
                f"Current value: {this!r}"
                )
            return default
    return this
