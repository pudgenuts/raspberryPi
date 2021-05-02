from subprocess import check_output
from time import sleep
from datetime import datetime
from RPLCD.i2c import CharLCD
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--line1')
parser.add_argument('--line2')

args = parser.parse_args()

lcd = CharLCD('PCF8574', 0x27, auto_linebreaks=False)
lcd.clear()
def get_ip():
    cmd = "hostname -I | cut -d\' \' -f1"
    return check_output(cmd, shell=True).decode("utf-8").strip()
while True:
    lcd_line_1 = args.line1
    lcd_line_2 = args.line2
    
    lcd.home()
    lcd.write_string(f'{lcd_line_1}\r\n{lcd_line_2}')
    sleep(10)
