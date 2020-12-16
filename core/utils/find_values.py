from json import loads

def find_values(json_repr, id):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    loads(json_repr, object_hook=_decode_dict)  # Return value ignored.
    return results

