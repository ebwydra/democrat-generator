import random
import tweepy
# from twitterauth import *
from os import environ
import time

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class Candidate:
     def __init__(self, first, last, role, state, slogan=None):
         self.first = first
         self.last = last
         self.role = role
         self.state = state
         self.slogan = slogan

bennet = Candidate('Michael', 'Bennet', 'U.S. Senator', 'CO', 'Building Opportunity Together')
biden = Candidate('Joe', 'Biden', 'Vice President', 'DE', 'Our Best Days Still Lie Ahead')
booker = Candidate('Cory', 'Booker', 'U.S. Senator', 'NJ', 'Together, America, We Will Rise')
bloomberg = Candidate('Mike', 'Bloomberg', 'Mayor', 'NY', 'Rebuild America')
bullock = Candidate('Steve', 'Bullock', 'Governor', 'MT', 'A Fair Shot For Everyone')
buttigieg = Candidate('Pete', 'Buttigieg', 'Mayor', 'IN', 'Win The Era')
castro = Candidate('Julian', 'Castro', 'Secretary of Housing and Urban Development', 'TX', 'One Nation. One Destiny.')
deblasio = Candidate('Bill', 'de Blasio', 'Mayor', 'NY', 'Working People First')
delaney = Candidate('John', 'Delaney', 'U.S. Representative', 'MD', 'Focus On The Future')
gabbard = Candidate('Tulsi', 'Gabbard', 'U.S. Representative', 'HI', 'Lead With Love')
gillibrand = Candidate('Kirsten', 'Gillibrand', 'U.S. Senator', 'NY', 'Brave Wins')
gravel = Candidate('Mike', 'Gravel', 'U.S. Senator', 'AK', 'No More Wars')
harris = Candidate('Kamala', 'Harris', 'U.S. Senator', 'CA', 'For The People')
hickenlooper = Candidate('John', 'Hickenlooper', 'Governor', 'CO', 'Come Together')
inslee = Candidate('Jay', 'Inslee', 'Governor', 'WA', 'Our Moment')
klobuchar = Candidate('Amy', 'Klobuchar', 'U.S. Senator', 'MN', "Let's Get To Work")
messam = Candidate('Wayne', 'Messam', 'Mayor', 'FL', 'Wayne For America')
moulton = Candidate('Seth', 'Moulton', 'U.S. Representative', 'MA', 'Seth Moulton For America')
orourke = Candidate('Beto', "O'Rourke", 'U.S. Representative', 'TX', "We're All In This Together")
patrick = Candidate('Deval', 'Patrick', 'Governor', 'MA', 'Deval For All')
ryan = Candidate('Tim', 'Ryan', 'U.S. Representative', 'OH', 'Our Future Is Now')
sanders = Candidate('Bernie', 'Sanders', 'U.S. Senator', 'VT', 'Not Me. Us.')
sestak = Candidate('Joe', 'Sestak', 'U.S. Representative', 'PA', 'Accountability For America')
steyer = Candidate('Tom', 'Steyer', 'Billionaire', 'CA', 'Actions Speak Louder Than Words')
swalwell = Candidate('Eric', 'Swalwell', 'U.S. Representative', 'CA', 'Go Big. Be Bold. Do Good.')
warren = Candidate('Elizabeth', 'Warren', 'U.S. Senator', 'MA', 'Dream Big, Fight Hard')
williamson = Candidate('Marianne', 'Williamson', 'Author', 'CA', 'Join The Evolution')
yang = Candidate('Andrew', 'Yang', 'Entrepreneur', 'NY', 'Humanity First')

candidate_list = [bennet, biden, booker, bloomberg, bullock, buttigieg, castro, deblasio, delaney, gabbard, gillibrand, gravel, harris, hickenlooper, inslee, klobuchar, messam, moulton, orourke, patrick, ryan, sanders, sestak, steyer, swalwell, warren, williamson, yang]

verb_list = ['Double', 'Triple', 'Abolish', 'Eliminate', 'Reduce', 'Establish', 'Re-establish', 'Increase', 'Save', 'Secure', 'Decrease', 'Ensure', 'Generate', 'Limit', 'Fight for', 'Tackle', 'End', 'Cancel', 'Fix', 'Raise', 'Build Up', 'Protect', 'Address', 'Reform', 'Stop', 'Legalize', 'Decriminalize', 'Criminalize', 'Prioritize', 'Invest in', 'Combat', 'Increase Funding for', 'Cut Funding for', 'Restrict']

noun_list = ['Climate Change', 'Racial Justice', 'the National Debt', 'Maternal Mortality', 'Higher Education', 'American Jobs', 'Universal Health Care', 'the Opioid Crisis', 'Taxes', 'Affordable Housing', 'Green Jobs', 'the Economy', 'Gun Violence', 'LGBTQ+ Rights', 'Infectious Disease Outbreaks', 'Term Limits', 'Corruption', 'Immigration', 'Student Loan Debt', 'the State Department', 'the Defense Budget', 'Our Troops', 'America', 'the Affordable Care Act', 'Marijuana', 'Universal Basic Income', 'Global Warming', 'Renewable Energy', 'the Cost of Prescription Drugs', 'Voting Rights', 'Voter Suppression', 'the Debt Ceiling', 'Cybersecurity', 'the Minimum Wage', 'Roe v. Wade', 'the Supreme Court', "Workers' Rights", 'Fuel Economy Standards', 'Fracking', 'Offshore Drilling', 'Funding for Planned Parenthood', 'Outsourcing of Jobs Overseas', 'Domestic Terrorism', 'National Security', 'Paid Family Leave', 'Universal Childcare', 'the First Amendment', 'the Second Amendment', 'Endless Wars']

def generatecandidate():
    first = random.choice(candidate_list).first
    last = random.choice(candidate_list).last
    role = random.choice(candidate_list).role
    state = random.choice(candidate_list).state
    slogan = random.choice(candidate_list).slogan
    if slogan == 'Deval For All':
        slogan = first + " For All"
    if slogan == 'Wayne For America':
        slogan = first + " For America"
    if slogan == 'Seth Moulton For America':
        slogan = first + " " + last + " for America"

    verb = random.choice(verb_list)
    noun = random.choice(noun_list)

    women_names = ['Tulsi', 'Kirsten', 'Kamala', 'Amy', 'Elizabeth', 'Marianne']
    if first in women_names:
        pronoun = "her"
    else:
        pronoun = "his"

    result = first + " " + last + ", " + role + " from " + state + ' - "' + slogan + '"'
    result += "\nIn " + pronoun + " first 100 days in office, " + first + " will: \n1. " + random.choice(verb_list) + " " + random.choice(noun_list) + "\n2. " + random.choice(verb_list) + " " + random.choice(noun_list) + "\n3. " + random.choice(verb_list) + " " + random.choice(noun_list)

    return result

while True:
    result = generatecandidate()
    api.update_status(status = result)
    time.sleep(60*60*4) # every four hours
