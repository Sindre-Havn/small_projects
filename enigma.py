# Usefull sites
#  https://www.matematiksider.dk/enigma_eng.html#turing_bombe
#  https://piotte13.github.io/enigma-cipher/
#  https://cryptii.com/pipes/enigma-machine
#

import string
import re
from numba import jit, njit, int32, float32
from numba.experimental import jitclass


def index_of_coinsidence(txt):
     # chance for two characthers being the same
     # should return 1/26=0.038 for random text
     # should return 0.067 for english
    txt = re.sub(r'[^a-z]', '', txt.lower())
    length = len(txt)
    histogram = dict()
    alphabet = string.ascii_lowercase
    alpha_length = len(alphabet)
    for i in alphabet:
        histogram[i] = 0
    for i in txt:
        histogram[i] += 1
    summ = 0
    for i in alphabet:
        c = histogram[i]*(histogram[i]-1)
        if c > 0:
            summ += c
    IoC = summ / ((length*(length-1)))  # /alpha_length)
    # print(IoC)
    return IoC


def index_of_coinsidence_normalized(txt):
    # chance for two characthers being the same
     # should return 1 for random text
     # should return 1.73 for english
    txt = re.sub(r'[^a-z]', '', txt.lower())
    length = len(txt)
    histogram = dict()
    alphabet = string.ascii_lowercase
    alpha_length = len(alphabet)
    for i in alphabet:
        histogram[i] = 0
    for i in txt:
        histogram[i] += 1
    summ = 0
    for i in alphabet:
        c = histogram[i]*(histogram[i]-1)
        if c > 0:
            summ += c
    IoC = summ / ((length*(length-1))/alpha_length)
    # print(IoC)
    return IoC


class I:
    def __init__(self):
        # from reference transated to contacts
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'e', 'b': 'k', 'c': 'm', 'd': 'f', 'e': 'l', 'f': 'g', 'g': 'd', 'h': 'q', 'i': 'v', 'j': 'z', 'k': 'n', 'l': 't',
                             'm': 'o', 'n': 'w', 'o': 'y', 'p': 'h', 'q': 'x', 'r': 'u', 's': 's', 't': 'p', 'u': 'a', 'v': 'i', 'w': 'b', 'x': 'r', 'y': 'c', 'z': 'j'}
        # inv_map = {v: k for k, v in my_map.items()}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'r'


class II:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'a', 'b': 'j', 'c': 'd', 'd': 'k', 'e': 's', 'f': 'i', 'g': 'r', 'h': 'u', 'i': 'x', 'j': 'b', 'k': 'l', 'l': 'h',
                             'm': 'w', 'n': 't', 'o': 'm', 'p': 'c', 'q': 'q', 'r': 'g', 's': 'z', 't': 'n', 'u': 'p', 'v': 'y', 'w': 'f', 'x': 'v', 'y': 'o', 'z': 'e'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'f'


class III:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'b', 'b': 'd', 'c': 'f', 'd': 'h', 'e': 'j', 'f': 'l', 'g': 'c', 'h': 'p', 'i': 'r', 'j': 't', 'k': 'x', 'l': 'v',
                             'm': 'z', 'n': 'n', 'o': 'y', 'p': 'e', 'q': 'i', 'r': 'w', 's': 'g', 't': 'a', 'u': 'k', 'v': 'm', 'w': 'u', 'x': 's', 'y': 'q', 'z': 'o'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'w'


class IV:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'e', 'b': 's', 'c': 'o', 'd': 'v', 'e': 'p', 'f': 'z', 'g': 'j', 'h': 'a', 'i': 'y', 'j': 'q', 'k': 'u', 'l': 'i',
                             'm': 'r', 'n': 'h', 'o': 'x', 'p': 'l', 'q': 'n', 'r': 'f', 's': 't', 't': 'g', 'u': 'k', 'v': 'd', 'w': 'c', 'x': 'm', 'y': 'w', 'z': 'b'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'k'


