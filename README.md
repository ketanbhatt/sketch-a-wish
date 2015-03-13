#Sketch A Wish
A website made for increasing social interaction among the users of the internet. The backend for the site is done on Django.


##To Do:
    + Persist random choice even after refresh,logout*
    + Check for error messages everywhere
    + Enable Sharing on Facebook, google, twitter, instagram
    + Take care of location of users
    + Enable Static files on production server
    + Handle media on production server
    + Show User Profile information inside Users link only


*Add 'choices' field for every user. As soon as the user makes a wish, the 'choices' field gets populated with a list of PKs of 3 wishes that the user has to choose from. Display the drop down from this field. Once the user selects any one of these wishes, the field gets set to NULL. Make a 'is_temp_locked' for every wish for depicting the state for a wish when it is in the 'choices' field of some other user. When the user selects his desired wish, all other wishes' 'is_temp_locked' goes to False.
