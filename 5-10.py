current_user = ["a"]
New = ["a","b"]
for user in current_user:
    for N_user in New:
        if N_user == user:
            print(f"sorry the username ({user}) is taken")
    else:
        print(f"Your new username is {N_user}")