class V:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'v', 'b': 'z', 'c': 'b', 'd': 'r', 'e': 'g', 'f': 'i', 'g': 't', 'h': 'y', 'i': 'u', 'j': 'p', 'k': 's', 'l': 'd',
                             'm': 'n', 'n': 'h', 'o': 'l', 'p': 'x', 'q': 'a', 'r': 'w', 's': 'm', 't': 'j', 'u': 'q', 'v': 'o', 'w': 'f', 'x': 'e', 'y': 'c', 'z': 'k'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'a'


class VI:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'j', 'b': 'p', 'c': 'g', 'd': 'v', 'e': 'o', 'f': 'u', 'g': 'm', 'h': 'f', 'i': 'y', 'j': 'q', 'k': 'b', 'l': 'e',
                             'm': 'n', 'n': 'h', 'o': 'z', 'p': 'r', 'q': 'd', 'r': 'k', 's': 'a', 't': 's', 'u': 'x', 'v': 'l', 'w': 'i', 'x': 'c', 'y': 't', 'z': 'w'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'an'


class VII:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'n', 'b': 'z', 'c': 'j', 'd': 'h', 'e': 'g', 'f': 'r', 'g': 'c', 'h': 'x', 'i': 'm', 'j': 'y', 'k': 's', 'l': 'w',
                             'm': 'b', 'n': 'o', 'o': 'u', 'p': 'f', 'q': 'a', 'r': 'i', 's': 'v', 't': 'l', 'u': 'p', 'v': 'e', 'w': 'k', 'x': 'q', 'y': 'd', 'z': 't'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'an'


class VIII:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'f', 'b': 'k', 'c': 'q', 'd': 'h', 'e': 't', 'f': 'l', 'g': 'x', 'h': 'o', 'i': 'c', 'j': 'b', 'k': 'j', 'l': 's',
                             'm': 'p', 'n': 'd', 'o': 'z', 'p': 'r', 'q': 'a', 'r': 'm', 's': 'e', 't': 'w', 'u': 'n', 'v': 'i', 'w': 'u', 'x': 'y', 'y': 'g', 'z': 'v'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = 'an'


class Beta:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'l', 'b': 'e', 'c': 'y', 'd': 'j', 'e': 'v', 'f': 'c', 'g': 'n', 'h': 'i', 'i': 'x', 'j': 'w', 'k': 'p', 'l': 'b',
                             'm': 'q', 'n': 'm', 'o': 'd', 'p': 'r', 'q': 't', 'r': 'a', 's': 'k', 't': 'z', 'u': 'g', 'v': 'f', 'w': 'u', 'x': 'h', 'y': 'o', 'z': 's'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = ''


class Gamma:
    def __init__(self):
        self.contacts = 'abcdefghijklmnopqrstuvwxyz'
        self.ring_forward = {'a': 'f', 'b': 's', 'c': 'o', 'd': 'k', 'e': 'a', 'f': 'n', 'g': 'u', 'h': 'e', 'i': 'r', 'j': 'h', 'k': 'm', 'l': 'b',
                             'm': 't', 'n': 'i', 'o': 'y', 'p': 'c', 'q': 'w', 'r': 'l', 's': 'q', 't': 'p', 'u': 'z', 'v': 'x', 'w': 'v', 'x': 'g', 'y': 'j', 'z': 'd'}
        self.ring_backward = {value: key for key,
                              value in self.ring_forward.items()}
        self.notch = ''


class Reflector_A:
    def __init__(self):
        self.contacts = 'ejmzalyxvbwfcrquontspikhgd'


class Reflector_B:
    def __init__(self):
        self.contacts = 'yruhqsldpxngokmiebfzcwvjat'


class Reflector_C:
    def __init__(self):
        self.contacts = 'fvpjiaoyedrzxwgctkuqsbnmhl'


class Reflector_B_thin:
    def __init__(self):
        self.contacts = 'enkqauywjicopblmdxzvfthrgs'


class Reflector_C_thin:
    def __init__(self):
        self.contacts = 'rdobjntkvehmlfcwzaxgyipsuq'


