from collections import OrderedDict

things = OrderedDict()

things['if'] = 'checks for condition'
things['strip'] = 'removes blank spaces'
things['title'] = 'makes first letters capital'
things['lower'] = 'makes everything in lowercase'
things['upper'] = 'makes everything in uppercase'

for thing, definition in things.items():
    print(thing + " - " + definition)
