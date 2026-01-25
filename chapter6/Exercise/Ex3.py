p1 = "good choice"
p2  = "limited time"
p3 = "hurry"

comment = input("Enter your comment")
if((p1 in comment) or (p2 in comment) or (p3 in comment)):
    print("This comment is spam")
else:
    print("This comment is not a spam")
