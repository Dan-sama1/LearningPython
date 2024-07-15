capitals = {'Philippines': 'Manila',
            'Usa': 'Washington Dc',
            'China': 'Beijing'}

#print(capitals['Philippines'])
#print(capitals.get('Germany'))
capitals.update({'Germany': 'Berlin'})
for key,value in capitals.items():
    print(key, value)
capitals.pop('Germany')
