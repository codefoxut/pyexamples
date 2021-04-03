import complex_pb2


def make_complex():
    complex_msg = complex_pb2.ComplexMessage()

    # Assignment not allowed to composite field
    # one_dummy = complex_pb2.DummyMessage()
    # one_dummy.id = 1
    # one_dummy.name = "python"
    # complex_msg.one_dummy = one_dummy

    complex_msg.one_dummy.id = 123
    complex_msg.one_dummy.name = "I am dummy message"

    print(complex_msg)

    first = complex_msg.multiple_dummy.add()
    first.id = 23
    first.name = "this is first dummy"

    print(complex_msg)

    complex_msg.multiple_dummy.add(id=24, name="this is second dummy.")

    print(complex_msg)

    third_dummy = complex_pb2.DummyMessage()
    third_dummy.id = 1000
    third_dummy.name = "this is third element."
    complex_msg.multiple_dummy.extend([third_dummy])

    print(complex_msg)

    third_dummy.id = 100
    third_dummy.name = "I am changed now."
    print(third_dummy)

    with open('complex.bin', "wb") as f:
        print("write as binary.")
        bytes_string = complex_msg.SerializeToString()
        f.write(bytes_string)

    with open("complex.bin", "rb") as f:
        print("reading binary file.")
        simple_msg_read = complex_pb2.ComplexMessage().FromString(f.read())
        print(simple_msg_read)


if __name__  == '__main__':
    make_complex()
