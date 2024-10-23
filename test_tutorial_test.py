import unreal


def test_upper():
    upper = "foo".upper()
    if upper != "FOO":
        unreal.log_error(f"Expected `upper` to be '`FOO', not {upper}.")


def test_fail_me():
    unreal.log_error("I was supposed to fail!")


if __name__ == "__main__":
    test_upper()
    test_fail_me()