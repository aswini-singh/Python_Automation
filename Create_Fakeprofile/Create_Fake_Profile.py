from faker import Faker
fake = Faker(['en_IN', 'en_US', 'fr_FR','en_UK','en_PA'])
print(" ALL FAKER DETAILS ")
print(dir(fake))

summary = '''

# Faker profile Summery 

Name : {}
Address : {}
phone_number : {}
Email : {}
Social_Security_number(SSN) : {}
Location : {},{} 
URL : {}
'''. format(fake.name(),
            fake.address(),
            fake.phone_number(),
            fake.email(),
            fake.ssn(),
            fake.latitude(), fake.longitude(),
            fake.url())

print(summary)
