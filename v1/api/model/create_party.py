from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)
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
class AllParties(Resource):
	def get(self):
		return parties, 200
'''
Class CreateParty is for adding a parties
It has 4 parameters and returns back the parties
'''
class CreateParty(Resource):
	def post(self,id,name,logo):
		party = {
		    'id':id,
			'name':name,
			'Logo Url':logo
		}
		parties.append(party)
		return party, 201

'''
Class ManageParty has two functions
1. get function that loops through the parties and gives out the intended partY
2. Delete method that deletes a specified partY
'''
class ManageParty(Resource):
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


app.run(debug=True)