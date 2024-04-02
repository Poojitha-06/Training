                                                          #1.4 DICTIONARIES

#1.41 Creating dictionary and printing the value of the one member
       friends_age={"Rolf":24,"Bob":20}
       print(friends_age["Rolf"])
  
output: 24

#1.42 To change the assigned value and add a new value to the existing dictionary:
      friends_age={"Rolf":24,"Bob":20}
      friends_age["Rolf"]=26
      friends_age["Anne"]=18
      print(friends_age)

output:{"Rolf":26,"Bob":20,"Anne":18} 

#1.43 To print the dictionary value by using there index number:
      friends=(
              {"name":"RolfSmith","age":24},
              {"name":"Poojitha","age":18},
              {"name":"Anitha","age":46}
              )
     print(friends[0]["name"])
     print(friends[1]["name"])
     print(friends[2]["name"])

output: "RolfSmith"
        "Poojitha"
        "Anitha"