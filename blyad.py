print("Welcome to the salary calculator!")
print("Note: The calculator calculates 31 days per month")
arbeitsstunden = int(input("Please indicate your working hours in full hours"))
stundenlohn = int(input("Please enter your hourly wage now"))

tageslohn = stundenlohn * arbeitsstunden
wochenlohn = tageslohn * 7
monatslohn = wochenlohn * 4 + 3 * tageslohn


print("Your monthly salary is around " + str(monatslohn) + "$.")
print("")
print("")
print("")

feed_back = int(input("Can you give me a little feedback? 1 = Very good/Good, 3 = Needs improvement 6 = Very bad"))

if feed_back == 1:
    print("Thank you for the lovely feedback, have a nice day.")
elif feed_back == 3:
    print("Thank you very much for the feedback, have a nice day.")
elif feed_back == 6:
    print("Oh, I'm sorry, feel free to write suggestions for improvements in my GitHub. Have a nice day!")
else:
    print("Sorry, I only understand the numbers 1, 3 and 6")


print("Thank you for using my first own program!")
input("Now press a button to end the program...")











