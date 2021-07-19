People = ["Akshat", "Faiz"]
People.insert(0,"Shreyash")
People.insert(1,"Ishan")
People.append("Ali")
print(f"These people are now invited to my party\t\n{People}\n")
print("my dining table will not arrive in time sorry but some people will not be invited")
Ali = People.pop()
print(f"{Ali} sorry you are no longer invited")
Faiz = People.pop()
print(f"{Faiz} sorry you are no longer invited")
AKshat = People.pop()
print(f"{AKshat} sorry you are no longer invited")
print(f"{People} Hey you are still invited")
print(f"The people that can't go are {Ali.title()},{Faiz.title()},{AKshat.title()}")
del People[1]
del People[0]
print(People)
print(len(People))