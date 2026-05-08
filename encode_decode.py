import random 
def encode(val):
  high_byte= val>>8
  low_byte=val & 0xFF
  return high_byte, low_byte
def decode(high_byte, low_byte):
  return (high_byte<<8) | low_byte
def run_checks():
  print("bitwise logic test")
  for _ in range(10):
    original_value=random.randint(0,4095)
    h,l=encode(original_value)
    decoded_value=decode(h,l)
    status="pass" if original_value==decoded_value else "fail"
    print(f"Original: {original_value}, Encoded: ({h}, {l}), Decoded: {decoded_value} - {status}")
if __name__=="__main__":
  run_checks()