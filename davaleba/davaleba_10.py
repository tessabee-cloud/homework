#1

nums = [1,2,3,4,5,6,7,8,9]


def safe_get(list, index):
    return list[index]

try:
   print(safe_get(nums, 0))

except IndexError:
    print("Error: There is no item with this index")

except TypeError:
    print("Error: Index must be an integer")


#2

current_user_1 = {
    "username": "irakli",
    "role": "admin"
}

def safe_get_value(dictionary, key):

    try:
        return dictionary[key]

    except KeyError:
        print("Error: Key '{key}' doesn't exist")
    return "none"


print(safe_get_value(current_user_1, "username"))



#3

try:
    num= int(input("Enter a number: "))

    num_square=num**2
except ValueError:
    print("Error: Number must be an integer")

else:
    print(num_square)

finally:
    print('operation is done')