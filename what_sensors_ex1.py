## (c) 2013 Dale Reagan
## simple read sensors and data type example

## the 'best' way to use such resources is to place them in an
## external file and import them as needed...
###
def what_print(text_msg, this_struct):
    print '\n\tWhat-Print | %s is type:' % (text_msg),
    my_type = type(this_struct).__name__
    if my_type == 'Result':
        print 'Result:\n\t', this_struct
    else:
        if my_type == 'dict':
            print 'Dictionary:\n\t ', this_struct
        else:
            if my_type == 'list':
                print 'List:\n\t', this_struct
            else:
                print 'Curious:\n\t', this_struct
    print '\t-----------\n'
###

import android, time, sys
droid = android.Android()
droid.startSensingTimed(1, 250)
time.sleep(1)

print '\n\t### What type of data do we have? ###\n'
raw_data = droid.readSensors()
print '\tRaw Data Returned by API:\n\t', raw_data, '\n'

## now just fetch the 'results'
raw_result = droid.readSensors().result
print '\tRaw RESULT Data Returned by API:\n\t', raw_result, '\n'

## after adding the 'what_print' function to the code let's see what the 'data types' are
what_print('Raw Data', raw_data)
what_print('Raw Result', raw_result)
### end ###

sys.exit()
######### sample output
 ### What type of data do we have? ###
        Raw Data Returned by API:
        Result(id=2, result={u'light': 89, u'accuracy': 3, u'pitch': -0.17525501549243927, u'xMag': -35.628616000000001, u'azimuth': 0.85555952787399292, u'zforce': 9.8293949999999999, u'yfo
rce': 1.7405846, u'time': 1376845710.2449999, u'yMag': 28.437930999999999, u'zMag': -15.815201999999999, u'roll': -0.0094534987583756447, u'xforce': 0.092924950000000006}, error=None)

        Raw RESULT Data Returned by API:
        {u'light': 89, u'accuracy': 3, u'pitch': -0.17525501549243927, u'xMag': -35.628616000000001, u'azimuth': 0.85555952787399292, u'zforce': 9.8293949999999999, u'yforce': 1.7405846, u't
ime': 1376845710.2449999, u'yMag': 28.437930999999999, u'zMag': -15.815201999999999, u'roll': -0.0094534987583756447, u'xforce': 0.092924950000000006}

        What-Print | Raw Data is type: Result:
        Result(id=2, result={u'light': 89, u'accuracy': 3, u'pitch': -0.17525501549243927, u'xMag': -35.628616000000001, u'azimuth': 0.85555952787399292, u'zforce': 9.8293949999999999, u'yfo
rce': 1.7405846, u'time': 1376845710.2449999, u'yMag': 28.437930999999999, u'zMag': -15.815201999999999, u'roll': -0.0094534987583756447, u'xforce': 0.092924950000000006}, error=None)
        -----------

        What-Print | Raw Result is type: Dictionary:
        {u'light': 89, u'accuracy': 3, u'pitch': -0.17525501549243927, u'xMag': -35.628616000000001, u'azimuth': 0.85555952787399292, u'zforce': 9.8293949999999999, u'yforce': 1.7405846, u't
ime': 1376845710.2449999, u'yMag': 28.437930999999999, u'zMag': -15.815201999999999, u'roll': -0.0094534987583756447, u'xforce': 0.092924950000000006}
        -----------
