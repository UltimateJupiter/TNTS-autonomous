import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord
from astropy import units as u

file = open('0210_list.txt', 'r')

stars, galaxies = [], []

x_, y_, s_ = [], [], []

for x in file:
    k = x.split('\t')
    if len(k) == 6:

        if float(k[5]) < 17:
            
            crd = SkyCoord(''.join([k[2],' ',k[3]]), unit=(u.hourangle, u.deg))
            base_ra = crd.ra.deg
            base_dec = crd.dec.deg
            x_.append(base_ra)
            y_.append(base_dec)

            s_.append((17 - float(k[5]))**5/15)

        # print(k[4])
        if k[4] == '*':
            stars.append(float(k[5][:-1]))
        elif k[4] == 'G':
            galaxies.append(float(k[5][:-1]))
'''
print(stars)
plt.figure(figsize=(8, 6))
plt.hist(stars, 50)
plt.grid(True)
plt.xticks(range(10, 22))
plt.title('Stars',fontsize=14)
plt.xlabel('Mag')
plt.savefig('s10.png', dpi=150)
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(galaxies, 50)
plt.grid(True)
plt.xticks(range(14, 22))
plt.xlabel('Mag')
plt.title('Galaxies', fontsize=14)
plt.savefig('g10.png', dpi=150)
plt.figure(figsize=(8, 6))
plt.show()
'''
plt.figure(figsize=(10, 10))
plt.scatter(x_,y_,s_)
'''
for n in range(len(x_)):
    plt.scatter(x_[n], y_[n], s=s_[n])
'''
plt.savefig('test.jpg',dpi=150)
plt.show()
