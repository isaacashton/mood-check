# Script that gets the mood of user on a scale of 1 - 10.
# Program runs on startup of computer, therefore this mostly
# represents morning mood. Write 'plot' to plot the graph.
import matplotlib.pyplot as plt

mood = input("Enter your mood on a scale of 1-10: ")

if mood == "plot":
    with open("moods.txt") as read_file:
        values = [int(x) for x in read_file.read().splitlines()]
    plt.plot(range(1, len(values)+1), values)
    plt.xlabel("Days")
    plt.ylabel("Mood level")
    plt.title("Mood Levels over the Past "+ str(len(values)) + " Days"
            + " (Since July 10th, 2019)")
    plt.show()

elif mood.isdigit():
    with open("moods.txt", "a") as append_file:
        append_file.write(mood + "\n")

else:
    print("User gave invalid input")
