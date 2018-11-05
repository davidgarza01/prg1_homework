

def message(recipient, sender):
    print("Hello " + recipient +  ",How are you? What is up?")
    print("-" + sender)


student = "Patrick Wamsley"
teacher = "Mr.Gold"

message(student, teacher)
message(teacher, student)
message(teacher, teacher)