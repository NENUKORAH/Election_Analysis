print("Hello World")
print(type(3))
ballots = 1,341
print(ballots)
print(type(ballots))
num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True
print(f'There are {num_candidates} candidates in the current election won by {candidate} with {winning_percentage}')
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[2])
print(len(counties))
print(counties[0:2])
print(counties[:2])
print(counties.append("El Paso"))
print(counties)
print(counties.insert(0,"Nnaemeka"))
print(counties)
print(counties.remove("Nnaemeka"))
print(counties.pop(3))
print(counties.remove("Denver"),counties.insert(1, "Test"))
print(counties)
print(counties.remove("Test"),counties.insert(1, "Denver"))
print(counties)
my_tuple = ( )
print(my_tuple)
my_dict = {'Nisha': 2019, 'Nnaemeka': 2020, 'Brian': 2020, 'Mohsin': 2021, 'Konsta': 1990}
print(my_dict)
print(len(my_dict))
print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get("Brian"))
counties = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
print(counties.keys())
voting_data = []
print(voting_data.append({"county":"Arapahoe", "registered_voters": 422829,"county":"Denver", "registered_voters": 463353,"county":"Jefferson", "registered_voters": 432438}))
print(voting_data)

if "Nnaemeka" in my_dict and "Nisha" in my_dict:
    print("Nnaemeka and Nisha are in my dictionary")
else:
    print("Nnaemeka or Nisha is not in my dictionary")

print(my_dict)
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")