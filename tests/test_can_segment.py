from canSegmentString import can_segment_string

def test_can_segment_one():
    """This function will test the string in the words of dictionary"""
    assert True == can_segment_string('applepie','appleapplepearpie')

def test_can_segment_two():
    """This function will test the string in the words of dictionary"""
    assert False == can_segment_string('applepeer','appleapplepearpie')