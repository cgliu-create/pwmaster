from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


# activation tokens for email confirmations
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()
