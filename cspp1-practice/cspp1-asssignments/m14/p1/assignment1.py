'''
Author:Gnanika
Date:22 August 2018
'''
import string
class Cipher:
    '''class'''
    def __init__(self, text):
        '''method for creating an instance'''
        self.text = text

    def __len__(self):
        '''method to find the length'''
        count = 0
        for _ in self.text:
            count += 1
        return count

    def shift(self, shift_number):
        '''main cipher method'''
        small_value = ""
        large_value = ""
        small_value = "-" + string.ascii_lowercase + string.ascii_lowercase
        large_value = "-" + string.ascii_uppercase + string.ascii_uppercase
        final_str = ""
        a_1 = len(self.text)
        for i in range(0, a_1):
            if self.text[i] in small_value:
                final_str += small_value[small_value.index(self.text[i]) + shift_number]
            elif self.text[i] in large_value:
                final_str += large_value[large_value.index(self.text[i]) + shift_number]
            else:
                final_str += self.text[i]

        return final_str

def main():
    '''
        main function
    '''
    data_input = input()
    shift_number = int(input())
    cipher_obj = Cipher(data_input)
    print(cipher_obj.shift(shift_number))

if __name__ == "__main__":
    main()
