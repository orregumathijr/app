'''
API END POINT FOR OFFICES
'''

'''
Define offices variable as an empty lits
'''
offices=[]
'''
Class AllOffices displays all offices
returns all offices
'''
class ModelOffice():
    '''
	get all specific office
	'''
	def get(self):
		return offices

    '''
	Post an office
	'''
	def post(self,id,type,name):
		office = {
		'status':201,
		'id':id,
		'type':type,
		'name':name
		}
		offices.append(office)
		return office,201
    
    '''
	Get a specific office
	'''
	def get(self,id):
		for office in offices:
			if office['id'] == id:
				return office
		return{'id':None}
	'''
	Delete a petition function
	'''
	def delete(self, id):
		for ind,office in enumerate(offices):
			deleted_office = offices.pop(ind)
			return{'note':'delete success '}
	
if __name__ == '__main__':
	app.run(debug=True)