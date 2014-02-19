Feature: Simple EchoServer
    Implement a simple version of the EchoServer

    Scenario Outline: EchoServer [just enough]
        Given the message <input>
        When I call echo_me
        Then I see the output <output>

    Examples:
    | input                          | output                               |
    | Message shorter than bs        | ECHO: Message shorter than bs        |
    | Message longer than buffersize | ECHO: Message longer than buffersize |
    | Message at buffersize....      | ECHO: Message at buffersize....      |

