import itertools
from datetime import datetime

def get_min_date(date):
    dates = date.split('/')
    permutations = itertools.permutations(dates, 3)
    result = None

    for permutation in permutations:
        year,month, day = permutation
        if int(year) < 2000:
            year = str(int(year) + 2000)

        try:
            perm_date = datetime.strptime("{0}-{1}-{2}".format(year, month, day), "%Y-%m-%d")
            if not result or result > perm_date:
                result = perm_date
        except Exception as e:
            pass

    if not result:
        return "is invalid"
    else:
        return datetime.strftime(result, "%Y-%m-%d")
    return result


print(get_min_date("1/2/2010"))