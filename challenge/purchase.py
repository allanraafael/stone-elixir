from pprint import pprint
from typing import Union
from challenge.email import Email
from challenge.item import Item


class Purchase:
    """Class used to represent a purchases list"""

    def __init__(self, items: list[Item], emails: list[Email]):
        """
        :param items:
            List of purchase items
        :param emails:
            List of purchase emails
        """

        self.items = items
        self.emails = emails

    @property
    def sum_of_items(self) -> int:
        """
        Obtains the cost sum of the purchase items

        :return:
            Cost sum of the purchase items
        """
        cost = 0
        for item in self.items:
            cost += item.multiplication

        return cost

    @property
    def emails_list_size(self) -> int:
        """
        Gets the size of the mails list

        :return:
            Size of the mails list
        """
        return len(self.emails)

    @property
    def items_list_size(self) -> int:
        """
        Gets the size of the items list

        :return:
            Size of the items list
        """
        return len(self.items)

    def calculates_cost_per_email(self) -> Union[None, dict]:
        """
        Calculates cost per email, i.e. divides the value as equally as possible between the amount of emails (people)

        :return:
            Dictionary where the key is the email and its value is how much the owner of it should pay in that
        """
        dictionary = {}
        sum_of_items = self.sum_of_items

        if self.items_list_size == 0 and self.emails_list_size == 0:
            print('\nEmpty purchase list, enter at least or more items, and try again.')
            print('\nEmpty email list, enter at least or more emails, and try again')
            return
        elif self.items_list_size == 0 and not self.emails_list_size == 0:
            print('\nEmpty purchase list, enter at least or more items, and try again.')
            return
        elif self.emails_list_size == 0 and not self.items_list_size == 0:
            print('\nEmpty email list, enter at least or more emails, and try again')
            return

        print(f'\nTotal value of the purchases list = {sum_of_items}')

        cost_paid_by_the_majority = sum_of_items // self.emails_list_size
        cost_to_distribute_remaining = sum_of_items % self.emails_list_size

        for email in self.emails:
            dictionary.update({
                email.address: cost_paid_by_the_majority
            })

        dictionary_converted_to_mail_list = list(dictionary.keys())

        for iteration in range(1, cost_to_distribute_remaining + 1):
            email = dictionary_converted_to_mail_list[len(dictionary) - iteration]
            dictionary.update({
                email: dictionary.get(email) + 1
            })

        pprint(dictionary)

        sum_of_dictionary_values = 0
        for value in dictionary.values():
            sum_of_dictionary_values += value
        print(f'Sum of the equal cost of the dictionary = {sum_of_dictionary_values}')

        if sum_of_dictionary_values == sum_of_items:
            print("Perfect! The cost split was made without leaving or exceeding the total value of the purchases list")

        return dictionary
