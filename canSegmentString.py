def can_segment_string(s,dict):
    """This function will check if dict contains the segement for s"""
    for i in range(0, len(s) + 1):
        first = s[0:i]
        if first in dict:
            second = s[i:]
            #print(second)
            if second in dict:
                return True
    return False

if __name__ == '__main__':
    print(can_segment_string('applepie','appleapplepearpie'))
    print(can_segment_string('applepeer','appleapplepearpie'))