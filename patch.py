import struct

init_code = list(b"\x66\x0F\xCF\x66\x33\xC0\x0F\xA2\x66\x81\xFB\x47\x65\x6E\x75\x75\x54\x0F\x08\x0F\x20\xD8\x0F\x22\xD8\x66\x33\xC0\x66\x8B\xD0\x66\xB9\x50\x02\x00\x00\x0F\x30\xB9\x58\x02\x0F\x30\xB9\x59\x02\x0F\x30\xB9\x68\x02\x0F\x30\xB9\x69\x02\x0F\x30\xB9\x6A\x02\x0F\x30\xB9\x6B\x02\x0F\x30\xB9\x6C\x02\x0F\x30\xB9\x6D\x02\x0F\x30\xB9\x6E\x02\x0F\x30\xB9\x6F\x02\x0F\x30\xB9\x00\x02\x0F\x30\x41\x81\xF9\x0F\x02\x76\xF7\x66\x0F\xCF\xFF\xE7\xF8\xC3")

path = input("File Path: ")
jmp_offset = int(input("jump inst offset: "), 16)
code_offset = int(input("code offset: "), 16)
jmp = list(b"\xe9" + struct.pack("<H", code_offset - jmp_offset - 3))

data = list(open(path, "rb").read())
boot_block = data[-65536:]

boot_block[code_offset:code_offset+len(init_code)]= init_code
boot_block[jmp_offset:jmp_offset+3] = jmp
data[-65536:] = boot_block
open(path+".patched.rom", "wb").write(bytes(data))
print("patched.")