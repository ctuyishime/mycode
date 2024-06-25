x = 0

answer = "Brian"
while x < 3:
    x = x + 1
    movie_name = "Monty Python's The Life of ..."
    print(f'Finish the movie title, {movie_name}"')
    your_answer = input("Your guess ---> ")
    if your_answer == answer:
        print("Correct!")
        break
    elif x==3:
        print(f"Sorry, the answer was {answer}")
        break
    else:
        print("Sorry, try again!")



