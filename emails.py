"""
CP1404/CP5632 Practical
Record email and name
"""


def main():
    """Store email and name in a dictionary."""
    email_to_name = {}
    email = input("Email:")
    while email != "":
        name = get_name(email)
        email_to_name[email] = name
        email = input("Email:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    """Generate name by email."""
    email_items = email.split("@")[0]
    name_items = email_items.split(".")
    name = " ".join(name_items).title()
    confirm_name(name)
    return name


def confirm_name(name):
    """Ask for actual name."""
    answer = input(f"Is your name {name}? (Y/n)")
    if answer != "" and answer.upper() != "Y":
        name = input("Name: ")
    return name


main()
