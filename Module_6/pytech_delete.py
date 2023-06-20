#pytech_delete

# Get the database instance 
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.ympg28b.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)

# pytech database
pytech = client.pytech


students = pytech.students

docs = students.find()

print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()
    
#new student info
new_student = {
        "student_id": "1010",
        "first_name": "Jack",
        "last_name": "Johnson"
    }

# insert new student
document_id = students.insert_one(new_student).inserted_id
 
 #insert statements
print ("-- INSERT STATEMENTS --")   
print (f"Inserted student record into the students collection with document_id {document_id}")   
        
          
# # display a single document by student_id
print ("-- DISPLAYING STUDENT TEST DOC --")

doc = students.find_one({"student_id": "1010"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print ()

# #delete student 1010
doc=students.delete_one({"student_id": "1010"})


docs = students.find()

print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()

print ("End of program, press any key to continue...")   
