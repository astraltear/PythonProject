def split(line, types=None, delimeter=None):
    fields = line.split(delimeter)

    if types:
        fields=[ ty(val) for ty,val in zip(types,fields)]
    return fields
