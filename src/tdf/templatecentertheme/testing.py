# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tdf.templatecentertheme


class TdfTemplatecenterthemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tdf.templatecentertheme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tdf.templatecentertheme:default')


TDF_TEMPLATECENTERTHEME_FIXTURE = TdfTemplatecenterthemeLayer()


TDF_TEMPLATECENTERTHEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TDF_TEMPLATECENTERTHEME_FIXTURE,),
    name='TdfTemplatecenterthemeLayer:IntegrationTesting'
)


TDF_TEMPLATECENTERTHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TDF_TEMPLATECENTERTHEME_FIXTURE,),
    name='TdfTemplatecenterthemeLayer:FunctionalTesting'
)


TDF_TEMPLATECENTERTHEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TDF_TEMPLATECENTERTHEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TdfTemplatecenterthemeLayer:AcceptanceTesting'
)
