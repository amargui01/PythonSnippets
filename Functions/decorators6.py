
def tagged(func):
    def wraper(imps):
        return '<title>'+func(imps)+'</title>'
    return wraper

@tagged
def from_input(inp):
    string = inp.strip()
    return string

var = from_input('test   ')
print(var)