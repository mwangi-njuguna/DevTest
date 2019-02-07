def search(collection, value_to_find):
    first_item = 0 
    last_item = len(collection)
    sorted_collection = sorted(collection)
    value_found = False

    while first_item<=last_item and not value_found:
        try:
            midpoint = (first_item + last_item)//2
            if sorted_collection[midpoint] == value_to_find:
                value_found = True
                return collection.index(sorted_collection[midpoint])
            else:
                if value_to_find < sorted_collection[midpoint]:
                    last_item = midpoint - 1
                else:
                    first_item = midpoint + 1
        except IndexError:
            return -1
