'''
Created on 2015. 11. 14.

@author: user
'''

class Singer:
    title_song = 'default song'

    def sing(self):
        msg = 'sing is '
        print(msg, self.title_song, 'lalala~~~')



psy = Singer()
psy.sing()  # sing is  default song lalala~~~

girls = Singer()
girls.sing()  # sing is  default song lalala~~~

girls.title_song='dancing queen'
girls.sing()  # sing is  dancing queen lalala~~~
girls.co = 'SM'

print('company : ',girls.co)

print(id(psy), id(girls), id(Singer))

