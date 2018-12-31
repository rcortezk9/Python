# Pop method

subscribers = ['rene@example.com', 'cortez@example.com', 'steph@example.com']
print(subscribers)

popped_subscribers = subscribers.pop()
print(subscribers)

print(popped_subscribers)

subscribers = ['rene@example.com', 'cortez@example.com', 'steph@example.com']
first_subscriber = subscribers.pop(0)

print("Your first subsriver was " + first_subscriber + ".")

subscribers = ['rene@example.com', 'cortez@example.com', 'steph@example.com']
print(subscribers)

subscribers.remove('cortez@example.com')
print(subscribers)

subscribers = ['rene@example.com', 'cortez@example.com', 'steph@example.com']
subscribed_by_mistake = 'rene@example.com'
subscribers.remove(subscribed_by_mistake)

print(subscribers)
print("\nThis person " + subscribed_by_mistake + " did not mean to sign up.")