I_ = I()
II_ = II()
III_ = III()
IV_ = IV()
V_ = V()
VI_ = VI()
VII_ = VII()
VIII_ = VIII()
beta_ = Beta()
gamma_ = Gamma()
A_ = Reflector_A()
B_ = Reflector_B()
C_ = Reflector_C()
B_thin_ = Reflector_B_thin()
C_thin_ = Reflector_C_thin()


def rotate_list(l, n):
    return l[n:] + l[:n]


def f(x):
    if x == 1 or x == 0:
        return 1
    elif x == None or x < 0:
        return None
    else:
        return x*f(x-1)

# specs = [('value', int32),('array', float32)]
# @jitclass()


class Enigma:
    def __init__(self, rotors, initial_rotor_settings, pluggboard_settings, reflector, ring_settings):
        self.init_settings(rotors, initial_rotor_settings,
                           pluggboard_settings, reflector, ring_settings)

    def init_settings(self, rotors, initial_rotor_settings, pluggboard_settings, reflector, ring_settings):
        # when rotor_sett change, the rotors class change as well
        # Inputs are rotors and corresponsive values from left to right
        #  therefore they are reversed below to make their arangement cronological
        self.rotor_sett = rotors[::-1]
        self.initial_rotor_settings = initial_rotor_settings[::-1]
        self.pluggboard_settings = pluggboard_settings
        self.reflector = reflector
        self.ring_settings = ring_settings[::-1]  # if no input, return ()

        reflector_dict = dict()
        alphabet = string.ascii_lowercase
        for i in range(len(alphabet)):
            reflector_dict[alphabet[i]] = self.reflector.contacts[i]
        self.reflector = reflector_dict

        self.rotors = []
        idx = 0
        for i in self.rotor_sett:  # Rotor settings
            self.rotors.append(i)
            # 'abcdefghijk'[-2:]+'abcdefghijk'[:-2]
            self.rotors[idx].contacts = rotate_list(
                i.contacts, self.initial_rotor_settings[idx])
            # print(self.rotors[idx].reference[0], self.rotors[idx].reference)
            idx += 1

        count_letters = len(self.rotors[0].contacts)
        for k in range(len(self.rotors)):  # sett ring settings
            rotor = self.rotors[k]
            turns = self.ring_settings[k]
            new_ring_settings = {}
            for i in iter(rotor.ring_forward):
                prev_value = rotor.ring_forward[i]
                new_char = chr((ord(i)-97+turns) % count_letters + 97)
                new_ring_settings[new_char] = chr((ord(prev_value)-97+turns) %
                                                  count_letters + 97)
            rotor.ring_forward = new_ring_settings
            new_ring_settings = {}
            for i in iter(rotor.ring_backward):
                prev_value = rotor.ring_backward[i]
                new_char = chr((ord(i)-97+turns) % count_letters + 97)
                new_ring_settings[new_char] = chr((ord(prev_value)-97+turns) %
                                                  count_letters + 97)
            rotor.ring_backward = new_ring_settings

        # Number of rotors to choose from
        k = 10
        # Number of rotors in enigma (slots)
        l = len(rotors)
        # Number of characters on rotor
        n = len(rotors[0].contacts)
        # Number of wirepairs
        m = len(pluggboard_settings)
        # Number of reflectors to choose
        o = 5
        if m > 0:
            self.combinations = int(
                o * f(k)/f(k-l) * n**l * f(n) / (f(n-2*m) * f(m) * 2**m))
        else:
            self.combinations = int(
                o * f(k)/f(k-l) * n**l * f(n) / (f(n-0) * 1 * 1))

    def encode_decode(self, txt):
        txt = re.sub(r'[^a-z]', '', txt.lower())
        # print(txt)
        txt = self.pluggboard(txt)
        txt = self.rotor_cipher(txt)
        txt = self.pluggboard(txt)
        # print('\n\n\n'+txt)
        # print('The settings gives', self.combinations, 'different combinations!')
        return txt

    def pluggboard(self, txt):  # verified
        new_txt = ''
        pluggdict = dict()
        for i, j in self.pluggboard_settings:
            il, jl = i.lower(), j.lower()
            pluggdict[il] = jl
            pluggdict[jl] = il
        for i in txt:
            try:
                new_txt += pluggdict[i]  # check if letter in dict
            except Exception:
                new_txt += i
        return new_txt

    def rotor_cipher(self, txt):
        new_txt = ''
        rotors = self.rotors
        for i in txt:
            self.recursive_rotor_step(0, len(rotors), rotors)  # rotate rotors
            var = i
            for i in range(0, len(rotors)):  # forwarding the signal
                if i == 0:  # Signal enters the first rotor
                    var = rotors[0].contacts[string.ascii_lowercase.index(
                        var)]
                # Signal redirected within a rotor
                var = rotors[i].ring_forward[var]
                if i+1 == len(rotors):  # Signal goes from last rotor to the reflector
                    var = string.ascii_lowercase[rotors[len(
                        rotors)-1].contacts.index(var)]
                else:  # Signal goes from one rotor and enters the next
                    var = rotors[i+1].contacts[rotors[i].contacts.index(var)]

            var = self.reflector[var]  # Signal enters the reflector

            for i in range(len(rotors)-1, -1, -1):  # Signal go back trough the rotors
                if i == len(rotors)-1:  # Signal goes from the reflector to the first rotor
                    var = rotors[i].contacts[string.ascii_lowercase.index(
                        var)]
                # Signal redirected within a rotor
                var = rotors[i].ring_backward[var]
                if i == 0:  # Signal leaves the last rotor and into the puggboard
                    var = string.ascii_lowercase[rotors[0].contacts.index(
                        var)]
                else:  # Signal goes from one rotor to another
                    var = rotors[i-1].contacts[rotors[i].contacts.index(var)]
            new_txt += var

        return new_txt

    # Rotates the rotors one step when a 'button' is clicked
    def recursive_rotor_step(self, x, n, rotors):
        if x == n:
            return
        rotors[x].contacts = rotate_list(rotors[x].contacts, 1)
        for i in rotors[x].notch:
            if rotors[x].contacts[0] == i:
                # print('WHEEL: ',x+1+1, 'ROTATES!')
                return self.recursive_rotor_step(x+1, n, rotors)
        return


