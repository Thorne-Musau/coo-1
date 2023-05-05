# DICTIONARIES
D = {'a':0,'b':1,'c':2}
print(D.values())
# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict

# accessing keys
print(release_year_dict['Thriller'])

# Retreiving the keys
print(release_year_dict.keys())

# Getting all keys in the dictionary
print(release_year_dict.keys())

# Append value with a key into the dictionary
release_year_dict['Graduation'] = '1984'

#deleting entries by key
del release_year_dict['Thriller']

#verify the key is in the dictionary
print('The Bodyguard' in release_year_dict) # returns a bool