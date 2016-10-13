from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from wanderit import settings


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return settings.OPEN_FOR_SIGNUP


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request, sociallogin):
        return settings.OPEN_FOR_SIGNUP