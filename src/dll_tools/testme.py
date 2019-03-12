import pendulum
from numpy import round
from timeit import default_timer as timer

from ChartData import ChartData
from ChartManager import ChartManager
from swissephlib import SwissephLib

def test_nj_area():
    name = 'Mike'
    ldt = pendulum.datetime(2019, 2, 27, 20, 31, 0, tz='America/New_York')
    udt = pendulum.datetime(2019, 2, 28, 1, 31, 0)
    lat = 40.9958
    long = -74.0435

    # TODO: Eventually do these checks with just degree/min/sec and not floats
    ecliptic = {
        'Sun': 314.1574473222989,
        'Moon': 242.31248223042022,
        'Mercury': 332.1508530228922,
        'Venus': 273.06218323415544,
        'Mars': 14.171693744541951,
        'Jupiter': 236.75788601387848,
        'Saturn': 262.6542778677117,
        'Uranus': 4.727366440577683,
        'Neptune': 320.8933177569314,
        'Pluto': 267.41143149288126
    }

    mundane = {
        'Sun': 146.79742300562305,
        'Moon': 71.18931301348978,
        'Mercury': 165.26423810383073,
        'Venus': 103.7315401411139,
        'Mars': 205.09812899050644,
        'Jupiter': 65.96392174555527,
        'Saturn': 92.73263103766716,
        'Uranus': 195.80956452315695,
        'Neptune': 153.37642091894648,
        'Pluto': 97.80109986083579
    }

    RA = {
        'Sun': 340.75288686821625,
        'Moon': 267.1340741579414,
        'Mercury': 356.7020075425924,
        'Venus': 299.9761777212315,
        'Mars': 36.57476357194008,
        'Jupiter': 261.0789262548151,
        'Saturn': 289.0786951081564,
        'Uranus': 27.8386495448017,
        'Neptune': 347.398339836326,
        'Pluto': 294.2457769761652
    }

    chart = ChartData(name, ldt, udt, long, lat)

    # e = chart.get_ecliptical_coords()
    # assert e == ecliptic
    #
    # m = chart.get_mundane_coords()
    # assert m == mundane
    #
    # r = chart.get_right_ascension_coords()
    # assert r == RA

    # TODO: Do checks with degree/min/sec
    assert round(chart.LST - 7.0863, 2) == 0
    assert round(chart.ramc - 106.296, 2) == 0

    cusps = {'1': 167.88191373470818, '2': 199.5851626176927, '3': 230.6383525226713, '4': 260.0082620127005,
             '5': 288.3863500663652, '6': 317.3157694471956, '7': 347.8819137347082, '8': 19.585162617692678,
             '9': 50.63835252267132, '10': 80.00826201270056, '11': 108.3863500663652, '12': 137.3157694471956}

    angles = {'Asc': 167.88191373470818, 'MC': 80.00826201270056, 'Dsc': 347.8819137347082, 'IC': 260.0082620127006,
              'Eq Asc': 172.66636153568209, 'Eq Dsc': 352.6663615356821, 'EP (Ecliptical)': (170.00826201270056,),
              'Zen': 77.88191373470818, 'WP (Ecliptical)': 350.0082620127006, 'Ndr': 257.8819137347082}

    # for key, value in chart.cusps_longitude.items():
    #     assert value == cusps[key]
    #
    for key, value in chart.angles_longitude.items():
        print(key, value)
    #     assert value == angles[key]



def test_natal():
    name = 'Mike'
    ldt = pendulum.datetime(1989, 12, 20, 22, 20, 0, tz='America/New_York')
    udt = ldt.in_tz('UTC')
    lat = 40.9792
    long = -74.1169
    natal_chart = ChartData(name, ldt, udt, long, lat)

    # assert natal_chart.get_ecliptical_coords() == {
    #     'Sun': 244.6313629376893,
    #     'Moon': 167.13759652799106,
    #     'Mercury': 264.38172216168175,
    #     'Venus': 280.5141929178817,
    #     'Mars': 217.43828113917368,
    #     'Jupiter': 72.08233125322747,
    #     'Saturn': 259.7217882439701,
    #     'Uranus': 250.49893171302688,
    #     'Neptune': 257.0068942021749,
    #     'Pluto': 202.15101494641362
    # }
    # assert natal_chart.get_mundane_coords() == {
    #     'Sun': 112.30177637740623,
    #     'Moon': 31.73940479378539,
    #     'Mercury': 130.83782823970748,
    #     'Venus': 146.42614237772526,
    #     'Mars': 84.4099562736074,
    #     'Jupiter': 299.6760710412005,
    #     'Saturn': 127.11796339621995,
    #     'Uranus': 118.00207743229325,
    #     'Neptune': 124.6836834230844,
    #     'Pluto': 68.65188700850499
    # }
    #
    # assert natal_chart.get_right_ascension_coords() == {
    #     'Sun': 269.1625706083745,
    #     'Moon': 189.15316359652076,
    #     'Mercury': 290.83014331163423,
    #     'Venus': 307.6064368752971,
    #     'Mars': 239.96535633889692,
    #     'Jupiter': 97.26967529094908,
    #     'Saturn': 285.514947289806,
    #     'Uranus': 275.5664554682417,
    #     'Neptune': 282.53946438003425,
    #     'Pluto': 228.57596239602026
    # }

    name = 'Transits in LA'
    ldt = pendulum.datetime(2019, 3, 1, 21, 58, 25, tz='America/Los_Angeles')
    udt = ldt.in_timezone('UTC')
    lat = 37.9577
    long = -121.2897
    los_angeles = ChartData(name, ldt, udt, long, lat)



    for x, y in natal_chart.get_mundane_coords().items():
        print(x, y)


swiss_lib = SwissephLib()
manager = ChartManager(swiss_lib)

name = 'Mike'
ldt = pendulum.datetime(1989, 12, 20, 22, 20, 0, tz='America/New_York')
udt = ldt.in_tz('UTC')
lat = 40.9792
long = -74.1169

mike = manager.create_chartdata(name, ldt, long, lat)

name = 'Transits in LA'
ldt = pendulum.datetime(2019, 3, 3, 22, 40, 24, tz='America/Los_Angeles')
udt = ldt.in_timezone('UTC')
lat = 34.0522
long = -118.2427

la = manager.create_chartdata(name, ldt, long, lat)
manager.precess_into_sidereal_framework(radix=mike, transit_chart=la)

dt = pendulum.datetime(2019, 3, 3, 6, 0, 0, tz='America/Argentina/La_Rioja')
lat = -29.4333
long = -66.85

test = manager.create_chartdata('', dt, long, lat)


name = 'Mike'
ldt = pendulum.datetime(1989, 12, 20, 22, 20, 0, tz='America/New_York')
udt = ldt.in_tz('UTC')
lat = 40.9792
long = -74.1169
mike = manager.create_chartdata(name, ldt, long, lat)

now = pendulum.datetime(2019, 3, 11)
start = timer()
L = manager.calculate_return_list(mike, now, 1, 2, 15)
end = timer()
print(end - start)
# for x in L:
#     print(x.utc_datetime)
