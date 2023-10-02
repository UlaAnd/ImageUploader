import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText

from users.models import Tier, TierOptions, UserProfile


class UserProfileFactory(DjangoModelFactory):
    tier = factory.SubFactory("users.factories.TierFactory")
    username = FuzzyText(length=10)

    class Meta:
        model = UserProfile


class TierFactory(DjangoModelFactory):
    class Meta:
        model = Tier

    @factory.post_generation
    def tier_options(self, create, extracted, **kwargs):
        if not create:
            # If not explicitly told to create, do nothing
            return

        if extracted:
            # If you provided a list of TierOptions instances, add them to the ManyToMany relationship
            for tier_option in extracted:
                self.tier_options.add(tier_option)
        else:
            # If not provided, create a TierOptions instance and add it to the ManyToMany relationship
            tier_option = TierOptionsFactory()
            self.tier_options.add(tier_option)


class TierOptionsFactory(DjangoModelFactory):
    class Meta:
        model = TierOptions
