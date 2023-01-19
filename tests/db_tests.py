from bd import *

get_connect()

user_id = 123456789
insert_data('fileId1', user_id, 1, 'now')

assert all_photos(user_id) == 1

assert true_answers(user_id) == 1
assert false_answers(user_id) == 0

insert_data('fileId2', user_id, 0, 'now')

assert all_photos(user_id) == 2

assert true_answers(user_id) == 1
assert false_answers(user_id) == 1
