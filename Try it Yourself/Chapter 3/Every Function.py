mountains=['Rila','Pirin','Stara planina','Strandzha','Belasitsa']
mountains.insert(1, 'Rodopa')
mountains.append('Vitosha')
too_unpopular='Strandzha'
mountains.remove(too_unpopular)
mountains.pop(4)
print(sorted(mountains))
print(sorted(mountains, reverse=True))
mountains.reverse()
print(mountains)
