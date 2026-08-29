from statistics import mean, median


def summarize(values: list[float]) -> dict:
    return {
        "mean": mean(values),
        "median": median(values),
        "count": len(values),
    }


print(summarize([1.0, 2.0, 9.0]))
