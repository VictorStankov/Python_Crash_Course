things = {'if': 'checks for condition',
          'strip': 'removes blank spaces',
          'title': 'makes first letters capital',
          'lower': 'makes everything in lowercase',
          'upper': 'makes everything in uppercase',
          }
print('if - ' + things['if'])
print('strip - ' + things['strip'])
print('title - ' + things['title'])
print('lower - ' + things['lower'])
print('upper - ' + things['upper'])

print("\n")

for thing, definition in things.items():
    print(thing + " - " + definition)
