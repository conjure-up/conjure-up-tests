from behave import given, when, then, step

from lxd import *


@given(u'we have a lxd profile')
def step_impl(context):
    conjure_up()
    print("ran conjure-up")

@when(u'a non default zfs pool is defined')
def step_impl(context):
    pass

@then(u'conjure-up will deploy canonical-kubernetes')
def step_impl(context):
    pass
