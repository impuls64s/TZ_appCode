def check_relation(net, first, second):

    all_friends = []

    def inner(args):
        all_friends.append(args)

        friends = []
        for n in net:
            if args in n:
                new_friend = [name for name in n if name not in all_friends]
                friends.extend(new_friend)

        if second in friends:
            return True

        if not friends:
            return False

        if len(friends) == 1:
            return inner(friends[0])

        if len(friends) > 1:
            for name in friends:
                fn = [f for f in net if name in f]
                if len(fn) > 1:
                    return inner(name)
    return inner(first)


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
