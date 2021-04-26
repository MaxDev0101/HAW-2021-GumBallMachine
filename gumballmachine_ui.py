from gumballmachine import State, Message, push

current_state = State.wait_for_coin
current_message = Message.insert_coin

print("Gum Ball Machine 2021 \n")

print("[1] Insert Coin, [2] Request Gum, [3] Get Item, [Other] Exit")

while True:
    selection = input("Please Choose Message: ")
    if selection == "1":
        print("[1] Insert Coin")
        current_message = Message.insert_coin
    elif selection == "2":
        print("[2] Request Gum")
        current_message = Message.request_gum
    elif selection == "3":
        print("[3] Get Item")
        current_message = Message.item_out
    else:
        print("[Other] Exit")
        break

    new_state = push(current_state, current_message)
    print(new_state)
    current_state = new_state
