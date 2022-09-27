import base64
#This is a byte64 coder/decoder module
def encoder(text):

    text_byte_like = text.encode(encoding="ascii")

    text_base64bytes = base64.b64encode(text_byte_like)

    return str(text_base64bytes).strip("'b")

def decoder(text):

    str_to_byte_like = text.encode(encoding="ascii")
    
    byte_to_str = base64.b64decode(str_to_byte_like)

    byte_to_str = str(byte_to_str).strip("'b")
    
    return byte_to_str




