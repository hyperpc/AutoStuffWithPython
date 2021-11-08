import census2010

print(census2010.allData['AK']['Anchorage'])
#{'pop':291826, 'tracts':'55'}
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))