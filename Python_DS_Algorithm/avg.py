from typing import List


def average(ll: List[int]) -> float | None:
    """
    :rtype: float
    """
    if not ll:
        return None
    return sum(ll) / len(ll)


def test_average():
    # assert 13.5 == average([3, 43, 3, 5])

    test_cases = [
        {
            'name': 'test case 1',
            'input': [3, 43, 3, 5],
            'expected': 13.5
        },
        {
            'name': 'test case 2',
            'input': [43, 5, 6, 3],
            'expected': 14.25
        },
        {
            'name': 'test case 3',
            'input': [4, 65, 22, 44, 343],
            'expected': 95.6
        },
        {
            'name': 'test case 3',
            'input': [],
            'expected': None
        }
    ]

    for test in test_cases:
        assert test['expected'] == average(test['input'])


if __name__ == "__main__":
    result = average([3, 43, 3, 5])
    print(result)
    assert result == 13.5
