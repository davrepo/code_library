from typing import List

def join(xs: List[str], sep: str) -> str:
    """Join returns a string with the elements from the list joined by sep."""
    generated_string: str = ""
    
    for item in xs:
        if generated_string == "":
            generated_string = str(item)
        else:
            generated_string += sep + str(item)
        
    return generated_string