def getTheMostValue(weights: list, values: list, bag: int) -> int:
    return process(0, weights, values, 0, bag)


def process(i, weights, values, already_weight, bag):
    if i == len(weights):
        return 0
    if already_weight >= bag:
        return 0
    if already_weight + weights[i] <= bag:
        return max(values[i]+process(i+1, weights, values, already_weight+weights[i], bag),
                   process(i+1, weights, values, already_weight, bag))
    return process(i+1, weights, values, already_weight, bag)


if __name__ == '__main__':
    value = [1, 2, 3, 1]
    weight = [1, 1, 2, 1]
    print(getTheMostValue(weight, value, 3))
