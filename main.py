from challenge.item import Item
from challenge.purchase import Purchase
from challenge.email import Email
from random import randrange


def creates_random_items_list(size: int, number_of_items: int, price: int) -> list[Item]:
    """
    Creates a list of random items according to parameter values

    :param size:
        Size of purchases list
    :param number_of_items:
        Quatity of items
    :param price:
        Price of each unit of the purchase item
    :return:
        Random item list
    """

    items = []
    for item in range(1, size + 1):
        items.append(
            Item(f'item{item}', number_of_items, price)
        )

    return items


def creates_random_emails_list(size: int) -> list[Email]:
    """
    Creates a list of random emails according to parameter values

    :param size:
        Size of emails list
    :return:
        Random email list
    """

    emails = []
    for email in range(1, size + 1):
        emails.append(
            Email(f'email_{email}@email.com')
        )

    return emails


def challenge():
    """
    Main function that invokes the "calculates_cost_per_email" method, which in turn calculates the cost
    for each email randomly reported by the variables "items_list" and "emails_list".

    :return:
    """

    # this set of variables change how the "creates_random_items_list" and "creates_random_emails_list"
    # functions generate the lists.
    # Simply change the internal numbers of the "randrange" function or
    # the variables "size_of_emails_list" or "size_of_purchases_list".
    size_of_emails_list = 7
    size_of_purchases_list = 1
    number_of_random_items = randrange(1, 100)
    random_price = randrange(1, 100)

    # Use these variables "items_list" and "emails_list" to EVALUATE the challenge,
    # because this assignment with the functions "creates_random_items_list" and "creates_random_emails_list"
    # were only to stress the model well with large lists of data.
    items = creates_random_items_list(size_of_purchases_list, number_of_random_items, random_price)
    emails = creates_random_emails_list(size_of_emails_list)

    purchases = Purchase(items=items, emails=emails)

    # How the "purchases" object was created it is possible to access the
    # challenge function: "calculates_cost_per_email"
    # by passing parameters to it indirectly
    purchases.calculates_cost_per_email()


if __name__ == '__main__':
    challenge()
