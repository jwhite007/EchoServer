from lettuce import step
from lettuce import world
from echo_client import echo_me


@step('the message (.+$)')
def the_message(step, message):
    world.message = message


@step('I call echo_me')
def call_echo_me(step):
    world.es = echo_me(world.message)


@step('I see the output (.+$)')
def compare(step, expected):
    assert world.es == expected, "Got %s" % world.es
