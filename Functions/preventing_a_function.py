# Preventing a function from modifying a list

passengers(listname[:]) # Slice notation makes a copy of the list to send to the function

passengers(not_checked_in[:], checked_in # To send a copy of the list and not the original
