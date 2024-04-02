                                                    #1.3 LIST,TUPLE,and SETS basic codes

1.31. friends=["Rolf,"Bob","Anne"]
      print(friends)

output: "Rolf,"Bob","Anne"

1.32. # Accepting the member by using the index number:
      friends=["Rolf,"Bob","Anne"]
      print(friends[2])

output: "Anne"

1.33 # Printing the length of the list:
       friends=["Rolf","Bob","Anne","Jen","Charlie"]
       print(len(friends))

output: 5

1.34 #To add and remove an element from a list:
      friends=["Rolf","Bob","Anne"]
      friends.append("Jen")
      print(friends)

output: ["Rolf","Bob","Anne","Jen"]

      friends.remove("Bob")
      print(friends)

output:["Rolf","Anne"]

1.35 #To add elements to a tuple:
      friends=("Rolf","Bob","Anne")
      friends=friends+("Jen")
      print(friends)

output:("Rolf","Bob","Anne","Jen")

1.36 #Advanced Set operations
    1. art_friends={"Rolf","Bob","Anne"}
     science_friends={"Bob","Charlie"}
     art_but_not_science=art_friends.difference(science_friends)
     science_but_not_art=science_friends.difference(art_friends)
     print(art_but_not_science)
     print(science_but_not_art

output: {"Anne","Rolf"}
        {"Charlie"}

    2. not_in_both=art_friends.symmetric_difference(science_friends)
       print(not_in_both)

output: {"Anne","Rolf","Charlie"}

   3.  art_and_science=art_friends.intersection(science_friends)
       print(art_and_science)

output: {"Bob"}

   4.  all_friends=art_friends.union(science_friends)
       print(all_friends)

output: {"Rolf","Bob","Anne","Charlie"}

 