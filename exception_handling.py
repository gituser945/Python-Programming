# input1 = input("Enter 1st number:")
# input2 = input("Enter 2nd number:")


# # try:
# #     div_result = int(input1)/int(input2)
# # except Exception as e: # generic exceptions
# #     print("Exception occured:",e)
# #     div_result = 0

# # print(div_result)


# try:
#     div_result = int(input1)/int(input2)
#     str = 'nick' + 30
# except ZeroDivisionError as e:
#     print(e)
#     div_result = 0
# except TypeError as e:
#     print(e)


# print(div_result)


if __name__ == "__main__":
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try:
        z = x / int(y)

    except Exception as e:
        print("Exception type: ", type(e).__name__)
        print("Exception occurred:", e)
        z = None

    finally:
        print(z)