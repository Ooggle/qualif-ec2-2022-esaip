from pwn import *
import requests
import json
import base64

AES_BLOCK_SIZE = 16

my_json_cookie = '0000000000000000{"name":"Test","unlock":true}000'
server_cookie_decoded = base64.b64decode("ZyYw4tCA7STmjqKuRnW3/VrPXhpo/NhAiHLgpxs6HVR8WpAn9j8lhb8pH90WKhVE==")
log.info("Server cookie - decoded: {}".format(enhex (server_cookie_decoded)))
my_json_cookie_with_dummy_iv = ("A" * AES_BLOCK_SIZE) + my_json_cookie
offset_of_byte_to_control = my_json_cookie_with_dummy_iv.find('0')
log.info("Offset of byte to control: {}".format(offset_of_byte_to_control))
offset_of_byte_to_flip = offset_of_byte_to_control - AES_BLOCK_SIZE #Flip byte in previous block
log.info("Offset of byte to flip: {}".format(offset_of_byte_to_flip))
server_cookie_decoded_copy = bytearray(server_cookie_decoded)
flip_value = server_cookie_decoded_copy[offset_of_byte_to_flip] ^ ord("0") ^ ord("1")
#log.info("Flipping 0x{:02X} to 0x{:02X} at offset {}".format(server_cookie_decoded_copy[offset_of_byte_to_flip], flip_value, offset_of_byte_to_flip))
server_cookie_decoded_copy[offset_of_byte_to_flip] = flip_value
#log.info("Server cookie - after flip: {}".format(enhex (str(server_cookie_decoded_copy))))
server_cookie_encoded_copy = base64.b64encode(server_cookie_decoded_copy).decode("utf-8")
print(server_cookie_encoded_copy)