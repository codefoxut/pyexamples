from simple_pb2 import SimpleMessage


def make_msg():
    simple_msg = SimpleMessage()
    simple_msg.id = 123
    simple_msg.is_simple = True
    simple_msg.name = "This is a simple Message"
    # simple_msg.sample_list = [1, 2, 3, 5]  // not allowed
    sample_list = simple_msg.sample_list
    sample_list.append(1)
    sample_list.append(2)
    sample_list.append(5)

    print(simple_msg)

    with open('simple.bin', "wb") as f:
        print("write as binary.")
        bytes_string = simple_msg.SerializeToString()
        f.write(bytes_string)

    with open("simple.bin", "rb") as f:
        print("reading binary file.")
        simple_msg_read = SimpleMessage().FromString(f.read())
        print(simple_msg_read)

    print("is_simple?:", simple_msg_read.is_simple)
    print("name?: ", simple_msg_read.name)


if __name__ == '__main__':
    make_msg()
