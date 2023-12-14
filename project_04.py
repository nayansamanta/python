# making caeser ciper 
def encryption(plain_text , shift_key):
    hidden_text=""
    for char in plain_text:
        if char in array:
          position = array.index(char)  # store the position of alphabate 
          new_position = (position+shift_key)%26
          hidden_text += array[new_position]
        else:
            hidden_text+=char
    print("encrypt message is : ",hidden_text)    

def decryption(hidden_text, shift_key):
    plain_text=""
    for char in hidden_text:
        if char in array:
          position = array.index(char)  # store the position of alphabate 
          new_position = (position - shift_key)%26
          plain_text += array[new_position]
        else:
            plain_text+=char
    print("decrypt message is : ",plain_text)    

end_game=False
while not end_game:
    user_input=input("type 'encrypt' for encryption and type 'decrypt' for decryption:")
    text=input("enter your message : ")
    shift_value=int(input("type shift value : "))
    array=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if user_input=="encrypt":
        encryption(plain_text=text , shift_key=shift_value)
    elif user_input=="decrypt":
        decryption(hidden_text=text , shift_key=shift_value)
    play_again=input("Type 'yes' to continoue and Type 'no' for quit the game :")
    if play_again=="no":
        end_game=True
        print("have a nice day nad good bye !")