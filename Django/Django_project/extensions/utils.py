from . import jalali

def jalali_converter(time):
    time_to_str = ""
    output = jalali.Gregorian(str(time)).persian_string()
    return output