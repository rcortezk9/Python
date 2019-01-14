# List in while loop

# Create a list of unverified users
unconfirmed_users = ['rene', 'stephanie', 'victoria', 'sophia']

# An empty lis to hold confirmed users
confirmed_users = []

# Add in one unconfirmed user one at a time to current user
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying users: " + current_user.title())
    confirmed_users.append(current_user)

# Displayed all confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
