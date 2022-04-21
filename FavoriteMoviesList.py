# CITC-2391-C01 Summer 2020
# Program 1
# Name: Kylan McLin
# Date: 8/2/2020
# Lab5

import csv
import sys


FILENAME = "movies.txt"


def read_movies():
    try:
        movies = []

        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
                
        return movies

    except FileNotFoundError:
        print("Could not find ", FILENAME, " file.")
        exit_program()

    except Exception as e:
        print(type(e), e)
        exit_program()


def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)

    except Exception as e:
        print(type(e), e)
        exit_program()


def exit_program():
    print("terminating program.")
    sys.exit()


def list_movies(movies):
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i+1) + ". " + movie[0])
    print()


def add_movie(movies):
    name = input("Movie: ")
    movie = []
    movie.append(name)
    movies.append(movie)
    write_movies(movies)
    print(name, "was added.\n")


def delete_movie(movies):
    while True:
        try:
            number = int(input("# Movie to delete: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. ", "Please try again.")
        else:
            break

    movie = movies.pop(number - 1)
    write_movies(movies)
    print(movie[0], "was deleted.\n")


def display_menu():
    print("Favorite Movie List Program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("delete -  Delete a movie")
    print("exit - Exit program")
    print()


def main():
    display_menu()
    movies = read_movies()

    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "delete":
            delete_movie(movies)
        elif command.lower() == "exit":
            print("Bye! \n")
            exit_program()
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
