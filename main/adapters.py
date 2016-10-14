from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from main.models import WanderitUser
from wanderit import settings


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super(AccountAdapter, self).save_user(request, user, form, commit=commit)
        wiuser = WanderitUser.objects.create(user=user)

    def is_open_for_signup(self, request):
        return settings.OPEN_FOR_SIGNUP


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request, sociallogin):
        return settings.OPEN_FOR_SIGNUP

    def save_user(self, request, sociallogin, form=None):
        user = super(SocialAccountAdapter, self).save_user(request, sociallogin, form=form)
        wiuser = WanderitUser.objects.create(user=user)
