'''
API END POINT FOR CREATING A PARTIES
'''

'''
Define parties variable as an empty lits
'''
parties = []

'''
Class AllParties displays all parties
returns all parties
'''
class ModelParty():
	def get(self):
		return parties, 200
    '''
	Get a specific party
	'''
	def post(self,id,name,logo):
		party = {
		    'id':id,
			'name':name,
			'Logo Url':logo
		}
		parties.append(party)
		return party, 201

    '''
	Get a specific party 
	'''
	def get(self,id):
		for party in parties:
			if party['id'] == id:
				return party
		return {'id':None},200

	'''
	Delete a party function
	'''
	def delete(self, id):
		for ind,party in enumerate(parties):
			deleted_party = parties.pop(ind)
			return{'note':'delete success '}, 200

if __name__ == '__main__':
	app.run(debug=True)