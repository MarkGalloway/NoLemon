import django.dispatch as dispatch

# A new player has registered.
player_registered = dispatch.Signal(providing_args=["user", "request"])

# A player has activated his or her account.
player_activated = dispatch.Signal(providing_args=["user", "request"])
