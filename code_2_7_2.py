class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
        print('I am climbing the tree')

monkey_1 = Monkey()
monkey_2 = Monkey()

all_monkeys = [monkey_1, monkey_2]
for monkeys in all_monkeys:
    monkeys.climb()
    print(getattr(monkeys, 'max_age'))
    print(getattr(monkeys, 'loves_bananas'))
