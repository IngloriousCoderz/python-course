import zlib

message = b"she sells sea shells on the sea shore. the shells that she sells are sea shells i'm sure."
# message = b"Hi, my name is Antony and I'm doing a course on Python" #?
len(message)  # ?

compressed_message = zlib.compress(message)
compressed_message  # ?
len(compressed_message)  # ?

decompressed_message = zlib.decompress(compressed_message)
decompressed_message  # ?
len(decompressed_message)  # ?

print(message == decompressed_message, message is decompressed_message)
