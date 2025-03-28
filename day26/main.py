import pandas

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv('nato.csv')
my_dictionary = {
    row.letter:row.code for (index , row) in data.iterrows()
}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def the_main():
    try :
        name = input("Name : ").upper()
        user_name = [
            my_dictionary[letter] for letter in name
                  ]
    except KeyError:
        print("only letters from alphabet is allowed .")
        the_main()
    else :
        print(user_name)

the_main()




