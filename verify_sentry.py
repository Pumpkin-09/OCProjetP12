from sentry_config import sentry_sdk


def test_erreur():
    # Déclencher une erreur volontaire
    division = 1 / 0

def test_message():
    sentry_sdk.capture_message("Test Sentry - ça marche !")

if __name__ == "__main__":
    test_message()  # Envoi un message
    test_erreur()   # Déclenche une erreur