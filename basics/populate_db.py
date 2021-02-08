import random

f_names = ["Michael", "Christopher", "Joshua", "Matthew", "David",
 "Daniel", "Andrew", "Joseph", "Justin", "James",
 "Jessica", "Ashley", "Brittany", "Amanda", "Melissa",
 "Stephanie", "Jennifer", "Samantha", "Sarah", "Megan", "Lauren"]

l_names = ["Smith", "Johnson", "Williams", "Jones", "Brown",
 "Davis", "Miller", "Wilson", "Moore", "Taylor",
 "Anderson", "Thomas", "Jackson", "White", "Harris",
 "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]

def create_students(qty):
    for i in range(qty):
        f_name = f_names[random.randint(0,len(f_names)-1)]
        l_name = l_names[random.randint(0, len(l_names) - 1)]

        sex = random.choice(['M','F'])

        print(f"INSERT INTO student (f_name, l_name, sex) VALUES ('{f_name}', '{l_name}', '{sex}');")

create_students(10)

def create_test_scores(num_tests, num_studs):
    for i in range(num_tests):
        for j in range(num_studs):
            score = random.randrange(1,25)
            print(f"INSERT INTO test_score VALUES ({j+1}, {i+1}, {score});")

create_test_scores(4,10)