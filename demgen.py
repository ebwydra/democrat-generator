import random

'''
Attributes that candidates have:
- first
- last
- role
- state
'''

class Candidate:
     def __init__(self, first, last, role, state):
         self.first = first
         self.last = last
         self.role = role
         self.state = state

bennet = Candidate('Michael', 'Bennet', 'U.S. Senator', 'CO')
biden = Candidate('Joe', 'Biden', 'Vice President', 'DE')
booker = Candidate('Cory', 'Booker', 'U.S. Senator', 'NJ')
bloomberg = Candidate('Mike', 'Bloomberg', 'Mayor', 'NY')
bullock = Candidate('Steve', 'Bullock', 'Governor', 'MT')
buttigieg = Candidate('Pete', 'Buttigieg', 'Mayor', 'IN')
castro = Candidate('Julian', 'Castro', 'Secretary of Housing and Urban Development', 'TX')
deblasio = Candidate('Bill', 'de Blasio', 'Mayor', 'NY')
delaney = Candidate('John', 'Delaney', 'U.S. Representative', 'MD')
gabbard = Candidate('Tulsi', 'Gabbard', 'U.S. Representative', 'HI')
gillibrand = Candidate('Kirsten', 'Gillibrand', 'U.S. Senator', 'NY')
gravel = Candidate('Mike', 'Gravel', 'U.S. Senator', 'AK')
harris = Candidate('Kamala', 'Harris', 'U.S. Senator', 'CA')
hickenlooper = Candidate('John', 'Hickenlooper', 'Governor', 'CO')
inslee = Candidate('Jay', 'Inslee', 'Governor', 'WA')
klobuchar = Candidate('Amy', 'Klobuchar', 'U.S. Senator', 'MN')
messam = Candidate('Wayne', 'Messam', 'Mayor', 'FL')
moulton = Candidate('Seth', 'Moulton', 'U.S. Representative', 'MA')
ojeda = Candidate('Richard', 'Ojeda', 'State Senator', 'WV')
orourke = Candidate('Beto', "O'Rourke", 'U.S. Representative', 'TX')
patrick = Candidate('Deval', 'Patrick', 'Governor', 'MA')
ryan = Candidate('Tim', 'Ryan', 'U.S. Representative', 'OH')
sanders = Candidate('Bernie', 'Sanders', 'U.S. Senator', 'VT')
sestak = Candidate('Joe', 'Sestak', 'U.S. Representative', 'PA')
steyer = Candidate('Tom', 'Steyer', 'Billionaire', 'CA')
swalwell = Candidate('Eric', 'Swalwell', 'U.S. Representative', 'CA')
warren = Candidate('Elizabeth', 'Warren', 'U.S. Senator', 'MA')
williamson = Candidate('Marianne', 'Williamson', 'Author', 'CA')
yang = Candidate('Andrew', 'Yang', 'Entrepreneur', 'NY')

candidate_list = [bennet, biden, booker, bloomberg, bullock, buttigieg, castro, deblasio, delaney, gabbard, gillibrand, gravel, harris, hickenlooper, inslee, klobuchar, messam, moulton, ojeda, orourke, patrick, ryan, sanders, sestak, steyer, swalwell, warren, williamson, yang]

# print(len(candidate_list))
first = random.choice(candidate_list).first
last = random.choice(candidate_list).last
role = random.choice(candidate_list).role
state = random.choice(candidate_list).state

print(first + " " + last + ", " + role + " from " + state)
