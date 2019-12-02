#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This program accepts an address and then prints it again but formatted nicel


def address(name, street_number, street_name, city, province, postal_code,
            apartment=None):
    # return the address

    address = name + "\n"
    if apartment is not None:
        address = address + " " + apartment[0] + "-"
    address = address + " " + street_number + " " + street_name + "\n" + city + " " + province + " " + postal_code

    return address


def main():
    # gets a users name and address
    apartment = None

    name = input("Enter your name: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    question = input("Do you have an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apartment = input("Enter your apartment number: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")

    postal_code = input("Enter your postal code: ")

    if apartment is not None:
        add = address(name, street_number, street_name, province, city,
                      postal_code, apartment)
    else:
        add = address(name, street_number, street_name, city,
                      province,  postal_code)
    print(add)


if __name__ == "__main__":
    main()
