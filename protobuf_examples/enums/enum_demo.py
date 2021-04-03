import enum_example_pb2


def make_enum():
    enum_msg = enum_example_pb2.EnumMessage()
    enum_msg.id = 234

    print(enum_msg)

    enum_msg.day_of_the_week = enum_example_pb2.THURSDAY

    print(enum_msg)
    print(enum_example_pb2.WEDNESDAY)

    with open('enums.bin', "wb") as f:
        print("write as binary.")
        bytes_string = enum_msg.SerializeToString()
        f.write(bytes_string)

    with open("enums.bin", "rb") as f:
        print("reading binary file.")
        simple_msg_read = enum_example_pb2.EnumMessage().FromString(f.read())
        print(simple_msg_read)


if __name__ == '__main__':
    make_enum()
