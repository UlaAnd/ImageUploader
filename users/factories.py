from typing import Any, List, Union

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
    def tier_options(
        self, create: bool, extracted: Union[List["TierOptions"], None], **kwargs: Any
    ) -> None:
        if not create:
            return
        if extracted:
            for tier_option in extracted:
                self.tier_options.add(tier_option)
        else:
            tier_option = TierOptionsFactory()
            self.tier_options.add(tier_option)


class TierOptionsFactory(DjangoModelFactory):
    class Meta:
        model = TierOptions
