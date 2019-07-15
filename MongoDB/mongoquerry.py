from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.University

# query 1: fetch advisor with id 12345
print("# query 1: fetch advisor with id 12345 \n")
my_post = db.advisor.find_one({'s_ID': '12345'})

print(my_post)
print('\n')

# query 2: fetch student with id 99999 if exists
print("# query 2: fetch student with id 99999 if exists")
my_post2 = db.student.find_one({'id': '99999'})

if  not my_post2:
    print(my_post2)
    print('\n')
else:
    print("No record found!")
    print('\n')

# query 3: insert student and then fetch
print("# query 3: insert student with id 99999 and then fetch")
post = { 'id': '99999', 'name': 'Evan', 'dept_name': 'Comp. Sci.', 'tot_cred': '999' }

post_id = db.student.insert_one(post).inserted_id

my_post3 = db.student.find_one({'id': '99999'})

print(my_post3)
print('\n')

# query 4: update student with id 99999 and then fetch
print("# query 4: update student with id 99999 and then fetch")
uppost = { 'id': '99999', 'name': 'Zack', 'dept_name': 'Comp. Sci.', 'tot_cred': '600' }

db.student.update({'id':'99999'}, {"$set": uppost}, upsert=False)

my_post4 = db.student.find_one({'id': '99999'})

print(my_post4)
print('\n')

# query 5 remove student with id 99999 and then fetch
print("# query 5 remove student with id 99999 and then fetch")

db.student.remove({'id':'99999'})

my_post5 = db.student.find_one({'id': '99999'})

if  not my_post5:
    print(my_post5)
    print('\n')
else:
    print("No record found!")
    print('\n')
