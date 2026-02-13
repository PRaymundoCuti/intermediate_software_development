from email_validator import validate_email, EmailNotValidError # pyright: ignore[reportMissingImports]

def is_numerical(a) -> bool:
    try:
        float(a)
        return True
    except Exception:
        return False

def is_int(a) -> bool:
    if (is_numerical(a)):
        if (a%1==0):
            return True
        else:
            return False
        
def type_str(val) -> str:
    word=str(type(val))
    return word[8:-2]

def comparations_type(val,type1):
    val=type_str(val)
    if(val==type1):
        return True
    else:
        return False

def is_and_greater_than (val1,type1,val2,val_name)->None:
    if(comparations_type(val1,type1)):
        if (not val1>val2):
            raise ValueError(f"{val_name} must be greater than 0")
    else:
        raise TypeError(f"{val_name} must be {type1}, not {val1}")

def is_name(val1,val_name)->None:
    if(not comparations_type(val1,"str")):
        raise TypeError(f"{val_name} must be str, not {val1}")
    elif(val1.strip()==""):
        raise ValueError(f"{val_name} must not be empty")

def email_verificator(email_address):
    try:
        validate_email(email_address, check_deliverability=False)
    except EmailNotValidError:
        raise EmailNotValidError(f"Email: {email_address} is not valid")
