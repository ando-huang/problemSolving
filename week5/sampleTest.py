# import package

def getBirthdayInfo(profile):
    return {
            'NAME': profile['name'],
            'AGE': profile['age'],
            'DOB': profile['birthday']
            }

def testGetName():
    testSubject = {
            'name': 'Andrew',
            'age': 21,
            'occupation': 'cookie muncher',
            'hometown': 'Minas Tirith',
            'birthday': '09/18/2000'
            }
    result = getBirthdayInfo(testSubject)
    assert result['NAME'] == 'Andrew'
    assert result['AGE'] = 21
    assert result['DOB'] = '09/18/2000'
    return true # reaches if all the asserts succeed

# assert doc
# https://www.w3schools.com/python/ref_keyword_assert.asp

