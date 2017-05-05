def main():
    def input_item():
        while True:
            str_input = input("What did you purchase?: ")
            break

        while True:
            try:
                int_weight = int(input("How much does your item weigh in"
                                       " pounds? (Round up): "))
            except ValueError:
                print("Sorry, you need to input a whole number.")
                continue
            if int_weight < 0:
                print("Sorry, your response must not be negative.")
                continue
            else:
                # we're happy with the value given.
                # we're ready to exit the loop.
                break

        while True:
            try:
                float_cost = float(input("How much does your item cost in "
                                         "dollars?:$ "))
            except ValueError:
                print("Sorry, you need to input a valid price.")
                continue
            if float_cost < 0:
                print("Sorry, your response must not be negative.")
                continue
            else:
                # we're happy with the value given.
                # we're ready to exit the loop.
                break
        return (str_input, int_weight, float_cost)

    itemlist = []
    weightlist = []
    costlist = []

    for _ in range(3):  # Run input_item() and append result to list 3 times
        item, weight, cost = input_item()
        itemlist.append(item)
        weightlist.append(weight)
        costlist.append(cost)

    sub_total = sum(t for t in costlist)
    shipping_and_handling = sum(t for t in weightlist)*.25 + 5
    tax = sub_total*.09
    fltTotal = sub_total + shipping_and_handling + tax

    print("You have purchased:", itemlist)
    print("Your Sub Total is: ${0:0.2f}".format(sub_total),
          "\nYour Shipping and Handling charges are : ${0:0.2f}"
          .format(shipping_and_handling),
          "\nYour Tax is ${0:0.2f}".format(tax),
          "\nYour Total is: ${0:0.2f}".format(fltTotal))
    print(itemlist, weightlist, costlist)


if __name__ == "__main__":
    main()
