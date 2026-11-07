q1 = "What time does school start?"
a1 = "School starts at 8:30 AM"

q2 = "Where is the library?"
a2 = "The library is on the second floor"

q3 = "When is lunch?"
a3 = "Lunch is at 12:15 PM"

q4 = "Who is the principal?"
a4 = "The principal is Mrs. Rao"

print("Helpdesk Bot:")

while True:
    prompt = input("Question: ")

    if prompt.lower().replace(" ","") in q1.lower().replace(" ",""):
        print(f"Response: {a1}")
    elif prompt .lower().replace(" ","") in q2.lower().replace(" ",""):
        print(f"Response: {a2}")
    elif prompt.lower().replace(" ","") in q3.lower().replace(" ",""):
        print(f"Response: {a3}")
    elif prompt.lower().replace(" ","") in q4.lower().replace(" ",""): 
        print(f"Response: {a4}")
    else:
        print("Sorry, I do not know that.")