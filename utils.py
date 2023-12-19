from typing import List

def get_chunks(docstring: str, size: int, around: int, overlap: int, char_to_split: str = " ", replace_to_char: bool = True) -> List[str]:
    if replace_to_char:
        docstring = char_to_split.join(docstring.split())
    chunks = []
    last_index = 0
    for i in range(1, int(len(docstring)/size)+2):
        finded_idx = docstring[i*size-around:i*size+around].find(char_to_split)
        chunks.append(docstring[last_index:finded_idx+i*size-around])
        last_index = (finded_idx+i*size-around) - overlap
        last_index = docstring[last_index-around:last_index+around].find(char_to_split)+last_index-around+1
    return chunks