"""
the application detection eartquake
Modularisation with function
"""


def extration_data():
    """

    date:09 Desember 2021, 0
    Time:2:00:53 WIB
    magnitudo:5.1
    depth:249 km
    location: LS=7.85 BT=-123.44
    epicenter: 69 km Nortwest LEMBATA-NTT
    be perceived:no tsunami potential
    :return:
    """
    conclusion = dict()
    conclusion['date'] = '09 december 2021'
    conclusion['time'] = '2:00:53 WIB'
    conclusion['magnitudo'] = 5.1
    conclusion['location'] = {'ls': 7.85, 'bt': -123.44}
    conclusion['epicenter'] = '69 km Nortwest LEMBATA-NTT'
    conclusion['be perceived'] = 'no tsunami potential'
    return conclusion


def show_data(result):
    print('The last eartquake based on BMKG')
    print(f"Date {result['date']}")
    print(f"Time {result['time']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Location:LS={result['location']['ls']}, BT={result['location']['bt']}")
    print(f"Epicenter {result['epicenter']}")
    print(f"Be perceived {result['be perceived']}")


if __name__ == '__main__':
    print('The main appication')
    result = extration_data()
    show_data(result)
