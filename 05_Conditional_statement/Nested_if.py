#  Write a program to check if a person is eligible to vote or not.
#  If a person is 18 or above and a citizen of Pakistan then he/she is eligible to vote otherwise not.

person = int(input("Enter your age: "))
citizen = input("Are you a citizen of Pakistan? (yes/no): ")
if person > 18:
    if citizen == "yes" or citizen == "Yes" or citizen == "YES" or citizen == "y" or citizen == "Y" :
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
else:
    print("You are not eligible to vote")


