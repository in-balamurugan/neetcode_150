# test_time_map.py
import pytest
from bisect import bisect_right


class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        i = bisect_right(arr, (timestamp, chr(255))) 
        if i == 0:
            return ""
        return arr[i - 1][1]


def main():
    print("Running example from prompt...\n")
    timeMap = TimeMap()
    print(timeMap.set("alice", "happy", 1))  # None
    print(timeMap.get("alice", 1))           # "happy"
    print(timeMap.get("alice", 2))           # "happy"
    print(timeMap.set("alice", "sad", 3))    # None
    print(timeMap.get("alice", 3))           # "sad"


@pytest.fixture(params=[
    (
        (
            ["TimeMap", "set", "get", "get", "set", "get"],
            [[], ["alice", "happy", 1], ["alice", 1], ["alice", 2], ["alice", "sad", 3], ["alice", 3]]
        ),
        [None, None, "happy", "happy", None, "sad"]
    ),
])
def case(request):
    return request.param


def test_time_map(case):
    (ops, args), expected = case
    obj = None
    result = []
    for op, arg in zip(ops, args):
        if op == "TimeMap":
            obj = TimeMap()
            result.append(None)
        elif op == "set":
            result.append(obj.set(*arg))
        elif op == "get":
            result.append(obj.get(*arg))
    assert result == expected


if __name__ == "__main__":
    main()

