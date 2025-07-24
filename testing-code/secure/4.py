import pytest
import time

def strong_password(password):
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password)
    )

class LoginSimulator:
    def __init__(self):
        self.attempts = {}
        self.locked = set()

    def login(self, user, password):
        if user in self.locked:
            return False
        if not strong_password(password):
            return False
        self.attempts[user] = self.attempts.get(user, 0) + 1
        if self.attempts[user] > 5:
            self.locked.add(user)
            return False
        return True

@pytest.mark.parametrize("user,password", [
    ("bob", "Weak1"),
    ("alice", "StrongPass1")
])
def test_login_rate_limit(user, password):
    sim = LoginSimulator()
    for _ in range(6):
        sim.login(user, password)
    assert (user in sim.locked) or strong_password(password)
