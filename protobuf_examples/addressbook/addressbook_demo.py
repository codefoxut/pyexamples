import addressbook_pb2
import time


def make_address_book_entry():
    ab = addressbook_pb2.AddressBook()
    p1 = addressbook_pb2.Person()
    p1.name = 'rahul'
    p1.id = 1
    p1.email = 'rahul@ddlj.com'
    phones = p1.phones
    phones.append(addressbook_pb2.Person.PhoneNumber(number='1234567890',
                                                     type=addressbook_pb2.Person.MOBILE))
    print(p1)
    ab.people.extend([p1])
    print(ab)

    p2 = ab.people.add()
    p2.name = 'simran'
    p2.id = 2
    p2.email = 'simran@ddlj.com'
    p2.phones.add(number='0987654321', type=addressbook_pb2.Person.WORK)

    print(ab)


if __name__ == '__main__':
    make_address_book_entry()
