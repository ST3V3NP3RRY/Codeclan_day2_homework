users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# print(users)
Jonathan_twitter_handle = users['Jonathan']['twitter']
print(Jonathan_twitter_handle)

# 2. Get Erik's hometown
erik_hometown = users['Erik']['home_town']
print(erik_hometown)

# 3. Get the list of Erik's lottery numbers
erik_lotto_num = users["Erik"]["lottery_numbers"]
print(erik_lotto_num)

# 4. Get the species of Avril's pet Monty
avril_pet = users["Avril"]["pets"][0]["species"] # pets is a list so we need to access the index of that list before we can access the dictionary.
print(avril_pet)

# 5. Get the smallest of Erik's lottery numbers
print(min(erik_lotto_num))

# 6. Return an list of Avril's lottery numbers that are even
avril_lotto_num = users["Avril"]["lottery_numbers"]
print(avril_lotto_num)

even_numbers = []   #SET an empty list to save each even number into when we cycle through the loop

for num in avril_lotto_num:
  if num % 2 == 0:     # IF number in Avril's lotto numbers divided by 2 equals 0 
    even_numbers.append(num) # THEN add that number to empty even_numbers list

print(even_numbers)
    
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])
# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"dog": "fluffy"})
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary
users.update({"Steven":
  {
    "twitter": "ReverentSpy",
    "lottery_numbers": [3, 13, 15, 30, 36, 48],
    "home_town": "Stirling",
    "pets": [
      {
        "name": "oreo",
        "species": "hamster"
      }
    ]
  }
})
print(users["Steven"]) # Added an element to the end of the dictionary but only prints out the items after the name
#How do you print out the single user with name in front?