contacts = {
    "Anne" : "anne@example.com",
    "Robert" : "robert@example.com",
    "Zbyszek" : "address unknown"
}

contacts ["Kamila"] = "specialgirl@example.com"

print (type(contacts)) # <class 'dict'>
print (contacts)

print (contacts["Zbyszek"]) # address unknown

print (len(contacts)) # 4 elements
print (contacts.keys () ) # dict_keys(['Anne', 'Robert', 'Zbyszek', 'Kamila'])
print (contacts.values () )
#dict_values(['anne@example.com', 'robert@example.com', 'address unknown', 'specialgirl@example.com'])

for key in contacts:
    print (key + "-" + contacts[key]) 

for key, value in contacts.items():
    print (key, value)

