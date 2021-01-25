from challenge.purchase import Purchase
from challenge.email import Email
from challenge.item import Item


def challenge():
    """
    Main function that invokes the "calculates_cost_per_email" method, which in turn calculates
    the cost for each email using the variables "items" and "emails".

    :return:
    """

    items = [
        Item(f'item', 1, 100),
    ]
    emails = [
        Email('email_1@email.com'),
        Email('email_2@email.com'),
        Email('email_3@email.com'),
    ]

    purchases = Purchase(items, emails)

    # Through the "purchasing" object created, you can access the function of this Challenge:
    # "calculates_cost_per_email", without having to pass parameters "items" and "emails" to it indirectly.
    purchases.calculates_cost_per_email()


if __name__ == '__main__':
    challenge()
