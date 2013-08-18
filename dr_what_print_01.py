# so, what is that data type?

### call with:   what_print('You message', your_data)
def what_print(text_msg, this_struct):
     my_type = type(this_struct).__name__
     if my_type == 'Result':
         print 'Result: %s | ', text_msg, this_struct
     else:
         if my_type == 'dict':
             print 'Dictionary: %s | ', text_msg, this_struct
         else:
             if my_type == 'list':
                 print 'List: %s | ', text_msg, this_struct
             else:
                 print 'Curious: %s | ', text_msg, this_struct
