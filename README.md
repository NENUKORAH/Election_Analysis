# Election_Analysis

## Overview of Election Audit

The purpose of this challenge is to assist Tom, a Colorado board of elections employee in an election audit of the tabulated results of US congressional precincts in Colarado.

I am tasked with reporting the following;

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the Percentage of votes each candidate won.
5. The winner of the election based on popular vote.

The election audit results have been submitted to the Election commission. 

However, the Election commission requires the following additional information;

* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

I will be modifying the python code using repetition statements, conditional statements with logical operators, and print statements to 
provide the additional information to the Election commission.

### Resources

The following resources were used for the election audit;

* Data Source: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.56.0

## Election Audit Results

The analysis of the election shows that:

* There were 369,711 votes cast in the election.

* The candidates were:

  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane

* The candidate results were:

  * Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
  * Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  * Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

* The winner of the election was:

  * Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

* The voter turnout for each county were;

  * Jefferson county had a total voter turnout of 38,855.
  * Denver county had a total voter turnout of 306,055.
  * Arapahoe county had a total voter turnout of 24,801.

* The percentage of votes from each county out of the total count were as follows;

  * Jefferson county had 10.5% of the total vote count.
  * Denver county had 82.8% of the total vote count.
  * Arapahoe county had 6.7% of the total vote count.

* The county with the highest turnout was;

  * Denver County, with 82.8% of the total vote and 306,055 voter turnout.

### Election Results Printed to the Command Line

![Election_Result-Terminal](https://user-images.githubusercontent.com/81701640/117550066-19919700-b00c-11eb-942a-c9f152ccb279.png)

### Election Results Saved to a Text File

![Election_Result_text](https://user-images.githubusercontent.com/81701640/117550190-eef40e00-b00c-11eb-86ce-96eea0f31165.png)

### Modified Code for the Election Audit

```python

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_number_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        vote_county = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        vote_county_percentage = float(vote_county) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {vote_county_percentage:.1f}% ({vote_county:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (vote_county > winning_count):
            #2. If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = vote_county
            largest_county_turnout = county_name

    # 7: Print the county with the largest turnout to the terminal.
        largest_county_results = (
        f"\n"
        f"----------------------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"----------------------------------------\n")
    print(largest_county_results)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_results)

```

## Election Audit Summary

This python code can be used to audit not only other congressional districts, but also senatorial districts, local elections and state
elections.

Firtly, the code can be modified to show candidate performance by counties. This will tell how popular the candidates are in each county.

Secondly, the code can be used in state elections by uploading state election information and modifying the code to display states election results 
instead of election result by county.

Finally, more information can be provided such as voter demographic information. The code can be modified to show voter demographic information 
such as age, state of origin and political ideology. This will help in studying electoral voting patterns.

**Nnaemeka Enukorah**

**8th May, 2021**


