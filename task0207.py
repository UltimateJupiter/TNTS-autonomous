from urllib import request
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
import time
import matplotlib.pyplot as plt

coord_center = SkyCoord('10:00:28.60 02:12:21.00', unit=(u.hourangle, u.deg))


def write_merge(ls):

    out = []
    for x in ls:
        out.append(x)
        out.append('\t')
    out[-1] = '\n'
    out_str = ''.join(out)

    return out_str


def visit(coord_raw, arcmin):

    ret = []

    coord = SkyCoord(str(coord_raw[0]) + ' ' + str(coord_raw[1]), unit=(u.deg, u.deg))
    coord_str = coord.to_string('dms').split(' ')
    print(coord_str)

    target_url = 'http://ned.ipac.caltech.edu/cgi-bin/objsearch?in_csys=Equatorial&in_equinox=J2000.0&lon={}&lat={}&radius={}&hconst=73&omegam=0.27&omegav=0.73&corr_z=1&search_type=Near+Position+Search&z_constraint=Unconstrained&z_value1=&z_value2=&z_unit=z&ot_include=ANY&nmp_op=ANY&out_csys=Equatorial&out_equinox=J2000.0&obj_sort=Distance+to+search+center&of=pre_text&zv_breaker=30000.0&list_limit=5&img_stamp=YES'.format(coord_str[0], coord_str[1], arcmin)
    # print(target_url)

    try:
        response = request.urlopen(target_url, timeout=20)
    except:
        print('Open URL Failed')
        return None

    page = str(response.read())

    if 'objects found in NED' not in page:
        return None

    # print(page)
    page = [_[:127] for _ in page.split('  </A>  ')[2:]]

    for line in page:

        basic = line[:78 - 18].split(' ')

        while '' in basic:
            basic.remove('')

        other = line[78:]
        if '<' in other:
            other = other.split('<')[0]

        other = other.split(';')[-1].split(' ')
        # print(other)
        while '' in other:
            other.remove('')

        mag = other[0]

        if 'g' in mag:
            mag = float(mag[:-1])

            if mag <= 21.0:
                basic.append(str(mag))
                ret.append(write_merge(basic))

        elif 'i' in mag:
            mag = float(mag[:-1])

            if mag <= 21.0:
                basic.append(str(mag))
                ret.append(write_merge(basic))

    if len(ret) == 0:
        return None
    else:
        return ret


base_ra = coord_center.ra.deg
base_dec = coord_center.dec.deg

spot_matrix = []
k = np.sqrt(3)

for ra in np.arange(-60, 60.1, 6):
    for dec in np.arange(-34 * k, 35 * k, 2 * k):
        spot_matrix.append((base_ra + ra/60, base_dec + dec/60))

for ra in np.arange(-63, 63, 6):
    for dec in np.arange(-35 * k, 36 * k, 2 * k):
        spot_matrix.append((base_ra + ra/60, base_dec + dec/60))

tag, mark = 0, 0
sums = len(spot_matrix)
file = open('tmp_ls.txt','a')

for spot in spot_matrix:

    tag += 1

    print('Iter {} over {} \t Grabbed {}'.format(str(tag), str(sums), str(mark)))

    result = visit(spot, 2)
    time.sleep(np.random.uniform(0.5, 1.5))

    if result is None:
        continue

    for x in result:
        file.write(x)
        mark += 1