txt = """boot klar x bei j schnoor j etwa zwo siben x nov x sechs nul cbm x proviant bis zwo nul x dez x benoetige glaeser y noch vier klar x stehe marqu bruno bruno zwo funf x lage wie j schaefer j x nnn www funf y eins funf mb steigend y gute sicht vvv j rasch"""


# Code for finding the rotor combination, this is not finished
def find_enigma_combination(e, rotors, txt):
    IoC_combinations = dict()
    for i in range(len(rotors)-1):
        i = rotors[i]
        for j in range(len(rotors)-1):
            j = rotors[j]
            for k in range(len(rotors)-1):
                k = rotors[k]
                if len(set((i, j, k))) < 3:
                    continue
                print(i, j, k)
                local_best_IoC = 0
                for l in range(26):
                    print(l)
                    for m in range(26):
                        for n in range(26):
                            e.init_settings([i, j, k], [l, m, n], [], B, [])
                            encryption = e.encode_decode(txt)
                            IoC = index_of_coinsidence(encryption)
                            if IoC > local_best_IoC:
                                local_best_IoC = IoC
                IoC_combinations[IoC] = [i, j, k]
                # print(encryption)
                print(local_best_IoC, '\n')
    return IoC_combinations


e = Enigma([I_, II_, III_], [4, 3, 24], ['qw', 'er', 'ty',
                                         'ui', 'op', 'as', 'df', 'gh', 'jk', 'lz'], B_, [3, 2, 1])
encryption = e.encode_decode(txt)
print(encryption)
print('\n')

# Create new rotor instances which are unmanipulated
I_, II_, III_ = I(), II(), III()
e.init_settings([I_, II_, III_], [4, 3, 24], ['qw', 'er', 'ty',
                                              'ui', 'op', 'as', 'df', 'gh', 'jk', 'lz'], B_, [3, 2, 1])
encryption = e.encode_decode(encryption)
print(encryption)
