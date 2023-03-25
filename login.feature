Feature: Login
  @negative
  Scenario Outline: Multple logins
    Given user is on Login page
    When user logs in as "<user>" with password "<password>"

    And hits login button
    Then the success page appears
    Examples: | user  | password  |
              | user1 | password1 |

    behave --tags negative

    pytest -k negative









    @when(u'user logs in as "{user}" with password "{password}"
    def login1(context,user,password):

    @when(u'user  "{user}" with password "{password}"
    def login2 (context,user,password):






