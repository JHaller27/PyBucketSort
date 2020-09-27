import random


class TypeStrategy:
    def get_num_buckets(self) -> int:
        raise NotImplementedError

    def get_max_item_length(self, items) -> int:
        '''
        Should be at most O(n)
        '''
        raise NotImplementedError

    def hash_value(self, value, itr_num: int) -> int:
        raise NotImplementedError


class IntStrategy(TypeStrategy):
    def get_num_buckets(self) -> int:
        return 10

    def get_max_item_length(self, items: list) -> int:
        max_length = 0
        largest_value = 0

        for i in items:
            if i < largest_value:
                continue

            l = 0
            while i > 0:
                l += 1
                i //= 10

            if l > max_length:
                max_length = l
                largest_value = 10**max_length

        return max_length

    def hash_value(self, value: int, itr_num: int) -> int:
        assert value >= 0

        return value // (10**itr_num)


class AsciiStrategy(TypeStrategy):
    def get_num_buckets(self) -> int:
        return 129

    def get_max_item_length(self, items: list) -> int:
        return max(items, key=len)

    def hash_value(self, value: str, itr_num: int) -> int:
        if itr_num > len(value):
            return 0

        return ord(value[-itr_num-1]) + 1


class RadixSort:
    def __init__(self, strategy: TypeStrategy):
        self._strategy = strategy

    def sorted(self, itr) -> list:
        values = list(itr)
        max_len = self._strategy.get_max_item_length(values)
        buckets = [[] for _ in range(self._strategy.get_num_buckets())]

        for itr_num in range(max_len):
            # Distribute
            for el in values:
                idx = self._strategy.hash_value(el, itr_num) % len(buckets)
                buckets[idx].append(el)
            values.clear()

            # Collect
            for b in buckets:
                values.extend(b)
                b.clear()

        return values


def sorted(values, strategy=None):
    def all_are_instances(itr, t):
        for i in itr:
            if not isinstance(i, t):
                return False
        return True

    values = list(values)

    if strategy is None:
        if all_are_instances(values, int):
            strategy = IntStrategy()
        elif all_are_instances(values, str):
            strategy = AsciiStrategy()
        else:
            raise TypeError(f"List contains unsupported types, or element types or mismatched: {values}")

    return RadixSort(strategy).sorted(values)


if __name__ == '__main__':
    def check(itr) -> bool:
        for x, y in zip(itr[:-1], itr[1:]):
            if x > y:
                raise ValueError(f'Mismatch: {x}, {y}')

    print('Generating values.')
    l = [random.randint(0, 10000000) for _ in range(100000)]

    print('Sorting.')
    sl = sorted(l)
    print('Done sorting.')

    print('Checking... ', end='')
    try:
        check(sl)
        print('sorted')
    except ValueError:
        print('NOT sorted')
        print(sl)
