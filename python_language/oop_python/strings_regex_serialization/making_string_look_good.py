'''
till we have worked on different datatypes we never bothered or thought about representing them in
a good way we just represented them in a way which is represented by python itself 

'''

subtotal=12.34
tax=subtotal * 0.44
total=subtotal+tax

print(f"""the subtotal is : {subtotal}
      the tax is :{tax}
      the total is :{total}
      """)

#remember this when % and % to specify the formats normally at the end but we can do like this also

print(f"""the subtotal is : {"%0.1f" %subtotal} 
      the tax is :{"%0.2f" %tax}
      the total is :{"%0.2f" %total}
      """)

"""
there are other ways but I think this is best for readability so I mostly use this format
"""

"""
strings are unicode 

you may think ok python could figure out how its represented but most of the time its an yes but
one time I stuck for 4 hours just to specify encoding as 'utf-8' while scraping a website
which is where we need to be specific on what is encoding and what is happening under the hood
how are characters are represented

most of the times characters are represented as ascii which is compatible with unicode i.e normally
you can use ascii everywhere but when you wanted to represent the chinese characters or want to
work on files that might contain those characters you need to provide an encoding and decoding standard

you can ask why not use unicode every where as it can represent(encode ) and decode every characters 
in the word 
but it all comes down to memory ascii encodes to 8bit representing 128 characters
unicode encodes to 16 bit representing more than 120,000 characters

é
"""

characters=b"\x63\x6c\xe9"

print(characters.decode("latin-1"))

characters="cliché"
print(characters)
print(characters.encode('UTF-8'))
print(characters.encode('latin-1'))
print(characters.encode('UTF-16'))
#print(characters.encode('ascii')) #ascii cant encode the above string as it excedes its limits