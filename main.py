text = input("Enter Your text here: ")

if not text == "":
    a_byte_array = bytearray(text, "utf8")

    byte_list = []

    wait = 0
    while wait <= 5:
        print("." * wait)
        wait += 1
        
    for byte in a_byte_array:
        binary_representation = bin(byte)

        byte_list.append(binary_representation)

    print(f"\n{byte_list}")
else:
    print("you didn't Input Any text!")
