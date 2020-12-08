class RockBand:
    genre = 'rock'
    key_instruments = ["electric guitar", "drums"]
    n_members = 4


linkin_park = RockBand()
print(linkin_park.genre)
print(linkin_park.n_members)
print(linkin_park.key_instruments)


"""
Let's rock
There are many bands in the world that perform all kinds of music. 
Let's suppose for a second that you're a fan of rock and want to create a program that deals with rock bands.

For that, you obviously need the class RockBand with such attributes as genre ("rock") and key_instruments 
(by default, a list ["electric guitar", "drums"]). 
Let's also, for the sake of simplicity, assume n_members to be a class attribute equal to 4, 
since most rock bands do have 4 members.

Create this class and an object of that class: name the variable after any rock band that you like. 
Print the attributes of your rock band on separate lines in this order: genre, n_members, key_instruments.

Hint

Make sure that the attributes have correct types: genre is a string, n_members is an integer, 
and key_instruments is a list.

Caution
You may see errors in your code or execution results due to missing context. 
Don’t worry about it, just write the solution and press Check.
"""